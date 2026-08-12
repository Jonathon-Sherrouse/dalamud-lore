using System.Net.Http.Headers;
using System.Text;
using System.Text.Json;
using System.Text.Json.Serialization;
using System.Text.RegularExpressions;

namespace NpcDialogueLinks;

internal sealed class LoreExplainClient : IDisposable
{
    private static readonly JsonSerializerOptions SerializerOptions = new()
    {
        PropertyNamingPolicy = JsonNamingPolicy.CamelCase,
        DefaultIgnoreCondition = JsonIgnoreCondition.WhenWritingNull,
    };

    private readonly HttpClient httpClient = new()
    {
        BaseAddress = new Uri("https://api.openai.com/v1/"),
        Timeout = TimeSpan.FromSeconds(60),
    };

    public async Task<LoreExplainResult> ExplainAsync(
        PluginConfiguration configuration,
        LoreExplainRequest request,
        CancellationToken cancellationToken)
    {
        if (string.IsNullOrWhiteSpace(configuration.OpenAiApiKey))
        {
            throw new InvalidOperationException("OpenAI API key is not configured.");
        }

        using var httpRequest = new HttpRequestMessage(HttpMethod.Post, "responses");
        httpRequest.Headers.Authorization = new AuthenticationHeaderValue("Bearer", configuration.OpenAiApiKey);

        var payload = BuildPayload(configuration, request);
        httpRequest.Content = new StringContent(JsonSerializer.Serialize(payload, SerializerOptions), Encoding.UTF8, "application/json");

        using var response = await this.httpClient.SendAsync(httpRequest, cancellationToken).ConfigureAwait(false);
        var responseBody = await response.Content.ReadAsStringAsync(cancellationToken).ConfigureAwait(false);
        if (!response.IsSuccessStatusCode)
        {
            throw new InvalidOperationException($"OpenAI request failed ({(int)response.StatusCode}): {ExtractErrorMessage(responseBody)}");
        }

        using var document = JsonDocument.Parse(responseBody);
        ThrowIfResponseIncomplete(document.RootElement);

        var text = ExtractOutputText(document.RootElement).Trim();
        if (string.IsNullOrWhiteSpace(text))
        {
            throw new InvalidOperationException("OpenAI returned a successful response, but no answer text was found. Try increasing max output tokens or disabling web search, then try again.");
        }

        var sources = ExtractSources(document.RootElement);
        var dictionaryProposals = ExtractDictionaryProposals(text, sources);

        return new LoreExplainResult(CleanAnswerText(text), sources, dictionaryProposals);
    }

    public void Dispose()
    {
        this.httpClient.Dispose();
    }

    private static object BuildPayload(PluginConfiguration configuration, LoreExplainRequest request)
    {
        var knownTerms = request.KnownTerms.Count == 0
            ? "None detected locally."
            : string.Join(", ", request.KnownTerms);

        var userInput = new StringBuilder()
            .AppendLine("Dialogue:")
            .AppendLine(request.Dialogue)
            .AppendLine()
            .AppendLine("Recent dialogue history:")
            .AppendLine(BuildDialogueHistoryText(request.DialogueHistory))
            .AppendLine()
            .AppendLine("User question:")
            .AppendLine(string.IsNullOrWhiteSpace(request.Question) ? "(none)" : request.Question)
            .AppendLine()
            .AppendLine("Previous answer:")
            .AppendLine(string.IsNullOrWhiteSpace(request.PreviousAnswer) ? "(none)" : request.PreviousAnswer)
            .AppendLine()
            .AppendLine("Conversation transcript:")
            .AppendLine(string.IsNullOrWhiteSpace(request.ConversationTranscript) ? "(none)" : request.ConversationTranscript)
            .AppendLine()
            .AppendLine("Follow-up question:")
            .AppendLine(string.IsNullOrWhiteSpace(request.FollowUpQuestion) ? "(none)" : request.FollowUpQuestion)
            .AppendLine()
            .AppendLine("Known local dictionary terms:")
            .AppendLine(knownTerms)
            .AppendLine()
            .AppendLine("Game context metadata:")
            .AppendLine(BuildMetadataText(request.Metadata))
            .AppendLine()
            .AppendLine("Web search:")
            .AppendLine(configuration.EnableWebSearch ? "enabled" : "disabled")
            .ToString();

        var tools = configuration.EnableWebSearch
            ? new object[] { new { type = "web_search" } }
            : Array.Empty<object>();

