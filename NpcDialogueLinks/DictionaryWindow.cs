using System.Numerics;
using Dalamud.Bindings.ImGui;
using Dalamud.Interface.Windowing;

namespace NpcDialogueLinks;

internal sealed class DictionaryWindow : Window
{
    private static readonly Vector4 AccentColor = new(0.45f, 0.72f, 1.0f, 1.0f);
    private static readonly Vector4 MutedTextColor = new(0.68f, 0.68f, 0.68f, 1.0f);
    private static readonly Vector4 SuccessColor = new(0.45f, 0.9f, 0.62f, 1.0f);
    private static readonly Vector4 WarningColor = new(1.0f, 0.76f, 0.35f, 1.0f);

    private readonly TermDictionary termDictionary;
    private readonly Action onDictionaryChanged;
    private string searchText = string.Empty;
    private string? selectedTerm;
    private string editTermName = string.Empty;
    private string editDefinition = string.Empty;
    private string editAliases = string.Empty;
    private string statusMessage = string.Empty;
    private DictionaryWindowStatusKind statusKind = DictionaryWindowStatusKind.Info;
    private string? pendingDeleteTerm;
    private bool isEditing;
    private bool isCreatingNewEntry;

    public DictionaryWindow(TermDictionary termDictionary, Action onDictionaryChanged)
        : base("NPC Dictionary###NpcDialogueLinksDictionary")
    {
        this.termDictionary = termDictionary;
        this.onDictionaryChanged = onDictionaryChanged;
        this.Size = new Vector2(860, 520);
        this.SizeCondition = ImGuiCond.FirstUseEver;
        this.SizeConstraints = new()
        {
            MinimumSize = new Vector2(640, 360),
            MaximumSize = new Vector2(1600, 1200),
        };
        this.ShowCloseButton = true;
        this.RespectCloseHotkey = true;
    }

    public override void Draw()
    {
        ImGui.TextUnformatted("Dictionary");
        ImGui.SameLine();
        TextMuted($"{this.termDictionary.Count} terms");
        ImGui.Spacing();

        ImGui.SetNextItemWidth(-196);
        ImGui.InputTextWithHint("##NpcDictionarySearch", "Search terms...", ref this.searchText, 128);
        ImGui.SameLine();
        if (ImGui.Button("New", new Vector2(88, 0)))
        {
            this.StartNewEntry();
        }

        ImGui.SameLine();
        if (ImGui.Button("Reload", new Vector2(88, 0)))
        {
            var result = this.termDictionary.Reload();
            this.SetStatus(result.Message, DictionaryWindowStatusKind.Success);
            this.pendingDeleteTerm = null;
            this.onDictionaryChanged();
        }

        if (!string.IsNullOrWhiteSpace(this.statusMessage))
        {
            ImGui.TextColored(this.GetStatusColor(), this.statusMessage);
        }

        ImGui.Spacing();

        var rows = this.GetFilteredRows();
        this.selectedTerm = EnsureSelection(rows, this.selectedTerm);

        var selectedRow = string.IsNullOrWhiteSpace(this.selectedTerm)
            ? null
            : rows.FirstOrDefault(row => string.Equals(row.Term, this.selectedTerm, StringComparison.Ordinal));

        var availableHeight = ImGui.GetContentRegionAvail().Y;
        if (!ImGui.BeginTable("NpcDictionaryLayout", 2, ImGuiTableFlags.BordersInnerV | ImGuiTableFlags.Resizable | ImGuiTableFlags.RowBg))
        {
            return;
        }

        ImGui.TableSetupColumn("Terms", ImGuiTableColumnFlags.WidthFixed, 280f);
        ImGui.TableSetupColumn("Details", ImGuiTableColumnFlags.WidthStretch);
        ImGui.TableHeadersRow();
        ImGui.TableNextRow();

        ImGui.TableSetColumnIndex(0);
        using (var leftChild = new ChildRegion("NpcDictionaryTerms", new Vector2(0, availableHeight), false))
        {
            if (rows.Count == 0)
            {
                TextMuted("No matching dictionary terms.");
            }

            foreach (var row in rows)
            {
                var isSelected = string.Equals(this.selectedTerm, row.Term, StringComparison.Ordinal);
                if (ImGui.Selectable(FormatRowLabel(row), isSelected))
                {
                    this.selectedTerm = row.Term;
                    this.pendingDeleteTerm = null;
                    if (this.isEditing)
                    {
                        this.StartEditEntry(row.Term);
                    }
                }
            }
        }

        ImGui.TableSetColumnIndex(1);
        using (var rightChild = new ChildRegion("NpcDictionaryDefinition", new Vector2(0, availableHeight), false))
        {
            if (this.isEditing)
            {
                this.DrawEditor();
            }
            else
            {
                this.DrawSelectedTerm(selectedRow);
            }
        }

        ImGui.EndTable();
    }

