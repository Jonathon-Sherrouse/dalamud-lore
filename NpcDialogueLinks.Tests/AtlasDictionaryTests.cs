using NpcDialogueLinks.Atlas;

namespace NpcDialogueLinks.Tests;

public sealed class AtlasDictionaryTests
{
    [Fact]
    public void FindsRepeatedWholeTermsAndAliasesWithoutOverlappingLongerTerms()
    {
        var folder = Directory.CreateTempSubdirectory();
        try
        {
            var path = Path.Combine(folder.FullName, "terms.json");
            File.WriteAllText(path, """
                {
                  "Aether": "Energy",
                  "Aether Current": { "definition": "Unlocks flight", "aliases": ["wind current"] },
                  "CAT": "Upper case"
                }
                """);
            // Distinct entries can have match keys that differ only in case.
            var userPath = Path.Combine(folder.FullName, "user-terms.json");
            File.WriteAllText(userPath, """{"Catfish":{"definition":"Fish","aliases":["cat"]}}""");
            var dictionary = new TermDictionary(path, userPath);
            const string text = "Aether Current, aetherial; wind current and aether. cat CAT scat. Aether!";
            var matches = dictionary.FindAtlasLinks(text);

            Assert.Equal(
                ["Aether Current", "wind current", "aether", "cat", "CAT", "Aether"],
                matches.Select(match => text.Substring(match.Start, match.Term.Length)));
            Assert.Equal(
                ["Aether Current", "Aether Current", "Aether", "Catfish", "CAT", "Aether"],
                matches.Select(match => match.CanonicalName));
        }
        finally
        {
            folder.Delete(recursive: true);
        }
    }

    [Fact]
    public void DictionaryMutationsRefreshCachedDefinitionsAndHiddenTerms()
    {
        var folder = Directory.CreateTempSubdirectory();
        try
        {
            var path = Path.Combine(folder.FullName, "terms.json");
            File.WriteAllText(path, """{"Aether":"Original definition"}""");
            var dictionary = new TermDictionary(path);
            const string text = "The aether.";
            Assert.Equal("Original definition", Assert.Single(dictionary.FindAtlasLinks(text)).Definition);
            Assert.True(dictionary.AddOrUpdateUserEntry("Aether", "Updated definition", ["energy"]).Succeeded);
            Assert.Equal("Updated definition", Assert.Single(dictionary.FindAtlasLinks(text)).Definition);
            Assert.True(dictionary.DeleteUserEntry("Aether").Succeeded); // Hide the bundled entry and its override.
            Assert.Empty(dictionary.FindAtlasLinks(text));
        }
        finally
        {
            folder.Delete(recursive: true);
        }
    }

    [Fact]
    public void RequiresTheWarningOnceAndRemembersAcknowledgementWhenDisabled()
    {
        var unset = default(AtlasDictionaryPreference);
        Assert.Equal(AtlasDictionaryPreference.Unacknowledged, AtlasDictionaryOptions.Toggle(unset));
        Assert.Equal(unset, AtlasDictionaryOptions.Confirm(unset, warningOpen: false));
        var enabled = AtlasDictionaryOptions.Confirm(unset, warningOpen: true);
        Assert.Equal(AtlasDictionaryPreference.Enabled, enabled);
        var disabled = AtlasDictionaryOptions.Toggle(enabled);
        Assert.Equal(AtlasDictionaryPreference.Disabled, disabled);
        Assert.Equal(enabled, AtlasDictionaryOptions.Toggle(disabled));
    }
}
