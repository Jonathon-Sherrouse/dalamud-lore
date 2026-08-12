using System.Text.Json;
using System.Text.Json.Serialization;

namespace NpcDialogueLinks;

internal sealed class TermDictionary
{
    private const string HiddenTermsPropertyName = "$hiddenTerms";

    private static readonly JsonSerializerOptions UserDictionarySerializerOptions = new()
    {
        DefaultIgnoreCondition = JsonIgnoreCondition.WhenWritingNull,
        PropertyNamingPolicy = JsonNamingPolicy.CamelCase,
        WriteIndented = true,
    };

    private readonly object syncRoot = new();
    private Dictionary<string, TermEntry> bundledEntriesByCanonicalName;
    private Dictionary<string, TermEntry> userEntriesByCanonicalName;
    private HashSet<string> hiddenCanonicalNames;
    private Dictionary<string, TermEntry> entriesByCanonicalName;
    private Dictionary<string, TermEntry> entriesByMatchTerm;

    public TermDictionary(string dictionaryPath)
        : this(dictionaryPath, Path.Combine(Path.GetDirectoryName(dictionaryPath) ?? ".", "user-terms.json"))
    {
    }

    public TermDictionary(string bundledDictionaryPath, string userDictionaryPath)
    {
        this.BundledDictionaryPath = Path.GetFullPath(bundledDictionaryPath);
        this.UserDictionaryPath = Path.GetFullPath(userDictionaryPath);
        this.bundledEntriesByCanonicalName = LoadCanonicalDefinitions(this.BundledDictionaryPath);
        (this.userEntriesByCanonicalName, this.hiddenCanonicalNames) = LoadUserDefinitions(this.UserDictionaryPath);
        (this.entriesByCanonicalName, this.entriesByMatchTerm) = BuildMergedDefinitions(
            this.bundledEntriesByCanonicalName,
            this.userEntriesByCanonicalName,
            this.hiddenCanonicalNames);
    }

    public string DictionaryPath => this.BundledDictionaryPath;

    public string BundledDictionaryPath { get; }

    public string UserDictionaryPath { get; }

    public int Count
    {
        get
        {
            lock (this.syncRoot)
            {
                return this.entriesByCanonicalName.Count;
            }
        }
    }

    public IEnumerable<string> CanonicalTerms
    {
        get
        {
            lock (this.syncRoot)
            {
                return this.entriesByCanonicalName.Keys.ToArray();
            }
        }
    }

    public IEnumerable<string> MatchTerms
    {
        get
        {
            lock (this.syncRoot)
            {
                return this.entriesByMatchTerm.Keys.ToArray();
            }
        }
    }

    public IReadOnlyList<TermListRow> GetRows()
    {
        lock (this.syncRoot)
        {
            return this.entriesByMatchTerm
                .Keys
                .OrderBy(value => value, StringComparer.OrdinalIgnoreCase)
                .Select(matchTerm =>
                {
                    var entry = this.entriesByMatchTerm[matchTerm];
                    var isUserDefined = this.userEntriesByCanonicalName.ContainsKey(entry.CanonicalName);
                    return new TermListRow(
                        matchTerm,
                        entry.CanonicalName,
                        entry.Definition,
                        !string.Equals(matchTerm, entry.CanonicalName, StringComparison.Ordinal),
                        isUserDefined,
                        isUserDefined && this.bundledEntriesByCanonicalName.ContainsKey(entry.CanonicalName));
                })
                .ToArray();
        }
    }

    public bool TryGetEntry(string term, out TermEntry entry)
    {
        lock (this.syncRoot)
        {
            return this.entriesByMatchTerm.TryGetValue(term, out entry!);
        }
    }

    public bool TryGetDefinition(string term, out string definition)
    {
        lock (this.syncRoot)
        {
            if (this.entriesByMatchTerm.TryGetValue(term, out var entry))
            {
                definition = entry.Definition;
                return true;
            }
        }

        definition = string.Empty;
        return false;
    }

