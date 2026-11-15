using Dalamud.Configuration;
using Dalamud.Plugin;

namespace NpcDialogueLinks;

internal sealed class PluginConfiguration : IPluginConfiguration
{
    [NonSerialized]
    private IDalamudPluginInterface? pluginInterface;

    public int Version { get; set; } = 1;

    public bool EnableOnlineExplain { get; set; }

    public bool EnableWebSearch { get; set; } = true;

    public string OpenAiApiKey { get; set; } = string.Empty;

    public string OpenAiModel { get; set; } = "gpt-5-mini";

    public int MaxOutputTokens { get; set; } = 2500;

    /// <summary>Lore Atlas spoiler limit (checkpoint id). Revalidated against the data on every open.</summary>
    public string? AtlasCeilingId { get; set; }

    /// <summary>Lore Atlas "Viewing as of" checkpoint id. Revalidated against the data on every open.</summary>
    public string? AtlasViewId { get; set; }

    public void Initialize(IDalamudPluginInterface pluginInterface)
    {
        this.pluginInterface = pluginInterface;
    }

    public void Save()
    {
        this.pluginInterface?.SavePluginConfig(this);
    }
}
