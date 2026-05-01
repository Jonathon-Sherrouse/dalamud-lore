using Dalamud.Game.Addon.Lifecycle;
using Dalamud.Game.Addon.Lifecycle.AddonArgTypes;
using Dalamud.Plugin.Services;
using FFXIVClientStructs.FFXIV.Client.UI;
using FFXIVClientStructs.FFXIV.Component.GUI;

namespace NpcDialogueLinks;

internal sealed class DialogueCapture : IDisposable
{
    private readonly IAddonLifecycle addonLifecycle;
    private readonly Action<string> onDialogueChanged;

    private string lastDialogue = string.Empty;

    public DialogueCapture(IAddonLifecycle addonLifecycle, Action<string> onDialogueChanged)
    {
        this.addonLifecycle = addonLifecycle;
        this.onDialogueChanged = onDialogueChanged;

        this.addonLifecycle.RegisterListener(AddonEvent.PostUpdate, "Talk", this.OnTalkUpdated);
    }

    public void Dispose()
    {
        this.addonLifecycle.UnregisterListener(this.OnTalkUpdated);
    }

    private unsafe void OnTalkUpdated(AddonEvent eventType, AddonArgs args)
    {
        _ = eventType;

        if (args.Addon.IsNull)
        {
            return;
        }

        var dialogueAddon = (AddonTalk*)args.Addon.Address;
        var dialogue = ReadDialogue(dialogueAddon);

        if (string.IsNullOrWhiteSpace(dialogue) || string.Equals(dialogue, this.lastDialogue, StringComparison.Ordinal))
        {
            return;
        }

        this.lastDialogue = dialogue;
        this.onDialogueChanged(dialogue);
    }

    private static unsafe string ReadDialogue(AddonTalk* dialogueAddon)
    {
        var bestText = string.Empty;

        var textNodes = stackalloc AtkTextNode*[5]
        {
            dialogueAddon->AtkTextNode220,
            dialogueAddon->AtkTextNode228,
            dialogueAddon->AtkTextNode238,
            dialogueAddon->AtkTextNode240,
            dialogueAddon->AtkTextNode248,
        };

        for (var index = 0; index < 5; index++)
        {
            var text = ReadNodeText(textNodes[index]);
            if (text.Length > bestText.Length)
            {
                bestText = text;
            }
        }

        return bestText;
    }

    private static unsafe string ReadNodeText(AtkTextNode* textNode)
    {
        if (textNode == null)
        {
            return string.Empty;
        }

        var rawText = textNode->NodeText.ToString();
        if (string.IsNullOrWhiteSpace(rawText))
        {
            return string.Empty;
        }

        return rawText
            .ReplaceLineEndings(" ")
            .Replace("  ", " ", StringComparison.Ordinal)
            .Trim();
    }
}
