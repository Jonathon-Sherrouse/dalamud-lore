using System.Numerics;
using System.Diagnostics;
using Dalamud.Bindings.ImGui;
using Dalamud.Interface.Windowing;

namespace NpcDialogueLinks;

internal sealed class LoreExplainWindow : Window
{
    private static readonly Vector4 UserColor = new(0.73f, 0.48f, 1.0f, 1.0f);
    private static readonly Vector4 LoreExplainColor = new(1.0f, 0.35f, 0.35f, 1.0f);
    private static readonly Vector4 LinkColor = new(0.35f, 0.68f, 1.0f, 1.0f);
    private static readonly Vector4 ChipColor = new(0.25f, 0.5f, 0.55f, 1.0f);
    private static readonly Vector4 MutedTextColor = new(0.68f, 0.68f, 0.68f, 1.0f);
    private static readonly Vector4 SuccessColor = new(0.45f, 0.9f, 0.62f, 1.0f);
    private static readonly Vector4 PendingColor = new(1.0f, 0.76f, 0.35f, 1.0f);
    private static readonly Vector4 ErrorColor = new(1.0f, 0.42f, 0.42f, 1.0f);
    private readonly Action<string> onFollowUpRequested;
    private readonly Func<DictionaryProposal, DictionaryMutationResult> onDictionaryProposalSave;
    private string dialogue = string.Empty;
    private string question = string.Empty;
    private LoreContextMetadata metadata = LoreContextMetadata.Empty;
    private IReadOnlyList<string> dialogueHistory = Array.Empty<string>();
    private string followUpQuestion = string.Empty;
    private string status = "No explanation requested yet.";
    private string result = string.Empty;
    private IReadOnlyList<LoreExplainSource> sources = Array.Empty<LoreExplainSource>();
    private readonly List<LoreExplainTurn> turns = [];
    private readonly List<DictionaryProposalDraft> dictionaryProposalDrafts = [];
    private string dictionaryProposalStatus = string.Empty;
    private bool isLoading;

    public LoreExplainWindow(
        Action<string> onFollowUpRequested,
        Func<DictionaryProposal, DictionaryMutationResult> onDictionaryProposalSave)
        : base("Lore Explain###NpcDialogueLinksLoreExplain")
    {
        this.onFollowUpRequested = onFollowUpRequested;
        this.onDictionaryProposalSave = onDictionaryProposalSave;
        this.Size = new Vector2(760, 560);
        this.SizeCondition = ImGuiCond.FirstUseEver;
        this.SizeConstraints = new()
        {
            MinimumSize = new Vector2(560, 380),
            MaximumSize = new Vector2(1400, 1100),
        };
        this.ShowCloseButton = true;
        this.RespectCloseHotkey = true;
    }

    public void ShowLoading(LoreExplainRequest request)
    {
        this.dialogue = request.Dialogue;
        this.question = request.Question;
        this.metadata = request.Metadata;
        this.dialogueHistory = request.DialogueHistory;
        this.status = "Asking OpenAI...";
        this.result = string.Empty;
        this.followUpQuestion = string.Empty;
        this.sources = Array.Empty<LoreExplainSource>();
        this.turns.Clear();
        this.dictionaryProposalDrafts.Clear();
        this.dictionaryProposalStatus = string.Empty;
        this.isLoading = true;
        this.IsOpen = true;
    }

    public void ShowResult(LoreExplainResult explanation)
    {
        this.status = "Complete";
        this.result = explanation.Text;
        this.sources = explanation.Sources;
        this.SetDictionaryProposalDrafts(explanation.DictionaryProposals);
        this.turns.Add(new LoreExplainTurn(
            string.IsNullOrWhiteSpace(this.question) ? "Explain this dialogue." : this.question,
            explanation.Text));
        this.isLoading = false;
        this.IsOpen = true;
    }

    public void ShowFollowUpLoading(string followUp)
    {
        this.question = followUp;
        this.status = "Asking follow-up...";
        this.result = string.Empty;
        this.sources = Array.Empty<LoreExplainSource>();
        this.dictionaryProposalDrafts.Clear();
        this.dictionaryProposalStatus = string.Empty;
        this.isLoading = true;
        this.IsOpen = true;
    }

