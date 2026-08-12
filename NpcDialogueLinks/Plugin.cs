using Dalamud.Game.Addon.Lifecycle;
using Dalamud.Game.Command;
using Dalamud.Interface;
using Dalamud.Interface.Windowing;
using Dalamud.Game.Text.SeStringHandling;
using Dalamud.Game.Text.SeStringHandling.Payloads;
using Dalamud.IoC;
using Dalamud.Plugin;
using Dalamud.Plugin.Services;
using System.Text.Json;

namespace NpcDialogueLinks;

public sealed class Plugin : IDalamudPlugin
{
    private const string CommandName = "/npclinks";
    private const uint LinkCommandId = 0x4E50434C;

    [PluginService]
    internal static IDalamudPluginInterface PluginInterface { get; private set; } = null!;

    [PluginService]
    internal static IAddonLifecycle AddonLifecycle { get; private set; } = null!;

    [PluginService]
    internal static ICommandManager CommandManager { get; private set; } = null!;

    [PluginService]
    internal static IClientState ClientState { get; private set; } = null!;

    [PluginService]
    internal static IChatGui ChatGui { get; private set; } = null!;

    [PluginService]
    internal static IDataManager DataManager { get; private set; } = null!;

    [PluginService]
    internal static IPluginLog Log { get; private set; } = null!;

    [PluginService]
    internal static ITargetManager TargetManager { get; private set; } = null!;

    private readonly DialogueCapture dialogueCapture;
    private readonly DialogueHistory dialogueHistory = new();
    private readonly DictionaryWindow dictionaryWindow;
    private readonly GameContextProvider gameContextProvider;
    private readonly LoreExplainClient loreExplainClient = new();
    private readonly LoreExplainWindow loreExplainWindow;
    private readonly DalamudLinkPayload linkPayload;
    private readonly PluginConfiguration configuration;
    private readonly QuestMetadataProbe questMetadataProbe;
    private readonly SettingsWindow settingsWindow;
    private readonly TermDictionary termDictionary;
    private readonly WindowSystem windowSystem = new("NpcDialogueLinks");
    private CancellationTokenSource? loreExplainCancellationTokenSource;

    private string lastDialogue = string.Empty;
    private IReadOnlyList<string> lastCandidates = Array.Empty<string>();
    private LoreExplainRequest? lastLoreExplainRequest;
    private LoreExplainResult? lastLoreExplainResult;

    public Plugin()
    {
        var pluginDirectory = PluginInterface.AssemblyLocation.DirectoryName;
        if (string.IsNullOrWhiteSpace(pluginDirectory))
        {
            pluginDirectory = AppContext.BaseDirectory;
        }

        this.configuration = PluginInterface.GetPluginConfig() as PluginConfiguration ?? new PluginConfiguration();
        this.configuration.Initialize(PluginInterface);
        this.loreExplainWindow = new LoreExplainWindow(this.HandleLoreExplainFollowUp, this.SaveDictionaryProposal);
        this.gameContextProvider = new GameContextProvider(ClientState, DataManager, TargetManager);
        this.questMetadataProbe = new QuestMetadataProbe(PluginInterface, AddonLifecycle, ClientState, DataManager, TargetManager);
        this.termDictionary = new TermDictionary(
            Path.Combine(pluginDirectory, "terms.json"),
            Path.Combine(PluginInterface.ConfigDirectory.FullName, "user-terms.json"));
        this.dictionaryWindow = new DictionaryWindow(this.termDictionary, this.RefreshLastCandidates);
        this.settingsWindow = new SettingsWindow(this.configuration);
        this.windowSystem.AddWindow(this.dictionaryWindow);
        this.windowSystem.AddWindow(this.settingsWindow);
        this.windowSystem.AddWindow(this.loreExplainWindow);
        this.linkPayload = ChatGui.AddChatLinkHandler(LinkCommandId, this.OnLinkClicked);
        this.dialogueCapture = new DialogueCapture(AddonLifecycle, this.OnDialogueChanged);
        PluginInterface.UiBuilder.Draw += this.DrawUi;

        CommandManager.AddHandler(
            CommandName,
            new CommandInfo(this.OnCommand)
            {
                HelpMessage = "Use /npclinks show, /npclinks list, /npclinks dict, /npclinks config, /npclinks lore, /npclinks questprobe, or /npclinks explain <dialogue> | <question>.",
            });

        Log.Information("NPC Dialogue Links loaded.");
    }