        return new
        {
            model = string.IsNullOrWhiteSpace(configuration.OpenAiModel) ? "gpt-5-mini" : configuration.OpenAiModel,
            instructions = string.Join(
                "\n",
                "You explain Final Fantasy XIV dialogue for a player who is confused in the moment.",
                "Start with the direct answer immediately. Do not spend tokens on preamble or hidden planning.",
                "Be concise, plain-language, and spoiler-careful.",
                "Answer the user's specific question first when one is provided.",
                "If a follow-up question is provided, answer it using the dialogue and previous answer as context.",
                "Use recent dialogue history only when it clarifies pronouns, references, relationships, or scene continuity.",
                "Do not summarize the entire history unless the user asks.",
                "Use game context metadata when it helps identify speaker, zone, or scene context.",
                "Speaker metadata may be best-effort; do not overstate it when confidence is low.",
                "Quest metadata may be unavailable; do not invent quest names or ids.",
                "Use the provided local dictionary terms first when they are relevant.",
                "When the user asks who a title, epithet, or codename refers to, identify the most likely named character if the local terms or search results support it.",
                "If web search is enabled and an unfamiliar proper noun, title, epithet, codename, faction, place, or quest term is important to the user's question, use web search before saying you cannot identify it.",
                "When using web search, prefer ffxiv.consolegameswiki.com for Final Fantasy XIV lore, NPC, quest, place, faction, and game-term citations.",
                "Use other sources only when ffxiv.consolegameswiki.com does not have relevant coverage or when another source is needed to resolve ambiguity.",
                "If web search is enabled, do not ask the user for quest or zone context until after you have tried to identify the term from available sources.",
                "If web search is disabled, use general Final Fantasy XIV knowledge to give the most likely explanation.",
                "If you are inferring from limited context, say so briefly, then still provide the best likely answer.",
                "Explain only the context needed to understand this passage.",
                "Keep the whole answer under 180 words unless citations require a little more.",
                "Use citations when web search provides sources.",
                "Do not fabricate precise quest IDs, patch details, or source-backed claims you cannot support.",
                "After the player-facing answer, append a machine-readable dictionary proposal block.",
                "Use exactly this wrapper: <dictionary_proposals>[...]</dictionary_proposals>.",
                "Use [] when no reusable dictionary entry is useful.",
                "Each proposal object must use canonicalName, definition, aliases, and sources keys.",
                "Keep proposal definitions concise enough for an in-game dictionary click.",
                "Only propose entries supported by the local context or searched sources."),
            input = userInput,
            max_output_tokens = Math.Clamp(configuration.MaxOutputTokens, 200, 6000),
            store = false,
            tools = tools.Length == 0 ? null : tools,
            tool_choice = configuration.EnableWebSearch ? "auto" : null,
            include = configuration.EnableWebSearch ? new[] { "web_search_call.action.sources" } : null,
        };
    }

    private static string BuildMetadataText(LoreContextMetadata metadata)
    {
        if (!metadata.HasAnyContext)
        {
            return "None available.";
        }

        var builder = new StringBuilder();
        if (!string.IsNullOrWhiteSpace(metadata.ZoneName))
        {
            builder.AppendLine($"Zone: {metadata.ZoneName}");
        }

        if (metadata.TerritoryType != 0)
        {
            builder.AppendLine($"TerritoryType: {metadata.TerritoryType}");
        }

        if (metadata.MapId != 0)
        {
            builder.AppendLine($"MapId: {metadata.MapId}");
        }

        if (!string.IsNullOrWhiteSpace(metadata.TargetName))
        {
            builder.AppendLine($"Current target: {metadata.TargetName}");
        }

        if (!string.IsNullOrWhiteSpace(metadata.SpeakerName))
        {
            builder.AppendLine($"Possible speaker: {metadata.SpeakerName} ({metadata.SpeakerConfidence})");
        }

        if (!metadata.HasVerifiedQuestContext)
        {
            return builder.ToString().Trim();
        }

        if (!string.IsNullOrWhiteSpace(metadata.QuestName))
        {
            builder.AppendLine($"Quest: {metadata.QuestName}");
        }

        if (metadata.QuestId.HasValue)
        {
            builder.AppendLine($"QuestId: {metadata.QuestId.Value}");
        }

        builder.AppendLine($"Quest metadata confidence: {metadata.QuestConfidence}");

        return builder.ToString().Trim();
    }