    public void ShowFollowUpResult(string followUp, LoreExplainResult explanation)
    {
        this.status = "Complete";
        this.result = explanation.Text;
        this.sources = explanation.Sources;
        this.SetDictionaryProposalDrafts(explanation.DictionaryProposals);
        this.turns.Add(new LoreExplainTurn(followUp, explanation.Text));
        this.isLoading = false;
        this.IsOpen = true;
    }

    public void ShowError(string message)
    {
        this.status = "Error";
        this.result = message;
        this.sources = Array.Empty<LoreExplainSource>();
        this.dictionaryProposalDrafts.Clear();
        this.dictionaryProposalStatus = string.Empty;
        this.isLoading = false;
        this.IsOpen = true;
    }

    public override void Draw()
    {
        this.DrawStatusHeader();
        ImGui.Separator();

        if (!string.IsNullOrWhiteSpace(this.question))
        {
            DrawSectionLabel("Question");
            ImGui.TextWrapped(this.question);
            ImGui.Spacing();
        }

        DrawSectionLabel("Dialogue");
        using (var child = new ChildRegion("NpcDialogueLinksLoreDialogue", new Vector2(0, 96), true))
        {
            ImGui.TextWrapped(string.IsNullOrWhiteSpace(this.dialogue) ? "(none)" : this.dialogue);
        }

        if (this.metadata.HasAnyContext)
        {
            ImGui.Spacing();
            if (ImGui.CollapsingHeader("Context"))
            {
                this.DrawContextChips();
            }
        }

        if (this.dialogueHistory.Count > 0)
        {
            ImGui.Spacing();
            if (ImGui.CollapsingHeader("Recent Context"))
            {
                using (var child = new ChildRegion("NpcDialogueLinksRecentContext", new Vector2(0, 72), true))
                {
                    foreach (var line in this.dialogueHistory.TakeLast(4))
                    {
                        ImGui.BulletText(line);
                    }
                }
            }
        }

        ImGui.Spacing();
        DrawSectionLabel("Conversation");
        var lowerPanelHeight = this.sources.Count > 0 || this.dictionaryProposalDrafts.Count > 0 ? -250 : -54;
        using (var child = new ChildRegion("NpcDialogueLinksLoreResult", new Vector2(0, lowerPanelHeight), true))
        {
            if (this.turns.Count == 0)
            {
                ImGui.TextWrapped(string.IsNullOrWhiteSpace(this.result) ? "Waiting for response..." : this.result);
            }
            else
            {
                foreach (var turn in this.turns)
                {
                    DrawConversationTurn(turn);
                    ImGui.Separator();
                }

                if (this.isLoading)
                {
                    DrawSpeakerBlock("You", this.question, UserColor);
                    ImGui.Spacing();
                    DrawSpeakerBlock("Lore Explain", "Waiting for response...", PendingColor);
                }
            }
        }

        if (this.dictionaryProposalDrafts.Count > 0)
        {
            ImGui.Spacing();
            if (ImGui.CollapsingHeader("Dictionary Proposals"))
            {
                this.DrawDictionaryProposals();
            }
        }

        if (this.sources.Count > 0)
        {
            ImGui.Spacing();
            if (ImGui.CollapsingHeader($"Sources ({this.sources.Count})"))
            {
                using (var child = new ChildRegion("NpcDialogueLinksLoreSources", new Vector2(0, 90), true))
                {
                    for (var index = 0; index < this.sources.Count; index++)
                    {
                        if (index > 0)
                        {
                            ImGui.Separator();
                        }

                        DrawSourceRow(this.sources[index]);
                    }
                }
            }
        }

        ImGui.Spacing();
        DrawSectionLabel("Follow-up");
        ImGui.SetNextItemWidth(-92);
        ImGui.InputTextWithHint("##NpcDialogueLinksFollowUp", "Ask a follow-up...", ref this.followUpQuestion, 512);
        ImGui.SameLine();
        var canAsk = !this.isLoading && !string.IsNullOrWhiteSpace(this.dialogue) && !string.IsNullOrWhiteSpace(this.followUpQuestion);
        if (!canAsk)
        {
            ImGui.BeginDisabled();
        }

        if (ImGui.Button("Ask", new Vector2(80, 0)))
        {
            var followUp = this.followUpQuestion.Trim();
            this.followUpQuestion = string.Empty;
            this.onFollowUpRequested(followUp);
        }

        if (!canAsk)
        {
            ImGui.EndDisabled();
        }
    }

    public string BuildTranscript()
    {
        if (this.turns.Count == 0)
        {
            return string.Empty;
        }

        return string.Join(
            "\n\n",
            this.turns.Select(turn => $"User: {turn.Question}\nAssistant: {turn.Answer}"));
    }