    public bool TryGetEditableEntry(string term, out EditableTermEntry entry)
    {
        lock (this.syncRoot)
        {
            if (this.entriesByMatchTerm.TryGetValue(term, out var termEntry))
            {
                var isUserDefined = this.userEntriesByCanonicalName.ContainsKey(termEntry.CanonicalName);
                entry = new EditableTermEntry(
                    termEntry.CanonicalName,
                    termEntry.Definition,
                    termEntry.Aliases.ToArray(),
                    isUserDefined,
                    isUserDefined && this.bundledEntriesByCanonicalName.ContainsKey(termEntry.CanonicalName));
                return true;
            }
        }

        entry = new EditableTermEntry(string.Empty, string.Empty, Array.Empty<string>(), false, false);
        return false;
    }

    public DictionaryMutationResult AddOrUpdateUserEntry(
        string canonicalName,
        string definition,
        IReadOnlyList<string> aliases)
    {
        var normalizedCanonicalName = canonicalName.Trim();
        if (string.IsNullOrWhiteSpace(normalizedCanonicalName))
        {
            return DictionaryMutationResult.Failure("Term name is required.");
        }

        var normalizedDefinition = definition.Trim();
        if (string.IsNullOrWhiteSpace(normalizedDefinition))
        {
            return DictionaryMutationResult.Failure("Definition is required.");
        }

        var normalizedAliases = NormalizeAliases(normalizedCanonicalName, aliases);

        lock (this.syncRoot)
        {
            var previousUserEntries = new Dictionary<string, TermEntry>(
                this.userEntriesByCanonicalName,
                StringComparer.OrdinalIgnoreCase);
            var previousHiddenCanonicalNames = new HashSet<string>(
                this.hiddenCanonicalNames,
                StringComparer.OrdinalIgnoreCase);

            var existed = this.entriesByCanonicalName.ContainsKey(normalizedCanonicalName);
            var overridesBundled = this.bundledEntriesByCanonicalName.ContainsKey(normalizedCanonicalName);
            this.userEntriesByCanonicalName[normalizedCanonicalName] =
                new TermEntry(normalizedCanonicalName, normalizedDefinition, normalizedAliases);
            this.hiddenCanonicalNames.Remove(normalizedCanonicalName);
            this.RebuildMergedDefinitions();

            try
            {
                this.SaveUserDefinitions();
            }
            catch (Exception exception)
            {
                this.userEntriesByCanonicalName = previousUserEntries;
                this.hiddenCanonicalNames = previousHiddenCanonicalNames;
                this.RebuildMergedDefinitions();
                Plugin.Log.Warning(exception, "Failed to save user term dictionary to {DictionaryPath}", this.UserDictionaryPath);
                return DictionaryMutationResult.Failure($"Failed to save user dictionary: {exception.Message}");
            }

            var verb = existed ? "Updated" : "Created";
            var source = overridesBundled ? " user override" : " user term";
            return DictionaryMutationResult.Success(
                normalizedCanonicalName,
                $"{verb}{source}: {normalizedCanonicalName}");
        }
    }