    private static string BuildDialogueHistoryText(IReadOnlyList<string> dialogueHistory)
    {
        if (dialogueHistory.Count == 0)
        {
            return "None available.";
        }

        var builder = new StringBuilder();
        for (var index = 0; index < dialogueHistory.Count; index++)
        {
            builder.AppendLine($"{index + 1}. {dialogueHistory[index]}");
        }

        return builder.ToString().Trim();
    }

    private static string ExtractOutputText(JsonElement root)
    {
        if (root.TryGetProperty("output_text", out var outputTextElement) &&
            outputTextElement.ValueKind == JsonValueKind.String)
        {
            return outputTextElement.GetString() ?? string.Empty;
        }

        var builder = new StringBuilder();
        ExtractOutputText(root, builder);
        return builder.ToString();
    }

    private static void ExtractOutputText(JsonElement element, StringBuilder builder)
    {
        switch (element.ValueKind)
        {
            case JsonValueKind.Object:
                if (element.TryGetProperty("type", out var typeElement) &&
                    IsTextContentType(typeElement.GetString()) &&
                    element.TryGetProperty("text", out var textElement))
                {
                    builder.AppendLine(textElement.GetString());
                }

                foreach (var property in element.EnumerateObject())
                {
                    ExtractOutputText(property.Value, builder);
                }

                break;
            case JsonValueKind.Array:
                foreach (var item in element.EnumerateArray())
                {
                    ExtractOutputText(item, builder);
                }

                break;
        }
    }

    private static bool IsTextContentType(string? type)
        => string.Equals(type, "output_text", StringComparison.Ordinal) ||
           string.Equals(type, "text", StringComparison.Ordinal);

    private static string NormalizeDisplayText(string text)
        => text
            .Replace('\u2018', '\'')
            .Replace('\u2019', '\'')
            .Replace('\u201C', '"')
            .Replace('\u201D', '"')
            .Replace("\u2014", " - ", StringComparison.Ordinal)
            .Replace("\u2013", "-", StringComparison.Ordinal)
            .Replace('\u00A0', ' ');

    private static string CleanAnswerText(string text)
    {
        var normalized = NormalizeDisplayText(text);
        normalized = Regex.Replace(
            normalized,
            @"\s*<dictionary_proposals>.*?</dictionary_proposals>\s*",
            "\n",
            RegexOptions.IgnoreCase | RegexOptions.Singleline);
        normalized = Regex.Replace(normalized, @"\s*\(\[[^\]]+\]\(https?://[^)]+\)\)", string.Empty);
        normalized = Regex.Replace(normalized, @"\[([^\]]+)\]\(https?://[^)]+\)", "$1");
        normalized = Regex.Replace(normalized, @"[ \t]{2,}", " ");
        return normalized.Trim();
    }

    private static IReadOnlyList<DictionaryProposal> ExtractDictionaryProposals(
        string text,
        IReadOnlyList<LoreExplainSource> responseSources)
    {
        var match = Regex.Match(
            text,
            @"<dictionary_proposals>\s*(?<json>\[.*?\])\s*</dictionary_proposals>",
            RegexOptions.IgnoreCase | RegexOptions.Singleline);
        if (!match.Success)
        {
            return Array.Empty<DictionaryProposal>();
        }

        try
        {
            var proposalDtos = JsonSerializer.Deserialize<List<DictionaryProposalDto>>(
                match.Groups["json"].Value,
                SerializerOptions);
            if (proposalDtos is null || proposalDtos.Count == 0)
            {
                return Array.Empty<DictionaryProposal>();
            }

            var fallbackSources = responseSources.Select(source => source.Url).ToArray();
            return proposalDtos
                .Select(dto => CreateDictionaryProposal(dto, fallbackSources))
                .Where(proposal => proposal is not null)
                .Select(proposal => proposal!)
                .ToArray();
        }
        catch (JsonException)
        {
            return Array.Empty<DictionaryProposal>();
        }
    }

    private static DictionaryProposal? CreateDictionaryProposal(
        DictionaryProposalDto dto,
        IReadOnlyList<string> fallbackSources)
    {
        var canonicalName = dto.CanonicalName?.Trim();
        var definition = dto.Definition?.Trim();
        if (string.IsNullOrWhiteSpace(canonicalName) || string.IsNullOrWhiteSpace(definition))
        {
            return null;
        }

        var aliases = dto.Aliases?
            .Select(alias => alias.Trim())
            .Where(alias => !string.IsNullOrWhiteSpace(alias))
            .Distinct(StringComparer.OrdinalIgnoreCase)
            .ToArray() ?? Array.Empty<string>();
        var sources = dto.Sources?
            .Select(source => source.Trim())
            .Where(source => !string.IsNullOrWhiteSpace(source))
            .Distinct(StringComparer.OrdinalIgnoreCase)
            .ToArray();

        return new DictionaryProposal(
            canonicalName,
            definition,
            aliases,
            sources is { Length: > 0 } ? sources : fallbackSources);
    }