    private void SetDictionaryProposalDrafts(IReadOnlyList<DictionaryProposal> proposals)
    {
        this.dictionaryProposalDrafts.Clear();
        foreach (var proposal in proposals)
        {
            this.dictionaryProposalDrafts.Add(new DictionaryProposalDraft(proposal));
        }

        this.dictionaryProposalStatus = string.Empty;
    }

    private void DrawDictionaryProposals()
    {
        if (!string.IsNullOrWhiteSpace(this.dictionaryProposalStatus))
        {
            ImGui.TextWrapped(this.dictionaryProposalStatus);
        }

        var savedIndex = -1;
        for (var index = 0; index < this.dictionaryProposalDrafts.Count; index++)
        {
            var draft = this.dictionaryProposalDrafts[index];
            ImGui.Separator();
            ImGui.TextUnformatted("Term");
            ImGui.SetNextItemWidth(-1);
            ImGui.InputTextWithHint($"##NpcDialogueLinksProposalTerm{index}", "Term", ref draft.CanonicalName, 160);

            ImGui.TextUnformatted("Definition");
            ImGui.SetNextItemWidth(-1);
            ImGui.InputTextMultiline($"##NpcDialogueLinksProposalDefinition{index}", ref draft.Definition, 1024, new Vector2(-1, 72));

            ImGui.TextUnformatted("Aliases");
            ImGui.SetNextItemWidth(-1);
            ImGui.InputTextMultiline($"##NpcDialogueLinksProposalAliases{index}", ref draft.Aliases, 512, new Vector2(-1, 48));

            if (draft.Sources.Count > 0)
            {
                ImGui.TextWrapped($"Sources: {string.Join(", ", draft.Sources.Take(3))}");
            }

            if (ImGui.Button($"Save to Dictionary##NpcDialogueLinksSaveProposal{index}"))
            {
                var result = this.onDictionaryProposalSave(draft.ToProposal());
                this.dictionaryProposalStatus = result.Message;
                if (result.Succeeded)
                {
                    savedIndex = index;
                }
            }
        }

        if (savedIndex >= 0)
        {
            this.dictionaryProposalDrafts.RemoveAt(savedIndex);
        }
    }

    private void DrawStatusHeader()
    {
        ImGui.TextUnformatted("Status");
        ImGui.SameLine();
        ImGui.TextColored(this.GetStatusColor(), this.isLoading ? $"{this.status}..." : this.status);
    }

    private Vector4 GetStatusColor()
    {
        if (this.isLoading)
        {
            return PendingColor;
        }

        if (string.Equals(this.status, "Complete", StringComparison.OrdinalIgnoreCase))
        {
            return SuccessColor;
        }

        return string.Equals(this.status, "Error", StringComparison.OrdinalIgnoreCase)
            ? ErrorColor
            : MutedTextColor;
    }

    private static void DrawConversationTurn(LoreExplainTurn turn)
    {
        DrawSpeakerBlock("You", turn.Question, UserColor);
        ImGui.Spacing();
        DrawSpeakerBlock("Lore Explain", turn.Answer, LoreExplainColor);
    }

    private static void DrawSpeakerBlock(string speaker, string turnText, Vector4 speakerColor)
    {
        ImGui.TextColored(speakerColor, speaker);
        ImGui.Indent(14f);
        ImGui.TextWrapped(turnText);
        ImGui.Unindent(14f);
    }

    private string BuildMetadataSummary()
    {
        var parts = new List<string>();
        if (!string.IsNullOrWhiteSpace(this.metadata.ZoneName))
        {
            parts.Add($"Zone: {this.metadata.ZoneName}");
        }

        if (!string.IsNullOrWhiteSpace(this.metadata.SpeakerName))
        {
            parts.Add($"Possible speaker: {this.metadata.SpeakerName}");
        }

        if (!string.IsNullOrWhiteSpace(this.metadata.TargetName) &&
            !string.Equals(this.metadata.TargetName, this.metadata.SpeakerName, StringComparison.Ordinal))
        {
            parts.Add($"Target: {this.metadata.TargetName}");
        }

        if (this.metadata.HasVerifiedQuestContext && !string.IsNullOrWhiteSpace(this.metadata.QuestName))
        {
            parts.Add($"Quest: {this.metadata.QuestName}");
        }

        return string.Join(" | ", parts);
    }

