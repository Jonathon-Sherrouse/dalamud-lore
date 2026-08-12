using System.Numerics;
using Dalamud.Bindings.ImGui;
using Dalamud.Interface.Windowing;

namespace NpcDialogueLinks;

internal sealed class SettingsWindow : Window
{
    private readonly PluginConfiguration configuration;
    private string apiKey;
    private int maxOutputTokens;

    public SettingsWindow(PluginConfiguration configuration)
        : base("NPC Dialogue Links Settings###NpcDialogueLinksSettings")
    {
        this.configuration = configuration;
        this.apiKey = configuration.OpenAiApiKey;
        this.maxOutputTokens = configuration.MaxOutputTokens;
        this.Size = new Vector2(640, 360);
        this.SizeCondition = ImGuiCond.FirstUseEver;
        this.SizeConstraints = new()
        {
            MinimumSize = new Vector2(520, 300),
            MaximumSize = new Vector2(1100, 900),
        };
        this.ShowCloseButton = true;
        this.RespectCloseHotkey = true;
    }

    public override void OnOpen()
    {
        this.apiKey = this.configuration.OpenAiApiKey;
        this.maxOutputTokens = this.configuration.MaxOutputTokens;
    }

    public override void Draw()
    {
        var enableOnlineExplain = this.configuration.EnableOnlineExplain;
        if (ImGui.Checkbox("Enable live Lore Explain", ref enableOnlineExplain))
        {
            this.configuration.EnableOnlineExplain = enableOnlineExplain;
            this.configuration.Save();
        }

        var enableWebSearch = this.configuration.EnableWebSearch;
        if (ImGui.Checkbox("Allow OpenAI web search for citations", ref enableWebSearch))
        {
            this.configuration.EnableWebSearch = enableWebSearch;
            this.configuration.Save();
        }

        ImGui.Spacing();
        ImGui.TextWrapped("Your API key is stored in the local Dalamud plugin config. Leave live explain off if you only want request export files.");
        ImGui.Spacing();

        ImGui.SetNextItemWidth(-1);
        ImGui.InputTextWithHint("##NpcDialogueLinksApiKey", "OpenAI API key", ref this.apiKey, 256, ImGuiInputTextFlags.Password);

        var selectedModel = OpenAiModelCatalog.Find(this.configuration.OpenAiModel);
        ImGui.SetNextItemWidth(-1);
        if (ImGui.BeginCombo("Model", selectedModel.DisplayName))
        {
            foreach (var option in OpenAiModelCatalog.Options)
            {
                var isSelected = string.Equals(option.Id, selectedModel.Id, StringComparison.OrdinalIgnoreCase);
                if (ImGui.Selectable(option.DisplayName, isSelected))
                {
                    this.configuration.OpenAiModel = option.Id;
                    this.configuration.Save();
                }

                if (ImGui.IsItemHovered())
                {
                    ImGui.SetTooltip($"{option.Id}\n{option.Notes}");
                }

                if (isSelected)
                {
                    ImGui.SetItemDefaultFocus();
                }
            }

            ImGui.EndCombo();
        }

        ImGui.TextWrapped(selectedModel.Notes);

        ImGui.SetNextItemWidth(180);
        ImGui.InputInt("Max output tokens", ref this.maxOutputTokens, 50, 100);
        this.maxOutputTokens = Math.Clamp(this.maxOutputTokens, 200, 6000);

        ImGui.Spacing();
        if (ImGui.Button("Save"))
        {
            this.configuration.OpenAiApiKey = this.apiKey.Trim();
            this.configuration.MaxOutputTokens = this.maxOutputTokens;
            this.configuration.Save();
        }

        ImGui.SameLine();
        if (ImGui.Button("Clear API key"))
        {
            this.apiKey = string.Empty;
            this.configuration.OpenAiApiKey = string.Empty;
            this.configuration.Save();
        }
    }
}
