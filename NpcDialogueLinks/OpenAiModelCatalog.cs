namespace NpcDialogueLinks;

internal static class OpenAiModelCatalog
{
    public static readonly IReadOnlyList<OpenAiModelOption> Options =
    [
        new(
            "gpt-5-mini",
            "GPT-5 mini",
            "$0.25 in / $2.00 out per 1M tokens",
            "Recommended balance for short lore explanations."),
        new(
            "gpt-4.1-mini",
            "GPT-4.1 mini",
            "$0.40 in / $1.60 out per 1M tokens",
            "Fast, low-latency fallback for concise answers."),
        new(
            "gpt-5-nano",
            "GPT-5 nano",
            "$0.05 in / $0.40 out per 1M tokens",
            "Cheapest option; best for simple summaries."),
        new(
            "gpt-5.1",
            "GPT-5.1",
            "$1.25 in / $10.00 out per 1M tokens",
            "Stronger reasoning for more tangled dialogue."),
        new(
            "gpt-5.2",
            "GPT-5.2",
            "$1.75 in / $14.00 out per 1M tokens",
            "Higher quality, higher cost."),
        new(
            "gpt-5",
            "GPT-5",
            "$1.25 in / $10.00 out per 1M tokens",
            "General high-quality option."),
        new(
            "gpt-4.1",
            "GPT-4.1",
            "$2.00 in / $8.00 out per 1M tokens",
            "Strong non-reasoning model with higher input cost."),
    ];

    public static OpenAiModelOption Find(string model)
        => Options.FirstOrDefault(option => string.Equals(option.Id, model, StringComparison.OrdinalIgnoreCase))
           ?? Options[0];
}

internal sealed record OpenAiModelOption(string Id, string Label, string Pricing, string Notes)
{
    public string DisplayName => $"{this.Label} ({this.Pricing})";
}