    public DictionaryMutationResult DeleteUserEntry(string term)
    {
        var normalizedTerm = term.Trim();
        if (string.IsNullOrWhiteSpace(normalizedTerm))
        {
            return DictionaryMutationResult.Failure("Term name is required.");
        }

        lock (this.syncRoot)
        {
            if (!this.entriesByMatchTerm.TryGetValue(normalizedTerm, out var entry) &&
                !this.entriesByCanonicalName.TryGetValue(normalizedTerm, out entry!))
            {
                return DictionaryMutationResult.Failure($"Dictionary term not found: {normalizedTerm}");
            }

            var previousUserEntries = new Dictionary<string, TermEntry>(
                this.userEntriesByCanonicalName,
                StringComparer.OrdinalIgnoreCase);
            var previousHiddenCanonicalNames = new HashSet<string>(
                this.hiddenCanonicalNames,
                StringComparer.OrdinalIgnoreCase);

            var canonicalName = entry.CanonicalName;
            var removedUserEntry = this.userEntriesByCanonicalName.Remove(canonicalName);
            var hidesBundledEntry = this.bundledEntriesByCanonicalName.ContainsKey(canonicalName);
            if (hidesBundledEntry)
            {
                this.hiddenCanonicalNames.Add(canonicalName);
            }

            this.RebuildMergedDefinitions();

            try
            {
                this.SaveUserDefinitions();
            }
            catch (Exception exception)
            {
                this.userEntriesByCanonicalName = previousUserEntries;
                this.hiddenCanonicalNames = previousHiddenCanonicalNames;
                this.RebuildMergedDefinitions();
                Plugin.Log.Warning(exception, "Failed to save user term dictionary to {DictionaryPath}", this.UserDictionaryPath);
                return DictionaryMutationResult.Failure($"Failed to save user dictionary: {exception.Message}");
            }

            var action = (removedUserEntry, hidesBundledEntry) switch
            {
                (true, true) => "Deleted user override and hid bundled term",
                (true, false) => "Deleted user term",
                (false, true) => "Hid bundled term",
                _ => "Deleted term",
            };

            return DictionaryMutationResult.Success(canonicalName, $"{action}: {canonicalName}");
        }
    }

    public DictionaryMutationResult Reload()
    {
        lock (this.syncRoot)
        {
            this.bundledEntriesByCanonicalName = LoadCanonicalDefinitions(this.BundledDictionaryPath);
            (this.userEntriesByCanonicalName, this.hiddenCanonicalNames) = LoadUserDefinitions(this.UserDictionaryPath);
            this.RebuildMergedDefinitions();
            return DictionaryMutationResult.Success(
                string.Empty,
                $"Reloaded {this.entriesByCanonicalName.Count} dictionary terms ({this.userEntriesByCanonicalName.Count} user).");
        }
    }

    private static Dictionary<string, TermEntry> LoadCanonicalDefinitions(string dictionaryPath)
    {
        var entriesByCanonicalName = new Dictionary<string, TermEntry>(StringComparer.OrdinalIgnoreCase);

        if (!File.Exists(dictionaryPath))
        {
            return entriesByCanonicalName;
        }

        try
        {
            using var document = JsonDocument.Parse(File.ReadAllText(dictionaryPath));
            if (document.RootElement.ValueKind != JsonValueKind.Object)
            {
                return entriesByCanonicalName;
            }

            foreach (var property in document.RootElement.EnumerateObject())
            {
                var canonicalName = property.Name.Trim();
                if (string.IsNullOrWhiteSpace(canonicalName))
                {
                    continue;
                }

                var entry = ParseEntry(canonicalName, property.Value);
                if (entry is null)
                {
                    continue;
                }

                entriesByCanonicalName[entry.CanonicalName] = entry;
            }
        }
        catch (Exception exception)
        {
            Plugin.Log.Warning(exception, "Failed to load term dictionary from {DictionaryPath}", dictionaryPath);
        }

        return entriesByCanonicalName;
    }