    public void Dispose()
    {
        PluginInterface.UiBuilder.Draw -= this.DrawUi;
        this.loreExplainCancellationTokenSource?.Cancel();
        this.loreExplainCancellationTokenSource?.Dispose();
        this.dialogueCapture.Dispose();
        this.questMetadataProbe.Dispose();
        CommandManager.RemoveHandler(CommandName);
        ChatGui.RemoveChatLinkHandler(LinkCommandId);
        this.windowSystem.RemoveAllWindows();
        this.loreExplainClient.Dispose();
    }

    private void OnDialogueChanged(string dialogue)
    {
        this.lastDialogue = dialogue;
        this.dialogueHistory.Add(dialogue);
        this.lastCandidates = LinkCandidateExtractor.Extract(dialogue, this.termDictionary.MatchTerms);

        if (this.questMetadataProbe.Enabled)
        {
            var result = this.CaptureQuestProbe("auto-dialogue", string.Empty);
            if (!result.Succeeded)
            {
                ChatGui.Print(result.Message, "NPC Links");
            }
        }

        if (this.lastCandidates.Count == 0)
        {
            return;
        }

        ChatGui.Print(this.BuildCandidateMessage(this.lastCandidates), "NPC Links");
    }

    private SeString BuildCandidateMessage(IReadOnlyList<string> candidates)
    {
        var builder = new SeStringBuilder()
            .Append("Detected from dialogue: ");

        for (var index = 0; index < candidates.Count; index++)
        {
            if (index > 0)
            {
                builder.Append("  ");
            }

            builder.Append(SeString.TextArrowPayloads);
            builder.Append(new Payload[] { this.linkPayload });
            builder.Append(candidates[index]);
            builder.Append(new Payload[] { RawPayload.LinkTerminator });
        }

        return builder.BuiltString;
    }

    private void OnLinkClicked(uint commandId, SeString payload)
    {
        _ = commandId;

        var clickedText = payload.TextValue.Trim();
        if (string.IsNullOrWhiteSpace(clickedText))
        {
            clickedText = "(unknown)";
        }

        ChatGui.Print($"Clicked candidate: {clickedText}", "NPC Links");

        if (this.termDictionary.TryGetEntry(clickedText, out var entry))
        {
            var label = string.Equals(clickedText, entry.CanonicalName, StringComparison.Ordinal)
                ? clickedText
                : $"{clickedText} ({entry.CanonicalName})";

            ChatGui.Print($"{label}: {entry.Definition}", "NPC Links");
        }

        if (!string.IsNullOrWhiteSpace(this.lastDialogue))
        {
            Log.Information($"Clicked dialogue candidate '{clickedText}' from dialogue: {this.lastDialogue}");
        }
    }

    private void OnCommand(string command, string arguments)
    {
        _ = command;

        var trimmed = arguments.Trim();
        if (string.IsNullOrEmpty(trimmed))
        {
            this.PrintStatus();
            return;
        }

        var parts = trimmed.Split(' ', 2, StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries);
        var subcommand = parts[0].ToLowerInvariant();

        switch (subcommand)
        {
            case "dict":
                if (parts.Length > 1)
                {
                    this.HandleDictionaryCommand(parts[1]);
                }
                else
                {
                    this.dictionaryWindow.Toggle();
                }

                break;
            case "config":
            case "settings":
                this.settingsWindow.Toggle();
                break;
            case "lore":
            case "explainwindow":
                this.loreExplainWindow.IsOpen = true;
                break;
            case "questprobe":
            case "qprobe":
                this.HandleQuestProbeCommand(parts.Length > 1 ? parts[1] : string.Empty);
                break;
            case "list":
                this.PrintTriggerList();
                break;
            case "show":
                this.PrintStatus();
                break;
            case "explain":
                this.HandleLoreExplain(parts.Length > 1 ? parts[1] : string.Empty);
                break;
            default:
                ChatGui.Print("Usage: /npclinks [dict|questprobe|config|lore|show|list|explain <dialogue> | <question>]", "NPC Links");
                break;
        }
    }

