using System.Buffers.Binary;
using System.IO.Compression;
using System.Text.Json;
using Lumina;
using Lumina.Data.Files;

// Fills the local Atlas viewer's portrait cache from your own FFXIV install (NDL-011), so the viewer draws the same
// portraits as the in-game window. Usage, from the repository root:
//   dotnet run --project tools/atlas/PortraitCache -- [--game <sqpack folder>] [--data <atlas.json>] [--out <folder>]
// The images stay on this machine, outside the repository; they are never committed or packaged.

var data = Path.Combine("NpcDialogueLinks", "atlas.json");
string? game = Environment.GetEnvironmentVariable("FFXIV_SQPACK");
var output = Path.Combine(
    Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData), "NpcDialogueLinks.AtlasViewer", "portraits");
for (var i = 0; i + 1 < args.Length; i++)
{
    switch (args[i])
    {
        case "--game": game = args[++i]; break;
        case "--data": data = args[++i]; break;
        case "--out": output = args[++i]; break;
    }
}

game ??= DefaultSqpack();
if (game is null || !Directory.Exists(game))
{
    Console.Error.WriteLine("Could not find the game's sqpack folder. Pass it with --game <path to game/sqpack>.");
    return 1;
}

if (!File.Exists(data))
{
    Console.Error.WriteLine($"Atlas data not found at {data}. Run from the repository root or pass --data.");
    return 1;
}

var icons = new SortedSet<uint>();
using (var document = JsonDocument.Parse(File.ReadAllBytes(data)))
{
    foreach (var entity in document.RootElement.GetProperty("entities").EnumerateArray())
    {
        if (entity.TryGetProperty("portrait", out var portrait) && portrait.TryGetProperty("gameIcon", out var icon))
        {
            icons.Add(icon.GetUInt32());
        }
    }
}

Directory.CreateDirectory(output);
var gameData = new GameData(game, new LuminaOptions { PanicOnSheetChecksumMismatch = false });
var written = 0;
foreach (var icon in icons)
{
    // The same high-resolution icon Dalamud loads in game, falling back to the standard one.
    var folder = icon / 1000 * 1000;
    var texture = gameData.GetFile<TexFile>($"ui/icon/{folder:D6}/{icon:D6}_hr1.tex")
        ?? gameData.GetFile<TexFile>($"ui/icon/{folder:D6}/{icon:D6}.tex");
    if (texture is null)
    {
        Console.Error.WriteLine($"Icon {icon} is not in this game install; the viewer will draw its category shape.");
        continue;
    }

    File.WriteAllBytes(Path.Combine(output, $"{icon}.png"), Png(texture.Header.Width, texture.Header.Height, texture.ImageData));
    written++;
}

Console.WriteLine($"Wrote {written} of {icons.Count} portraits to {output}");
return written == icons.Count ? 0 : 2;

static string? DefaultSqpack()
{
    var candidates = OperatingSystem.IsMacOS()
        ? new[] { Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.UserProfile), "Library", "Application Support", "XIV on Mac", "ffxiv", "game", "sqpack") }
        : new[]
        {
            @"C:\Program Files (x86)\SquareEnix\FINAL FANTASY XIV - A Realm Reborn\game\sqpack",
            @"C:\Program Files (x86)\Steam\steamapps\common\FINAL FANTASY XIV Online\game\sqpack",
        };
    return candidates.FirstOrDefault(Directory.Exists);
}

// A minimal PNG encoder for 8-bit RGBA, from Lumina's BGRA pixels.
static byte[] Png(int width, int height, byte[] bgra)
{
    var raw = new byte[height * ((width * 4) + 1)];
    for (var y = 0; y < height; y++)
    {
        var row = y * ((width * 4) + 1);
        for (var x = 0; x < width; x++)
        {
            var source = ((y * width) + x) * 4;
            var target = row + 1 + (x * 4);
            raw[target] = bgra[source + 2];
            raw[target + 1] = bgra[source + 1];
            raw[target + 2] = bgra[source];
            raw[target + 3] = bgra[source + 3];
        }
    }

    using var compressed = new MemoryStream();
    using (var zlib = new ZLibStream(compressed, CompressionLevel.Optimal, leaveOpen: true))
    {
        zlib.Write(raw);
    }

    var header = new byte[13];
    BinaryPrimitives.WriteInt32BigEndian(header, width);
    BinaryPrimitives.WriteInt32BigEndian(header.AsSpan(4), height);
    header[8] = 8; // bit depth
    header[9] = 6; // RGBA

    using var png = new MemoryStream();
    png.Write(new byte[] { 0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A });
    Chunk(png, "IHDR", header);
    Chunk(png, "IDAT", compressed.ToArray());
    Chunk(png, "IEND", Array.Empty<byte>());
    return png.ToArray();
}

static void Chunk(Stream stream, string type, byte[] body)
{
    var length = new byte[4];
    BinaryPrimitives.WriteInt32BigEndian(length, body.Length);
    stream.Write(length);
    var typeBytes = System.Text.Encoding.ASCII.GetBytes(type);
    stream.Write(typeBytes);
    stream.Write(body);
    var crc = new byte[4];
    BinaryPrimitives.WriteUInt32BigEndian(crc, Crc32(typeBytes, body));
    stream.Write(crc);
}

static uint Crc32(byte[] type, byte[] body)
{
    var crc = 0xFFFFFFFFu;
    foreach (var b in type.Concat(body))
    {
        crc ^= b;
        for (var k = 0; k < 8; k++)
        {
            crc = (crc & 1) != 0 ? 0xEDB88320u ^ (crc >> 1) : crc >> 1;
        }
    }

    return ~crc;
}
