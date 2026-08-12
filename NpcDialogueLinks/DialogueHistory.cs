namespace NpcDialogueLinks;

internal sealed class DialogueHistory
{
    private const int MaxEntries = 10;
    private readonly Queue<string> entries = new();

    public void Add(string dialogue)
    {
        var normalized = dialogue.Trim();
        if (string.IsNullOrWhiteSpace(normalized))
        {
            return;
        }

        if (this.entries.Count > 0 &&
            string.Equals(this.entries.Last(), normalized, StringComparison.Ordinal))
        {
            return;
        }

        this.entries.Enqueue(normalized);
        while (this.entries.Count > MaxEntries)
        {
            this.entries.Dequeue();
        }
    }

    public IReadOnlyList<string> GetPreviousLines(string currentDialogue)
    {
        var current = currentDialogue.Trim();
        return this.entries
            .Where(entry => !string.Equals(entry, current, StringComparison.Ordinal))
            .TakeLast(MaxEntries - 1)
            .ToArray();
    }
}
