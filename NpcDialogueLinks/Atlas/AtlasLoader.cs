using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace NpcDialogueLinks.Atlas;

public enum AtlasErrorCode
{
    MissingFile,
    ReadFailed,
    TooLarge,
    MalformedJson,
    UnsupportedSchemaVersion,
    BoundsExceeded,
    InvalidField,
    DuplicateId,
    UnknownReference,
    InvalidInterval,
    OverlappingPresentation,
    VisibilityGap,
    EndpointNotVisible,
    DuplicateRelationship,
    ReverseSymmetricDuplicate,
    OptionalSpansMainBoundary,
    OptionalEndsEarly,
    CitationTooNew,
    CitationScopeMismatch,
    InconsistentCitation,
    UnreviewedRecord,
    InvalidArc,
    CastTooLarge,
    EndCitationOutOfRange,
    InternalError,
}

public sealed record AtlasError(AtlasErrorCode Code, string Path, string Message);

public sealed class AtlasLoadResult
{
    private AtlasLoadResult(AtlasDataset? dataset, IReadOnlyList<AtlasError> errors)
    {
        Dataset = dataset;
        Errors = errors;
    }

    /// <summary>Non-null only when <see cref="Success"/> is true. A failed load never yields a usable graph.</summary>
    public AtlasDataset? Dataset { get; }

    public IReadOnlyList<AtlasError> Errors { get; }

    public bool Success => Dataset is not null;

    internal static AtlasLoadResult Ok(AtlasDataset dataset) => new(dataset, Array.Empty<AtlasError>());

    internal static AtlasLoadResult Fail(IReadOnlyList<AtlasError> errors) => new(null, errors);

    internal static AtlasLoadResult Fail(AtlasErrorCode code, string path, string message) =>
        new(null, new[] { new AtlasError(code, path, message) });
}

/// <summary>Loads and validates Atlas data. Never throws; failures are returned as structured errors.</summary>
public static class AtlasLoader
{
    public const int SupportedSchemaVersion = 2;
    public const int MaxFileBytes = 1024 * 1024;
    public const int MaxCheckpoints = 128;
    public const int MaxEntities = 64;
    public const int MaxRelationships = 256;
    public const int MaxRelationshipTypes = 32;
    public const int MaxArcs = 16;

    private static readonly JsonSerializerOptions SerializerOptions = new()
    {
        PropertyNamingPolicy = JsonNamingPolicy.CamelCase,
        UnmappedMemberHandling = JsonUnmappedMemberHandling.Disallow,
        ReadCommentHandling = JsonCommentHandling.Disallow,
        AllowTrailingCommas = false,
        AllowDuplicateProperties = false,
        MaxDepth = 16,
    };

    private static readonly JsonDocumentOptions DocumentOptions = new()
    {
        CommentHandling = JsonCommentHandling.Disallow,
        AllowTrailingCommas = false,
        AllowDuplicateProperties = false,
        MaxDepth = 16,
    };

    public static AtlasLoadResult LoadFile(string path, AtlasValidationMode mode)
    {
        try
        {
            var info = new FileInfo(path);
            if (!info.Exists)
            {
                return AtlasLoadResult.Fail(AtlasErrorCode.MissingFile, "$", "Atlas data file was not found.");
            }

            if (info.Length > MaxFileBytes)
            {
                return AtlasLoadResult.Fail(AtlasErrorCode.TooLarge, "$", $"Atlas data exceeds {MaxFileBytes} bytes.");
            }

            return LoadUtf8(File.ReadAllBytes(path), mode);
        }
        catch (Exception ex) when (ex is IOException or UnauthorizedAccessException or ArgumentException or NotSupportedException or System.Security.SecurityException)
        {
            return AtlasLoadResult.Fail(AtlasErrorCode.ReadFailed, "$", $"Atlas data could not be read: {ex.GetType().Name}.");
        }
    }

    public static AtlasLoadResult LoadJson(string json, AtlasValidationMode mode)
    {
        if (json is null)
        {
            return AtlasLoadResult.Fail(AtlasErrorCode.MalformedJson, "$", "Atlas data is empty.");
        }

        if (json.Length > MaxFileBytes)
        {
            return AtlasLoadResult.Fail(AtlasErrorCode.TooLarge, "$", $"Atlas data exceeds {MaxFileBytes} bytes.");
        }

        return LoadUtf8(Encoding.UTF8.GetBytes(json), mode);
    }

    public static AtlasLoadResult LoadUtf8(byte[] utf8Json, AtlasValidationMode mode)
    {
        try
        {
            return LoadCore(utf8Json, mode);
        }
        catch (Exception ex)
        {
            // Boundary guarantee: invalid Atlas data must never escape as an exception.
            return AtlasLoadResult.Fail(AtlasErrorCode.InternalError, "$", $"Atlas data could not be loaded: {ex.GetType().Name}.");
        }
    }