    private void DrawSelectedTerm(TermListRow? selectedRow)
    {
        if (selectedRow is null)
        {
            ImGui.TextColored(AccentColor, "No term selected");
            TextMuted("Choose a term from the list, or create a new one.");
            ImGui.Spacing();
            if (ImGui.Button("Create Term"))
            {
                this.StartNewEntry();
            }

            return;
        }

        ImGui.TextColored(AccentColor, selectedRow.CanonicalName);
        if (selectedRow.IsAlias)
        {
            TextMuted($"Selected alias: {selectedRow.Term}");
        }

        TextMuted($"Source: {FormatSourceLabel(selectedRow)}");
        ImGui.Separator();

        ImGui.TextUnformatted("Definition");
        ImGui.TextWrapped(selectedRow.Definition);

        if (this.termDictionary.TryGetEditableEntry(selectedRow.CanonicalName, out var editableEntry) &&
            editableEntry.Aliases.Count > 0)
        {
            ImGui.Spacing();
            ImGui.TextUnformatted("Aliases");
            TextMuted(string.Join(", ", editableEntry.Aliases));
        }

        ImGui.Spacing();

        if (ImGui.Button("Edit Term", new Vector2(104, 0)))
        {
            this.StartEditEntry(selectedRow.Term);
        }

        ImGui.SameLine();
        this.DrawDeleteButton(selectedRow);
    }

    private void DrawDeleteButton(TermListRow selectedRow)
    {
        var canonicalName = selectedRow.CanonicalName;
        var actionLabel = GetDeleteActionLabel(selectedRow);
        var confirmLabel = actionLabel.StartsWith("Hide", StringComparison.Ordinal)
            ? "Confirm Hide"
            : "Confirm Delete";

        if (string.Equals(this.pendingDeleteTerm, canonicalName, StringComparison.OrdinalIgnoreCase))
        {
            if (ImGui.Button(confirmLabel, new Vector2(128, 0)))
            {
                var result = this.termDictionary.DeleteUserEntry(canonicalName);
                this.SetStatus(result.Message, result.Succeeded ? DictionaryWindowStatusKind.Success : DictionaryWindowStatusKind.Warning);
                this.pendingDeleteTerm = null;
                if (result.Succeeded)
                {
                    this.selectedTerm = null;
                    this.isEditing = false;
                    this.onDictionaryChanged();
                }
            }

            ImGui.SameLine();
            if (ImGui.Button("Cancel", new Vector2(88, 0)))
            {
                this.pendingDeleteTerm = null;
            }

            return;
        }

        if (ImGui.Button(actionLabel, new Vector2(136, 0)))
        {
            this.pendingDeleteTerm = canonicalName;
            this.SetStatus(
                $"{actionLabel} selected for {canonicalName}. Click {confirmLabel} to continue.",
                DictionaryWindowStatusKind.Warning);
        }
    }

    private void DrawEditor()
    {
        ImGui.TextColored(AccentColor, this.isCreatingNewEntry ? "Create a new dictionary term" : "Edit dictionary term");
        TextMuted(this.isCreatingNewEntry
            ? "Saved terms go to your user dictionary and are available immediately."
            : "Saving a bundled term creates a user override.");
        ImGui.Separator();
        ImGui.Spacing();

        ImGui.TextUnformatted("Term");
        ImGui.SetNextItemWidth(-1);
        ImGui.InputTextWithHint("##NpcDictionaryEditTerm", "Canonical term name", ref this.editTermName, 160);

        ImGui.Spacing();
        ImGui.TextUnformatted("Definition");
        ImGui.SetNextItemWidth(-1);
        ImGui.InputTextMultiline("##NpcDictionaryEditDefinition", ref this.editDefinition, 4096, new Vector2(-1, 112));

        ImGui.Spacing();
        ImGui.TextUnformatted("Aliases");
        ImGui.SameLine();
        ImGui.TextDisabled("(optional)");
        ImGui.SetNextItemWidth(-1);
        ImGui.InputTextMultiline("##NpcDictionaryEditAliases", ref this.editAliases, 1024, new Vector2(-1, 72));
        TextMuted("One per line, or separated with commas.");

        ImGui.Spacing();
        if (ImGui.Button("Save Term", new Vector2(104, 0)))
        {
            var result = this.termDictionary.AddOrUpdateUserEntry(
                this.editTermName,
                this.editDefinition,
                ParseAliases(this.editAliases));
            this.SetStatus(result.Message, result.Succeeded ? DictionaryWindowStatusKind.Success : DictionaryWindowStatusKind.Warning);
            if (result.Succeeded)
            {
                this.selectedTerm = result.CanonicalName;
                this.isEditing = false;
                this.pendingDeleteTerm = null;
                this.onDictionaryChanged();
            }
        }

        ImGui.SameLine();
        if (ImGui.Button("Cancel", new Vector2(96, 0)))
        {
            this.isEditing = false;
            this.pendingDeleteTerm = null;
        }
    }