    private void HandleDictionaryCommand(string arguments)
    {
        var trimmed = arguments.Trim();
        if (string.IsNullOrWhiteSpace(trimmed))
        {
            this.dictionaryWindow.Toggle();
            return;
        }

        var parts = trimmed.Split(' ', 2, StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries);
        var action = parts[0].ToLowerInvariant();
        var rest = parts.Length > 1 ? parts[1] : string.Empty;

        switch (action)
        {
            case "open":
                this.dictionaryWindow.Toggle();
                break;
            case "set":
            case "add":
            case "update":
                this.HandleDictionarySetCommand(rest);
                break;
            case "delete":
            case "remove":
                this.HandleDictionaryDeleteCommand(rest);
                break;
            case "reload":
                this.PrintDictionaryMutationResult(this.termDictionary.Reload());
                this.RefreshLastCandidates();
                break;
            case "path":
                ChatGui.Print($"Bundled dictionary: {this.termDictionary.BundledDictionaryPath}", "NPC Links");
                ChatGui.Print($"User dictionary: {this.termDictionary.UserDictionaryPath}", "NPC Links");
                break;
            default:
                ChatGui.Print("Dictionary usage: /npclinks dict set <term> | <definition> | <alias1, alias2>; /npclinks dict delete <term>; /npclinks dict reload; /npclinks dict path", "NPC Links");
                break;
        }
    }

    private void HandleDictionarySetCommand(string arguments)
    {
        var parts = arguments.Split('|', 3, StringSplitOptions.TrimEntries);
        if (parts.Length < 2 || string.IsNullOrWhiteSpace(parts[0]) || string.IsNullOrWhiteSpace(parts[1]))
        {
            ChatGui.Print("Usage: /npclinks dict set <term> | <definition> | <optional alias1, alias2>", "NPC Links");
            return;
        }

        var aliases = parts.Length > 2 ? ParseAliasList(parts[2]) : Array.Empty<string>();
        var result = this.termDictionary.AddOrUpdateUserEntry(parts[0], parts[1], aliases);
        this.PrintDictionaryMutationResult(result);
        if (result.Succeeded)
        {
            this.RefreshLastCandidates();
        }
    }

    private void HandleDictionaryDeleteCommand(string arguments)
    {
        if (string.IsNullOrWhiteSpace(arguments))
        {
            ChatGui.Print("Usage: /npclinks dict delete <term>", "NPC Links");
            return;
        }

        var result = this.termDictionary.DeleteUserEntry(arguments);
        this.PrintDictionaryMutationResult(result);
        if (result.Succeeded)
        {
            this.RefreshLastCandidates();
        }
    }

    private void PrintDictionaryMutationResult(DictionaryMutationResult result)
    {
        ChatGui.Print(result.Message, "NPC Links");
    }

    private DictionaryMutationResult SaveDictionaryProposal(DictionaryProposal proposal)
    {
        var result = this.termDictionary.AddOrUpdateUserEntry(
            proposal.CanonicalName,
            proposal.Definition,
            proposal.Aliases);
        this.PrintDictionaryMutationResult(result);
        if (result.Succeeded)
        {
            this.RefreshLastCandidates();
        }

        return result;
    }

