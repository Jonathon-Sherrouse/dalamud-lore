using System.Text.Json;

namespace NpcDialogueLinks;

internal sealed class TermDictionary
{
    private readonly Dictionary<string, string> definitions;

    public TermDictionary(string dictionaryPath)
    {
        this.DictionaryPath = Path.GetFullPath(dictionaryPath);
        this.definitions = LoadDefinitions(this.DictionaryPath);
    }

    public string DictionaryPath { get; }

    public int Count => this.definitions.Count;

    public IEnumerable<string> Terms => this.definitions.Keys;

    public bool TryGetDefinition(string term, out string definition)
        => this.definitions.TryGetValue(term, out definition!);

    private static Dictionary<string, string> LoadDefinitions(string dictionaryPath)
    {
        if (!File.Exists(dictionaryPath))
        {
            return new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase);
        }

        try
        {
            var json = File.ReadAllText(dictionaryPath);
            var loaded = JsonSerializer.Deserialize<Dictionary<string, string>>(json);
            if (loaded is null)
            {
                return new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase);
            }

            return new Dictionary<string, string>(loaded, StringComparer.OrdinalIgnoreCase);
        }
        catch (Exception exception)
        {
            Plugin.Log.Warning(exception, "Failed to load term dictionary from {DictionaryPath}", dictionaryPath);
            return new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase);
        }
    }
}