    private static AtlasLoadResult LoadCore(byte[] utf8Json, AtlasValidationMode mode)
    {
        if (utf8Json is null || utf8Json.Length == 0)
        {
            return AtlasLoadResult.Fail(AtlasErrorCode.MalformedJson, "$", "Atlas data is empty.");
        }

        if (utf8Json.Length > MaxFileBytes)
        {
            return AtlasLoadResult.Fail(AtlasErrorCode.TooLarge, "$", $"Atlas data exceeds {MaxFileBytes} bytes.");
        }

        // Read the version first so a future schema reports as unsupported rather than malformed.
        try
        {
            using var document = JsonDocument.Parse(utf8Json, DocumentOptions);
            if (document.RootElement.ValueKind != JsonValueKind.Object)
            {
                return AtlasLoadResult.Fail(AtlasErrorCode.MalformedJson, "$", "Atlas data must be a JSON object.");
            }

            if (!document.RootElement.TryGetProperty("schemaVersion", out var version)
                || version.ValueKind != JsonValueKind.Number
                || !version.TryGetInt32(out var versionNumber))
            {
                return AtlasLoadResult.Fail(AtlasErrorCode.UnsupportedSchemaVersion, "$.schemaVersion", "schemaVersion is missing or not an integer.");
            }

            if (versionNumber != SupportedSchemaVersion)
            {
                return AtlasLoadResult.Fail(AtlasErrorCode.UnsupportedSchemaVersion, "$.schemaVersion", $"schemaVersion {versionNumber} is not supported; expected {SupportedSchemaVersion}.");
            }
        }
        catch (JsonException ex)
        {
            return AtlasLoadResult.Fail(AtlasErrorCode.MalformedJson, "$", $"Atlas data is not valid JSON: {ex.Message}");
        }

        AtlasFileDto? file;
        try
        {
            file = JsonSerializer.Deserialize<AtlasFileDto>(utf8Json, SerializerOptions);
        }
        catch (JsonException ex)
        {
            return AtlasLoadResult.Fail(AtlasErrorCode.MalformedJson, ex.Path ?? "$", $"Atlas data does not match schema v2: {ex.Message}");
        }

        if (file is null)
        {
            return AtlasLoadResult.Fail(AtlasErrorCode.MalformedJson, "$", "Atlas data is null.");
        }

        return AtlasValidator.Build(file, mode);
    }
}

// JSON transfer objects. Everything is nullable so the validator reports missing fields precisely.
internal sealed class AtlasFileDto
{
    public int? SchemaVersion { get; set; }
    public List<AtlasCheckpointDto?>? Checkpoints { get; set; }
    public List<AtlasRelationshipTypeDto?>? RelationshipTypes { get; set; }
    public List<AtlasEntityDto?>? Entities { get; set; }
    public List<AtlasRelationshipDto?>? Relationships { get; set; }
    public List<AtlasArcDto?>? Arcs { get; set; }
}

internal sealed class AtlasArcDto
{
    public string? Id { get; set; }
    public string? EntityId { get; set; }
    public string? FirstStep { get; set; }
    public string? LastStep { get; set; }
}

internal sealed class AtlasCheckpointDto
{
    public string? Id { get; set; }
    public string? Label { get; set; }
    public bool? Milestone { get; set; }
    public string? QuestTitle { get; set; }
    public bool? ContiguousWithPrevious { get; set; }
    public List<int?>? GameQuestIds { get; set; }
}

internal sealed class AtlasRelationshipTypeDto
{
    public string? Id { get; set; }
    public string? OutgoingLabel { get; set; }
    public string? IncomingLabel { get; set; }
    public bool? Symmetric { get; set; }
}

internal sealed class AtlasEntityDto
{
    public string? Id { get; set; }
    public string? Category { get; set; }
    public AtlasPortraitDto? Portrait { get; set; }
    public List<AtlasPresentationDto?>? Presentations { get; set; }
}

internal sealed class AtlasPortraitDto
{
    public uint? GameIcon { get; set; }
    public AtlasCropDto? Crop { get; set; }
    public string? Review { get; set; }
}

internal sealed class AtlasCropDto
{
    public double? X { get; set; }
    public double? Y { get; set; }
    public double? Size { get; set; }
}

internal sealed class AtlasPresentationDto
{
    public string? ValidFrom { get; set; }
    public string? ValidUntil { get; set; }
    public string? Scope { get; set; }
    public string? Name { get; set; }
    public List<string?>? Aliases { get; set; }
    public string? Summary { get; set; }
    public List<AtlasCitationDto?>? Citations { get; set; }
    public string? Review { get; set; }
}

internal sealed class AtlasCitationDto
{
    public string? Title { get; set; }
    public string? Url { get; set; }
    public string? AvailableAt { get; set; }
    public string? Scope { get; set; }
}

internal sealed class AtlasRelationshipDto
{
    public string? Id { get; set; }
    public string? Source { get; set; }
    public string? Type { get; set; }
    public string? Target { get; set; }
    public string? ValidFrom { get; set; }
    public string? ValidUntil { get; set; }
    public string? Scope { get; set; }
    public List<AtlasCitationDto?>? Citations { get; set; }
    public List<AtlasCitationDto?>? EndCitations { get; set; }
    public string? Review { get; set; }
}