    private void HandleQuestProbeCommand(string arguments)
    {
        var trimmed = arguments.Trim();
        if (string.IsNullOrWhiteSpace(trimmed))
        {
            this.PrintQuestProbeStatus();
            return;
        }

        var parts = trimmed.Split(' ', 2, StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries);
        var action = parts[0].ToLowerInvariant();
        var rest = parts.Length > 1 ? parts[1] : string.Empty;

        switch (action)
        {
            case "on":
            case "enable":
                this.questMetadataProbe.SetEnabled(true);
                ChatGui.Print($"Quest probe enabled. Output: {this.questMetadataProbe.OutputDirectory}", "NPC Links");
                ChatGui.Print("Talk to quest NPCs, then use /npclinks questprobe capture <verified quest name> when you know the quest.", "NPC Links");
                break;
            case "off":
            case "disable":
                this.questMetadataProbe.SetEnabled(false);
                ChatGui.Print("Quest probe disabled.", "NPC Links");
                break;
            case "capture":
            case "mark":
                this.PrintQuestProbeWriteResult(this.CaptureQuestProbe("manual-capture", rest));
                break;
            case "path":
                ChatGui.Print($"Quest probe output: {this.questMetadataProbe.OutputDirectory}", "NPC Links");
                break;
            case "status":
                this.PrintQuestProbeStatus();
                break;
            default:
                ChatGui.Print("Quest probe usage: /npclinks questprobe on|off|status|path|capture <verified quest name>", "NPC Links");
                break;
        }
    }

    private void PrintQuestProbeStatus()
    {
        var state = this.questMetadataProbe.Enabled ? "enabled" : "disabled";
        ChatGui.Print($"Quest probe is {state}. Output: {this.questMetadataProbe.OutputDirectory}", "NPC Links");
        ChatGui.Print("Usage: /npclinks questprobe on, then /npclinks questprobe capture <verified quest name> after a captured Talk line.", "NPC Links");
    }

    private QuestProbeWriteResult CaptureQuestProbe(string source, string userVerifiedQuestName)
    {
        var context = this.gameContextProvider.Capture();
        var knownTerms = string.IsNullOrWhiteSpace(this.lastDialogue)
            ? Array.Empty<string>()
            : LinkCandidateExtractor.Extract(this.lastDialogue, this.termDictionary.MatchTerms);

        return this.questMetadataProbe.CaptureDialogue(
            source,
            this.lastDialogue,
            userVerifiedQuestName,
            context,
            knownTerms);
    }

    private void PrintQuestProbeWriteResult(QuestProbeWriteResult result)
    {
        ChatGui.Print(result.Message, "NPC Links");
    }

    private void HandleLoreExplain(string dialogueArgument)
    {
        var (dialogue, question) = ParseLoreExplainArgument(dialogueArgument);
        var hasExplicitDialogue = !string.IsNullOrWhiteSpace(dialogue);
        var source = "manual-command";

        if (!hasExplicitDialogue)
        {
            dialogue = this.lastDialogue;
            source = "last-captured-dialogue";
        }

        if (string.IsNullOrWhiteSpace(dialogue))
        {
            ChatGui.Print("No dialogue provided. Use /npclinks explain <dialogue> | <question> or capture a Talk line first.", "NPC Links");
            return;
        }

        var candidates = LinkCandidateExtractor.Extract(dialogue, this.termDictionary.MatchTerms);
        var metadata = hasExplicitDialogue ? LoreContextMetadata.Empty : this.gameContextProvider.Capture();
        var dialogueHistory = hasExplicitDialogue
            ? Array.Empty<string>()
            : this.dialogueHistory.GetPreviousLines(dialogue);
        var request = new LoreExplainRequest(
            dialogue,
            question,
            candidates,
            metadata,
            dialogueHistory);

        if (this.configuration.EnableOnlineExplain && !string.IsNullOrWhiteSpace(this.configuration.OpenAiApiKey))
        {
            this.StartOnlineLoreExplain(request);
            return;
        }

        if (this.configuration.EnableOnlineExplain)
        {
            ChatGui.Print("Live Lore Explain is enabled, but no OpenAI API key is configured. Open /npclinks config.", "NPC Links");
        }

        this.ExportLoreExplainRequest(source, request);
    }