    private void StartNewEntry()
    {
        this.editTermName = string.IsNullOrWhiteSpace(this.searchText) ? string.Empty : this.searchText.Trim();
        this.editDefinition = string.Empty;
        this.editAliases = string.Empty;
        this.SetStatus(string.Empty);
        this.pendingDeleteTerm = null;
        this.isEditing = true;
        this.isCreatingNewEntry = true;
    }

    private void StartEditEntry(string term)
    {
        if (!this.termDictionary.TryGetEditableEntry(term, out var entry))
        {
            this.statusMessage = $"Dictionary term not found: {term}";
            return;
        }

        this.editTermName = entry.CanonicalName;
        this.editDefinition = entry.Definition;
        this.editAliases = string.Join(Environment.NewLine, entry.Aliases);
        this.SetStatus(
            entry.IsUserDefined
                ? "Editing a user dictionary term."
                : "Editing a bundled term will save a user override.",
            entry.IsUserDefined ? DictionaryWindowStatusKind.Info : DictionaryWindowStatusKind.Warning);
        this.pendingDeleteTerm = null;
        this.isEditing = true;
        this.isCreatingNewEntry = false;
    }

    private IReadOnlyList<TermListRow> GetFilteredRows()
    {
        var rows = this.termDictionary
            .GetRows()
            .OrderBy(row => row.Term, StringComparer.OrdinalIgnoreCase);

        if (string.IsNullOrWhiteSpace(this.searchText))
        {
            return rows.ToArray();
        }

        var search = this.searchText.Trim();
        return rows
            .Where(row => row.Term.Contains(search, StringComparison.OrdinalIgnoreCase))
            .ToArray();
    }

    private static string? EnsureSelection(IReadOnlyList<TermListRow> rows, string? selectedTerm)
    {
        if (!string.IsNullOrWhiteSpace(selectedTerm) &&
            rows.Any(row => string.Equals(row.Term, selectedTerm, StringComparison.Ordinal)))
        {
            return selectedTerm;
        }

        return rows.Count == 0 ? null : rows[0].Term;
    }

    private static string FormatRowLabel(TermListRow row)
        => row.IsAlias ? $"{row.Term} -> {row.CanonicalName}" : row.Term;

    private static string FormatSourceLabel(TermListRow row)
    {
        if (row.OverridesBundled)
        {
            return "user override";
        }

        return row.IsUserDefined ? "user dictionary" : "bundled dictionary";
    }

    private static string GetDeleteActionLabel(TermListRow row)
    {
        if (row.OverridesBundled)
        {
            return "Delete Override";
        }

        return row.IsUserDefined ? "Delete User Term" : "Hide Bundled Term";
    }

    private static IReadOnlyList<string> ParseAliases(string aliases)
        => aliases
            .Split(['\r', '\n', ',', ';'], StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
            .Where(alias => !string.IsNullOrWhiteSpace(alias))
            .ToArray();

    private void SetStatus(string message, DictionaryWindowStatusKind kind = DictionaryWindowStatusKind.Info)
    {
        this.statusMessage = message;
        this.statusKind = kind;
    }

    private Vector4 GetStatusColor()
        => this.statusKind switch
        {
            DictionaryWindowStatusKind.Success => SuccessColor,
            DictionaryWindowStatusKind.Warning => WarningColor,
            _ => MutedTextColor,
        };

    private static void TextMuted(string text)
    {
        ImGui.TextColored(MutedTextColor, text);
    }

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

internal enum DictionaryWindowStatusKind
{
    Info,
    Success,
    Warning,
}