    private static void ThrowIfResponseIncomplete(JsonElement root)
    {
        if (!root.TryGetProperty("status", out var statusElement))
        {
            return;
        }

        var status = statusElement.GetString();
        if (!string.Equals(status, "incomplete", StringComparison.OrdinalIgnoreCase) &&
            !string.Equals(status, "failed", StringComparison.OrdinalIgnoreCase) &&
            !string.Equals(status, "cancelled", StringComparison.OrdinalIgnoreCase))
        {
            return;
        }

        var details = string.Empty;
        if (root.TryGetProperty("incomplete_details", out var incompleteDetails) &&
            incompleteDetails.ValueKind != JsonValueKind.Null)
        {
            details = incompleteDetails.ToString();
        }
        else if (root.TryGetProperty("error", out var error) &&
                 error.ValueKind != JsonValueKind.Null)
        {
            details = error.ToString();
        }

        throw new InvalidOperationException($"OpenAI response status was {status}. {details}".Trim());
    }

    private static IReadOnlyList<LoreExplainSource> ExtractSources(JsonElement root)
    {
        var sources = new List<LoreExplainSource>();
        var seen = new HashSet<string>(StringComparer.OrdinalIgnoreCase);
        ExtractSources(root, sources, seen);
        return sources;
    }

    private static void ExtractSources(JsonElement element, List<LoreExplainSource> sources, HashSet<string> seen)
    {
        switch (element.ValueKind)
        {
            case JsonValueKind.Object:
                var isUrlCitation = element.TryGetProperty("type", out var typeElement) &&
                    string.Equals(typeElement.GetString(), "url_citation", StringComparison.Ordinal);
                var looksLikeSource = element.TryGetProperty("title", out _);
                if ((isUrlCitation || looksLikeSource) && element.TryGetProperty("url", out var urlElement))
                {
                    var url = urlElement.GetString()?.Trim();
                    if (!string.IsNullOrWhiteSpace(url) && seen.Add(url))
                    {
                        url = CleanSourceUrl(url);
                        var title = element.TryGetProperty("title", out var titleElement)
                            ? titleElement.GetString() ?? url
                            : url;
                        sources.Add(new LoreExplainSource(title, url));
                    }
                }

                foreach (var property in element.EnumerateObject())
                {
                    ExtractSources(property.Value, sources, seen);
                }

                break;
            case JsonValueKind.Array:
                foreach (var item in element.EnumerateArray())
                {
                    ExtractSources(item, sources, seen);
                }

                break;
        }
    }

    private static string CleanSourceUrl(string url)
        => url
            .Replace("?utm_source=openai", string.Empty, StringComparison.OrdinalIgnoreCase)
            .Replace("&utm_source=openai", string.Empty, StringComparison.OrdinalIgnoreCase);

    private static string ExtractErrorMessage(string responseBody)
    {
        try
        {
            using var document = JsonDocument.Parse(responseBody);
            if (document.RootElement.TryGetProperty("error", out var error) &&
                error.TryGetProperty("message", out var message))
            {
                return message.GetString() ?? responseBody;
            }
        }
        catch (JsonException)
        {
        }

        return responseBody;
    }

    private sealed class DictionaryProposalDto
    {
        public string? CanonicalName { get; set; }

        public string? Definition { get; set; }

        public List<string>? Aliases { get; set; }

        public List<string>? Sources { get; set; }
    }
}

internal sealed record LoreExplainRequest(
    string Dialogue,
    string Question,
    IReadOnlyList<string> KnownTerms,
    LoreContextMetadata Metadata,
    IReadOnlyList<string> DialogueHistory,
    string PreviousAnswer = "",
    string FollowUpQuestion = "",
    string ConversationTranscript = "");

internal sealed record LoreExplainResult(
    string Text,
    IReadOnlyList<LoreExplainSource> Sources,
    IReadOnlyList<DictionaryProposal> DictionaryProposals);

internal sealed record LoreExplainSource(string Title, string Url);

internal sealed record DictionaryProposal(
    string CanonicalName,
    string Definition,
    IReadOnlyList<string> Aliases,
    IReadOnlyList<string> Sources);
