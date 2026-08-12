namespace NpcDialogueLinks;

internal static partial class LinkCandidateExtractor
{
    public static IReadOnlyList<string> Extract(string dialogue, IEnumerable<string> dictionaryTerms)
    {
        if (string.IsNullOrWhiteSpace(dialogue))
        {
            return Array.Empty<string>();
        }

        var candidates = new List<(string Text, int Index)>();
        var seen = new HashSet<string>(StringComparer.OrdinalIgnoreCase);

        foreach (var term in dictionaryTerms)
        {
            if (string.IsNullOrWhiteSpace(term))
            {
                continue;
            }

            var normalizedTerm = term.Trim();
            var index = FindWholeTermIndex(dialogue, normalizedTerm);
            if (index < 0 || !seen.Add(normalizedTerm))
            {
                continue;
            }

            candidates.Add((normalizedTerm, index));
        }

        return candidates
            .OrderBy(candidate => candidate.Index)
            .ThenByDescending(candidate => candidate.Text.Length)
            .Take(5)
            .Select(candidate => candidate.Text)
            .ToArray();
    }

    private static int FindWholeTermIndex(string dialogue, string term)
    {
        var exactIndex = FindWholeTermVariantIndex(dialogue, term);
        var sentenceCapitalizedTerm = BuildSentenceCapitalizationVariant(term);
        if (sentenceCapitalizedTerm is null)
        {
            return exactIndex;
        }

        var sentenceCapitalizedIndex = FindWholeTermVariantIndex(dialogue, sentenceCapitalizedTerm);
        if (exactIndex < 0)
        {
            return sentenceCapitalizedIndex;
        }

        return sentenceCapitalizedIndex < 0
            ? exactIndex
            : Math.Min(exactIndex, sentenceCapitalizedIndex);
    }

    private static int FindWholeTermVariantIndex(string dialogue, string term)
    {
        var searchIndex = 0;

        while (searchIndex < dialogue.Length)
        {
            var index = dialogue.IndexOf(term, searchIndex, StringComparison.Ordinal);
            if (index < 0)
            {
                return -1;
            }

            if (HasTermBoundaries(dialogue, index, term.Length))
            {
                return index;
            }

            searchIndex = index + 1;
        }

        return -1;
    }

    private static string? BuildSentenceCapitalizationVariant(string term)
    {
        if (term.Length == 0 || !char.IsLower(term[0]))
        {
            return null;
        }

        var characters = term.ToCharArray();
        characters[0] = char.ToUpperInvariant(characters[0]);
        return new string(characters);
    }

    private static bool HasTermBoundaries(string dialogue, int index, int length)
    {
        var startsInsideWord = index > 0 && IsWordCharacter(dialogue[index - 1]) && IsWordCharacter(dialogue[index]);
        if (startsInsideWord)
        {
            return false;
        }

        var endIndex = index + length;
        return endIndex >= dialogue.Length ||
            !IsWordCharacter(dialogue[endIndex - 1]) ||
            !IsWordCharacter(dialogue[endIndex]);
    }

    private static bool IsWordCharacter(char value)
        => char.IsLetterOrDigit(value) || value == '_';
}
