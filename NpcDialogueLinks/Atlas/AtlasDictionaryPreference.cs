namespace NpcDialogueLinks.Atlas;

internal enum AtlasDictionaryPreference
{
    Unacknowledged,
    Enabled,
    Disabled,
}

internal static class AtlasDictionaryOptions
{
    public const string Label = "Dictionary previews";
    public const string Warning = "Dictionary definitions can reveal later story events, even when the Atlas is set to an earlier checkpoint.";
    public const string Enable = "Enable previews";
    public const string Cancel = "Cancel";
    public const string CloseEntry = "Close";

    public static AtlasDictionaryPreference Toggle(AtlasDictionaryPreference current)
        => current switch
        {
            AtlasDictionaryPreference.Enabled => AtlasDictionaryPreference.Disabled,
            AtlasDictionaryPreference.Disabled => AtlasDictionaryPreference.Enabled,
            _ => AtlasDictionaryPreference.Unacknowledged,
        };

    public static AtlasDictionaryPreference Confirm(AtlasDictionaryPreference current, bool warningOpen)
        => current == AtlasDictionaryPreference.Unacknowledged && warningOpen ? AtlasDictionaryPreference.Enabled : current;
}
