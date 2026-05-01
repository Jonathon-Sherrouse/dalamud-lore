using Dalamud.Game.Addon.Lifecycle;
using Dalamud.Game.Command;
using Dalamud.Game.Text.SeStringHandling;
using Dalamud.Game.Text.SeStringHandling.Payloads;
using Dalamud.IoC;
using Dalamud.Plugin;
using Dalamud.Plugin.Services;

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
    internal static IChatGui ChatGui { get; private set; } = null!;

    [PluginService]
    internal static IPluginLog Log { get; private set; } = null!;

    private readonly DialogueCapture dialogueCapture;
    private readonly DalamudLinkPayload linkPayload;
    private readonly TermDictionary termDictionary;

    private string lastDialogue = string.Empty;
    private IReadOnlyList<string> lastCandidates = Array.Empty<string>();

    public Plugin()
    {
        var pluginDirectory = PluginInterface.AssemblyLocation.DirectoryName;
        if (string.IsNullOrWhiteSpace(pluginDirectory))
        {
            pluginDirectory = AppContext.BaseDirectory;
        }

        this.termDictionary = new TermDictionary(Path.Combine(pluginDirectory, "terms.json"));
        this.linkPayload = ChatGui.AddChatLinkHandler(LinkCommandId, this.OnLinkClicked);
        this.dialogueCapture = new DialogueCapture(AddonLifecycle, this.OnDialogueChanged);

        CommandManager.AddHandler(
            CommandName,
            new CommandInfo(this.OnCommand)
            {
                HelpMessage = "Show the latest NPC dialogue POC state and dictionary-backed matches.",
            });

        Log.Information("NPC Dialogue Links loaded.");
    }

    public void Dispose()
    {
        this.dialogueCapture.Dispose();
        CommandManager.RemoveHandler(CommandName);
        ChatGui.RemoveChatLinkHandler(LinkCommandId);
    }

    private void OnDialogueChanged(string dialogue)
    {
        this.lastDialogue = dialogue;
        this.lastCandidates = LinkCandidateExtractor.Extract(dialogue, this.termDictionary.Terms);

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

        if (this.termDictionary.TryGetDefinition(clickedText, out var definition))
        {
            ChatGui.Print($"{clickedText}: {definition}", "NPC Links");
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

        switch (trimmed.ToLowerInvariant())
        {
            case "list":
                this.PrintTriggerList();
                break;
            case "show":
                this.PrintStatus();
                break;
            default:
                ChatGui.Print("Usage: /npclinks [show|list]", "NPC Links");
                break;
        }
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
        var knownTerms = this.termDictionary.Terms.OrderBy(value => value).ToArray();
        if (knownTerms.Length == 0)
        {
            ChatGui.Print("No dictionary terms configured.", "NPC Links");
            return;
        }

        ChatGui.Print($"Dictionary terms: {string.Join(", ", knownTerms)}", "NPC Links");
    }
}