    private static (Dictionary<string, TermEntry> EntriesByCanonicalName, HashSet<string> HiddenCanonicalNames)
        LoadUserDefinitions(string dictionaryPath)
    {
        var entriesByCanonicalName = new Dictionary<string, TermEntry>(StringComparer.OrdinalIgnoreCase);
        var hiddenCanonicalNames = new HashSet<string>(StringComparer.OrdinalIgnoreCase);

        if (!File.Exists(dictionaryPath))
        {
            return (entriesByCanonicalName, hiddenCanonicalNames);
        }

        try
        {
            using var document = JsonDocument.Parse(File.ReadAllText(dictionaryPath));
            if (document.RootElement.ValueKind != JsonValueKind.Object)
            {
                return (entriesByCanonicalName, hiddenCanonicalNames);
            }

            foreach (var property in document.RootElement.EnumerateObject())
            {
                var canonicalName = property.Name.Trim();
                if (string.Equals(canonicalName, HiddenTermsPropertyName, StringComparison.OrdinalIgnoreCase))
                {
                    foreach (var hiddenName in ParseHiddenTermNames(property.Value))
                    {
                        hiddenCanonicalNames.Add(hiddenName);
                    }

                    continue;
                }

                if (string.IsNullOrWhiteSpace(canonicalName))
                {
                    continue;
                }

                var entry = ParseEntry(canonicalName, property.Value);
                if (entry is null)
                {
                    continue;
                }

                entriesByCanonicalName[entry.CanonicalName] = entry;
            }
        }
        catch (Exception exception)
        {
            Plugin.Log.Warning(exception, "Failed to load user term dictionary from {DictionaryPath}", dictionaryPath);
        }

        return (entriesByCanonicalName, hiddenCanonicalNames);
    }

    private static (Dictionary<string, TermEntry> EntriesByCanonicalName, Dictionary<string, TermEntry> EntriesByMatchTerm)
        BuildMergedDefinitions(
            Dictionary<string, TermEntry> bundledEntries,
            Dictionary<string, TermEntry> userEntries,
            HashSet<string> hiddenCanonicalNames)
    {
        var entriesByCanonicalName = new Dictionary<string, TermEntry>(StringComparer.OrdinalIgnoreCase);
        foreach (var entry in bundledEntries.Values)
        {
            if (hiddenCanonicalNames.Contains(entry.CanonicalName))
            {
                continue;
            }

            entriesByCanonicalName[entry.CanonicalName] = entry;
        }

        foreach (var entry in userEntries.Values)
        {
            entriesByCanonicalName[entry.CanonicalName] = entry;
        }

        var entriesByMatchTerm = new Dictionary<string, TermEntry>(StringComparer.Ordinal);
        foreach (var entry in entriesByCanonicalName.Values)
        {
            foreach (var matchTerm in entry.MatchTerms)
            {
                entriesByMatchTerm[matchTerm] = entry;
            }
        }

        return (entriesByCanonicalName, entriesByMatchTerm);
    }

    private void RebuildMergedDefinitions()
    {
        (this.entriesByCanonicalName, this.entriesByMatchTerm) = BuildMergedDefinitions(
            this.bundledEntriesByCanonicalName,
            this.userEntriesByCanonicalName,
            this.hiddenCanonicalNames);
    }

    private void SaveUserDefinitions()
    {
        var serializedEntries = new SortedDictionary<string, object>(StringComparer.OrdinalIgnoreCase);
        if (this.hiddenCanonicalNames.Count > 0)
        {
            serializedEntries[HiddenTermsPropertyName] = this.hiddenCanonicalNames
                .OrderBy(term => term, StringComparer.OrdinalIgnoreCase)
                .ToArray();
        }

        foreach (var entry in this.userEntriesByCanonicalName.Values.OrderBy(entry => entry.CanonicalName, StringComparer.OrdinalIgnoreCase))
        {
            serializedEntries[entry.CanonicalName] = entry.Aliases.Count == 0
                ? entry.Definition
                : new SerializedTermEntry(entry.Definition, entry.Aliases);
        }

        var directory = Path.GetDirectoryName(this.UserDictionaryPath);
        if (!string.IsNullOrWhiteSpace(directory))
        {
            Directory.CreateDirectory(directory);
        }

        var json = JsonSerializer.Serialize(serializedEntries, UserDictionarySerializerOptions);
        File.WriteAllText(this.UserDictionaryPath, json + Environment.NewLine);
    }

    private static IReadOnlyList<string> NormalizeAliases(string canonicalName, IReadOnlyList<string> aliases)
    {
        var seen = new HashSet<string>(StringComparer.Ordinal) { canonicalName };
        var normalizedAliases = new List<string>();

        foreach (var alias in aliases)
        {
            var normalized = alias.Trim();
            if (string.IsNullOrWhiteSpace(normalized) || !seen.Add(normalized))
            {
                continue;
            }

            normalizedAliases.Add(normalized);
        }

        return normalizedAliases;
    }