    private void StartOnlineLoreExplain(LoreExplainRequest request)
    {
        this.loreExplainCancellationTokenSource?.Cancel();
        this.loreExplainCancellationTokenSource?.Dispose();
        this.loreExplainCancellationTokenSource = new CancellationTokenSource();
        var cancellationToken = this.loreExplainCancellationTokenSource.Token;

        this.loreExplainWindow.ShowLoading(request);
        this.lastLoreExplainRequest = request;
        ChatGui.Print("Lore Explain request sent.", "NPC Links");

        _ = Task.Run(async () =>
        {
            try
            {
                var result = await this.loreExplainClient.ExplainAsync(this.configuration, request, cancellationToken).ConfigureAwait(false);
                if (!cancellationToken.IsCancellationRequested)
                {
                    this.loreExplainWindow.ShowResult(result);
                    this.lastLoreExplainResult = result;
                    ChatGui.Print("Lore Explain response received.", "NPC Links");
                }
            }
            catch (OperationCanceledException)
            {
            }
            catch (Exception exception)
            {
                Log.Warning(exception, "Failed to complete online Lore Explain request.");
                this.loreExplainWindow.ShowError(exception.Message);
                ChatGui.Print("Lore Explain failed.", "NPC Links");
            }
        }, cancellationToken);
    }

    private void HandleLoreExplainFollowUp(string followUpQuestion)
    {
        if (string.IsNullOrWhiteSpace(followUpQuestion))
        {
            return;
        }

        if (!this.configuration.EnableOnlineExplain || string.IsNullOrWhiteSpace(this.configuration.OpenAiApiKey))
        {
            ChatGui.Print("Follow-up questions need live Lore Explain. Open /npclinks config.", "NPC Links");
            return;
        }

        if (this.lastLoreExplainRequest is null || string.IsNullOrWhiteSpace(this.lastLoreExplainRequest.Dialogue))
        {
            ChatGui.Print("No Lore Explain result to follow up on yet.", "NPC Links");
            return;
        }

        var previousQuestion = string.IsNullOrWhiteSpace(this.lastLoreExplainRequest.FollowUpQuestion)
            ? this.lastLoreExplainRequest.Question
            : this.lastLoreExplainRequest.FollowUpQuestion;
        var request = this.lastLoreExplainRequest with
        {
            Question = previousQuestion,
            PreviousAnswer = this.lastLoreExplainResult?.Text ?? string.Empty,
            FollowUpQuestion = followUpQuestion.Trim(),
            ConversationTranscript = this.loreExplainWindow.BuildTranscript(),
        };

        this.StartOnlineLoreExplain(request, followUpQuestion.Trim());
    }

    private void StartOnlineLoreExplain(LoreExplainRequest request, string followUpQuestion)
    {
        this.loreExplainCancellationTokenSource?.Cancel();
        this.loreExplainCancellationTokenSource?.Dispose();
        this.loreExplainCancellationTokenSource = new CancellationTokenSource();
        var cancellationToken = this.loreExplainCancellationTokenSource.Token;

        this.loreExplainWindow.ShowFollowUpLoading(followUpQuestion);
        this.lastLoreExplainRequest = request;
        ChatGui.Print("Lore Explain follow-up sent.", "NPC Links");

        _ = Task.Run(async () =>
        {
            try
            {
                var result = await this.loreExplainClient.ExplainAsync(this.configuration, request, cancellationToken).ConfigureAwait(false);
                if (!cancellationToken.IsCancellationRequested)
                {
                    this.loreExplainWindow.ShowFollowUpResult(followUpQuestion, result);
                    this.lastLoreExplainResult = result;
                    ChatGui.Print("Lore Explain follow-up received.", "NPC Links");
                }
            }
            catch (OperationCanceledException)
            {
            }
            catch (Exception exception)
            {
                Log.Warning(exception, "Failed to complete online Lore Explain follow-up.");
                this.loreExplainWindow.ShowError(exception.Message);
                ChatGui.Print("Lore Explain follow-up failed.", "NPC Links");
            }
        }, cancellationToken);
    }

