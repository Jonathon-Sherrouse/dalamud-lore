namespace NpcDialogueLinks;

internal static class DialogueText
{
    public static string Normalize(string rawText)
    {
        var sanitized = rawText.ReplaceLineEndings(" ");
        while (sanitized.Contains("===", StringComparison.Ordinal))
        {
            sanitized = sanitized.Replace("===", " ", StringComparison.Ordinal);
        }

        var characters = sanitized
            .Where(character => !char.IsControl(character) || char.IsWhiteSpace(character))
            .ToArray();

        return string.Join(
                " ",
                new string(characters).Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries))
            .Trim();
    }
}
