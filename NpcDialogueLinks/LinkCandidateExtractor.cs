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
            var index = dialogue.IndexOf(normalizedTerm, StringComparison.OrdinalIgnoreCase);
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
}