    private void ExportLoreExplainRequest(string source, LoreExplainRequest request)
    {
        var dialogue = request.Dialogue;
        var question = request.Question;

        try
        {
            var requestDirectory = Path.Combine(PluginInterface.ConfigDirectory.FullName, "lore-explain-requests");
            Directory.CreateDirectory(requestDirectory);

            var timestamp = DateTimeOffset.Now;
            var requestPath = Path.Combine(requestDirectory, $"request-{timestamp:yyyyMMdd-HHmmss}.json");
            var exportPayload = new
            {
                source,
                createdAt = timestamp,
                dialogue,
                question,
                knownTerms = request.KnownTerms,
                output = new
                {
                    explanation = true,
                    citations = true,
                    dictionaryProposals = true,
                },
            };

            var options = new JsonSerializerOptions
            {
                WriteIndented = true,
            };

            File.WriteAllText(requestPath, JsonSerializer.Serialize(exportPayload, options));
            ChatGui.Print($"Lore Explain request exported: {requestPath}", "NPC Links");
            if (!string.IsNullOrWhiteSpace(question))
            {
                ChatGui.Print($"Question: {question}", "NPC Links");
            }

            ChatGui.Print("Run the companion helper from the repo to turn it into an explanation.", "NPC Links");
        }
        catch (Exception exception)
        {
            Log.Warning(exception, "Failed to export Lore Explain request.");
            ChatGui.Print("Failed to export Lore Explain request. Check the plugin log for details.", "NPC Links");
        }
    }

    private static (string Dialogue, string Question) ParseLoreExplainArgument(string argument)
    {
        var trimmed = argument.Trim();
        var separatorIndex = trimmed.IndexOf('|');
        if (separatorIndex < 0)
        {
            return (trimmed, string.Empty);
        }

        var dialogue = trimmed[..separatorIndex].Trim();
        var question = trimmed[(separatorIndex + 1)..].Trim();
        return (dialogue, question);
    }

    private static IReadOnlyList<string> ParseAliasList(string aliases)
        => aliases
            .Split([',', ';'], StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
            .Where(alias => !string.IsNullOrWhiteSpace(alias))
            .ToArray();

    private void RefreshLastCandidates()
    {
        if (string.IsNullOrWhiteSpace(this.lastDialogue))
        {
            this.lastCandidates = Array.Empty<string>();
            return;
        }

        this.lastCandidates = LinkCandidateExtractor.Extract(this.lastDialogue, this.termDictionary.MatchTerms);
    }

    private void PrintStatus()
    {
        if (string.IsNullOrWhiteSpace(this.lastDialogue))
        {
            ChatGui.Print("No Talk dialogue captured yet. Start an NPC conversation and try again.", "NPC Links");
            return;
        }

        ChatGui.Print($"Last dialogue: {this.lastDialogue}", "NPC Links");

        if (this.lastCandidates.Count == 0)
        {
            ChatGui.Print("No candidate phrases were extracted from the last dialogue line.", "NPC Links");
            return;
        }

        ChatGui.Print(this.BuildCandidateMessage(this.lastCandidates), "NPC Links");
    }

    private void PrintTriggerList()
    {
        var knownTerms = this.termDictionary.MatchTerms.OrderBy(value => value).ToArray();
        if (knownTerms.Length == 0)
        {
            ChatGui.Print("No dictionary terms configured.", "NPC Links");
            return;
        }

        ChatGui.Print($"Dictionary terms: {string.Join(", ", knownTerms)}", "NPC Links");
    }

    private void DrawUi()
    {
        this.windowSystem.Draw();
    }
}