    private void DrawContextChips()
    {
        var chips = this.BuildContextChips();
        for (var index = 0; index < chips.Count; index++)
        {
            if (index > 0)
            {
                ImGui.SameLine();
            }

            ImGui.TextColored(ChipColor, chips[index]);
        }
    }

    private IReadOnlyList<string> BuildContextChips()
    {
        var chips = new List<string>();
        if (!string.IsNullOrWhiteSpace(this.metadata.ZoneName))
        {
            chips.Add($"Zone: {this.metadata.ZoneName}");
        }

        if (!string.IsNullOrWhiteSpace(this.metadata.SpeakerName))
        {
            chips.Add($"Speaker: {this.metadata.SpeakerName}");
        }

        if (!string.IsNullOrWhiteSpace(this.metadata.TargetName) &&
            !string.Equals(this.metadata.TargetName, this.metadata.SpeakerName, StringComparison.Ordinal))
        {
            chips.Add($"Target: {this.metadata.TargetName}");
        }

        if (this.metadata.HasVerifiedQuestContext && !string.IsNullOrWhiteSpace(this.metadata.QuestName))
        {
            chips.Add($"Quest: {this.metadata.QuestName}");
        }

        return chips;
    }

    private static void OpenSourceUrl(string url)
    {
        if (!Uri.TryCreate(url, UriKind.Absolute, out var uri) ||
            (uri.Scheme != Uri.UriSchemeHttp && uri.Scheme != Uri.UriSchemeHttps))
        {
            return;
        }

        Process.Start(new ProcessStartInfo(uri.ToString())
        {
            UseShellExecute = true,
        });
    }

    private static void DrawSourceLink(LoreExplainSource source)
    {
        var label = $"{source.Title}##{source.Url}";
        ImGui.TextColored(LinkColor, source.Title);
        var itemMin = ImGui.GetItemRectMin();
        var itemMax = ImGui.GetItemRectMax();
        ImGui.GetWindowDrawList().AddLine(
            new Vector2(itemMin.X, itemMax.Y),
            new Vector2(itemMax.X, itemMax.Y),
            ImGui.GetColorU32(LinkColor),
            1f);

        ImGui.SetCursorScreenPos(itemMin);
        if (ImGui.InvisibleButton(label, itemMax - itemMin))
        {
            OpenSourceUrl(source.Url);
        }

        if (ImGui.IsItemHovered())
        {
            ImGui.SetMouseCursor(ImGuiMouseCursor.Hand);
            ImGui.SetTooltip($"Open source\n{source.Url}");
        }
    }

    private static void DrawSourceRow(LoreExplainSource source)
    {
        DrawSourceLink(source);
        ImGui.Indent(14f);
        TextMuted(source.Url);
        ImGui.Unindent(14f);
    }

    private static void DrawSectionLabel(string label)
    {
        ImGui.TextUnformatted(label);
    }

    private static void TextMuted(string text)
    {
        ImGui.TextColored(MutedTextColor, text);
    }

    private static IReadOnlyList<string> ParseAliases(string aliases)
        => aliases
            .Split(['\r', '\n', ',', ';'], StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
            .Where(alias => !string.IsNullOrWhiteSpace(alias))
            .ToArray();

    private readonly ref struct ChildRegion
    {
        public ChildRegion(string id, Vector2 size, bool border)
        {
            ImGui.BeginChild(id, size, border);
        }

        public void Dispose()
        {
            ImGui.EndChild();
        }
    }
}

internal sealed class DictionaryProposalDraft
{
    public DictionaryProposalDraft(DictionaryProposal proposal)
    {
        this.CanonicalName = proposal.CanonicalName;
        this.Definition = proposal.Definition;
        this.Aliases = string.Join(Environment.NewLine, proposal.Aliases);
        this.Sources = proposal.Sources;
    }

    public string CanonicalName;

    public string Definition;

    public string Aliases;

    public IReadOnlyList<string> Sources { get; }

    public DictionaryProposal ToProposal()
        => new(this.CanonicalName, this.Definition, ParseAliases(this.Aliases), this.Sources);

    private static IReadOnlyList<string> ParseAliases(string aliases)
        => aliases
            .Split(['\r', '\n', ',', ';'], StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
            .Where(alias => !string.IsNullOrWhiteSpace(alias))
            .ToArray();
}

internal sealed record LoreExplainTurn(string Question, string Answer);
