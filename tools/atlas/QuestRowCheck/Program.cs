using System.Text.Json;
using Lumina;
using Lumina.Excel.Sheets;
using NpcDialogueLinks.Progress;

// Usage:
//   dotnet run --project tools/atlas/QuestRowCheck -- [--game <sqpack folder>] [--data <atlas.json>]
// Exit code 0 when every row exists in the English Quest sheet, is a main-scenario quest, fits the client's
// completed-quest range, and matches its authored title under QuestTitles.MatchesAuthored (milestones carry no title).
string? game = null;
var data = Path.Combine("NpcDialogueLinks", "atlas.json");
for (var i = 0; i + 1 < args.Length; i++)
{
    switch (args[i])
    {
        case "--game": game = args[++i]; break;
        case "--data": data = args[++i]; break;
    }
}

game ??= new[]
{
    @"C:\Program Files (x86)\SquareEnix\FINAL FANTASY XIV - A Realm Reborn\game\sqpack",
    @"C:\Program Files (x86)\Steam\steamapps\common\FINAL FANTASY XIV Online\game\sqpack",
}.FirstOrDefault(Directory.Exists);
if (game is null || !Directory.Exists(game))
{
    Console.Error.WriteLine("Could not find the game's sqpack folder. Pass it with --game <path to game/sqpack>.");
    return 2;
}

var sheet = new GameData(game, new LuminaOptions { PanicOnSheetChecksumMismatch = false }).GetExcelSheet<Quest>(Lumina.Data.Language.English)!;
using var doc = JsonDocument.Parse(File.ReadAllText(data));
int rows = 0, problems = 0;
foreach (var checkpoint in doc.RootElement.GetProperty("checkpoints").EnumerateArray())
{
    var id = checkpoint.GetProperty("id").GetString();
    var authored = checkpoint.TryGetProperty("questTitle", out var t) ? t.GetString() : null;
    foreach (var element in checkpoint.GetProperty("gameQuestIds").EnumerateArray())
    {
        rows++;
        var row = element.GetUInt32();
        string? problem = null;
        string? name = null;
        if (!QuestIdMapping.TryToClientId(row, 6008, out _) || !sheet.TryGetRow(row, out var quest))
        {
            problem = "not a quest row";
        }
        else
        {
            name = quest.Name.ExtractText();
            var category = quest.JournalGenre.ValueNullable?.JournalCategory.ValueNullable?.Name.ExtractText() ?? string.Empty;
            if (!category.Contains("Main Scenario", StringComparison.Ordinal))
            {
                problem = $"not a main-scenario quest ({category})";
            }
            else if (authored is not null && !QuestTitles.MatchesAuthored(row, authored, name))
            {
                problem = $"title mismatch: authored \"{authored}\"";
            }
        }

        if (problem is not null)
        {
            problems++;
            Console.WriteLine($"{id} {row} \"{name}\": {problem}");
        }
        else if (authored is null)
        {
            Console.WriteLine($"{id} {row} milestone quest \"{name}\"");
        }
    }
}

Console.WriteLine($"{rows} rows checked, {problems} problem(s).");
return problems == 0 ? 0 : 1;