    private static IReadOnlyList<string> ParseHiddenTermNames(JsonElement element)
    {
        if (element.ValueKind != JsonValueKind.Array)
        {
            return Array.Empty<string>();
        }

        var names = new List<string>();
        foreach (var item in element.EnumerateArray())
        {
            if (item.ValueKind != JsonValueKind.String)
            {
                continue;
            }

            var name = item.GetString()?.Trim();
            if (!string.IsNullOrWhiteSpace(name))
            {
                names.Add(name);
            }
        }

        return names;
    }

    private static TermEntry? ParseEntry(string canonicalName, JsonElement element)
    {
        switch (element.ValueKind)
        {
            case JsonValueKind.String:
            {
                var definition = element.GetString()?.Trim();
                return string.IsNullOrWhiteSpace(definition)
                    ? null
                    : new TermEntry(canonicalName, definition, Array.Empty<string>());
            }

            case JsonValueKind.Object:
            {
                if (!element.TryGetProperty("definition", out var definitionElement))
                {
                    return null;
                }

                var definition = definitionElement.GetString()?.Trim();
                if (string.IsNullOrWhiteSpace(definition))
                {
                    return null;
                }

                var aliases = new List<string>();
                if (element.TryGetProperty("aliases", out var aliasesElement) &&
                    aliasesElement.ValueKind == JsonValueKind.Array)
                {
                    foreach (var aliasElement in aliasesElement.EnumerateArray())
                    {
                        if (aliasElement.ValueKind != JsonValueKind.String)
                        {
                            continue;
                        }

                        var alias = aliasElement.GetString()?.Trim();
                        if (!string.IsNullOrWhiteSpace(alias))
                        {
                            aliases.Add(alias);
                        }
                    }
                }

                return new TermEntry(canonicalName, definition, aliases);
            }

            default:
                return null;
        }
    }

    private sealed record SerializedTermEntry(string Definition, IReadOnlyList<string> Aliases);
}

internal sealed record TermListRow(
    string Term,
    string CanonicalName,
    string Definition,
    bool IsAlias,
    bool IsUserDefined,
    bool OverridesBundled);

internal sealed record EditableTermEntry(
    string CanonicalName,
    string Definition,
    IReadOnlyList<string> Aliases,
    bool IsUserDefined,
    bool OverridesBundled);

internal sealed record DictionaryMutationResult(bool Succeeded, string CanonicalName, string Message)
{
    public static DictionaryMutationResult Success(string canonicalName, string message)
        => new(true, canonicalName, message);

    public static DictionaryMutationResult Failure(string message)
        => new(false, string.Empty, message);
}

internal sealed class TermEntry
{
    public TermEntry(string canonicalName, string definition, IReadOnlyList<string> aliases)
    {
        this.CanonicalName = canonicalName;
        this.Definition = definition;
        this.Aliases = aliases;
        this.MatchTerms = BuildMatchTerms(canonicalName, aliases);
    }

    public string CanonicalName { get; }

    public string Definition { get; }

    public IReadOnlyList<string> Aliases { get; }

    public IReadOnlyList<string> MatchTerms { get; }

    private static IReadOnlyList<string> BuildMatchTerms(string canonicalName, IReadOnlyList<string> aliases)
    {
        var seen = new HashSet<string>(StringComparer.Ordinal);
        var terms = new List<string>();

        AddTerm(canonicalName);
        foreach (var alias in aliases)
        {
            AddTerm(alias);
        }

        return terms;

        void AddTerm(string value)
        {
            var normalized = value.Trim();
            if (string.IsNullOrWhiteSpace(normalized) || !seen.Add(normalized))
            {
                return;
            }

            terms.Add(normalized);
        }
    }
}
