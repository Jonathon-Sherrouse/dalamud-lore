#!/usr/bin/env python
"""Look up FFXIV term definitions with one web-search LLM call per term.

The helper creates reviewable dictionary proposals. It does not modify
NpcDialogueLinks/terms.json.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


API_URL = "https://api.openai.com/v1/responses"
DEFAULT_MODEL = "gpt-5-mini"
TERM_LOOKUP_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "term": {"type": "string"},
        "definition": {"type": "string"},
        "aliases": {"type": "array", "items": {"type": "string"}},
        "category": {"type": "string"},
        "spoilerSensitivity": {"type": "string"},
        "sourcePatchOrRange": {"type": "string"},
        "lastVerifiedDate": {"type": "string"},
        "readyForDictionaryReview": {"type": "boolean"},
        "notes": {"type": "string"},
        "sourceUrls": {"type": "array", "items": {"type": "string"}},
    },
    "required": [
        "term",
        "definition",
        "aliases",
        "category",
        "spoilerSensitivity",
        "sourcePatchOrRange",
        "lastVerifiedDate",
        "readyForDictionaryReview",
        "notes",
        "sourceUrls",
    ],
    "additionalProperties": False,
}


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Research FFXIV terms and write reviewable dictionary proposals."
    )
    parser.add_argument(
        "terms",
        nargs="*",
        help="Terms to look up. Use --terms-file for larger batches.",
    )
    parser.add_argument(
        "--terms-file",
        type=Path,
        help="Text file with one term per line. Blank lines and # comments are ignored.",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("term-lookup-results.json"),
        help="Output JSON path. Defaults to term-lookup-results.json.",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"OpenAI model to use. Defaults to {DEFAULT_MODEL}.",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.0,
        help="Seconds to wait between term lookups.",
    )
    parser.add_argument(
        "--max-output-tokens",
        type=int,
        default=3000,
        help="Maximum output tokens per term lookup.",
    )

    args = parser.parse_args()
    api_key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not api_key:
        print("OPENAI_API_KEY is required.", file=sys.stderr)
        return 2

    terms = collect_terms(args.terms, args.terms_file)
    if not terms:
        print("Provide at least one term or --terms-file.", file=sys.stderr)
        return 2

    results: list[dict[str, Any]] = []
    for index, term in enumerate(terms, start=1):
        print(f"[{index}/{len(terms)}] Looking up {term}...", file=sys.stderr)
        result = lookup_term(
            api_key=api_key,
            model=args.model,
            term=term,
            max_output_tokens=args.max_output_tokens,
        )
        results.append(result)

        write_output(args.out, args.model, results)
        if args.delay > 0 and index < len(terms):
            time.sleep(args.delay)

    print(args.out)
    return 0


def collect_terms(cli_terms: list[str], terms_file: Path | None) -> list[str]:
    values: list[str] = []
    values.extend(cli_terms)

    if terms_file is not None:
        for line in terms_file.read_text(encoding="utf-8-sig").splitlines():
            stripped = line.strip()
            if stripped and not stripped.startswith("#"):
                values.append(stripped)

    terms: list[str] = []
    seen: set[str] = set()
    for value in values:
        term = value.strip()
        key = term.casefold()
        if term and key not in seen:
            seen.add(key)
            terms.append(term)

    return terms


def lookup_term(
    *,
    api_key: str,
    model: str,
    term: str,
    max_output_tokens: int,
) -> dict[str, Any]:
    payload = {
        "model": model,
        "instructions": "\n".join(
            [
                "You research Final Fantasy XIV terms for a local dictionary.",
                "Use web search for every term before answering.",
                "Prefer ffxiv.consolegameswiki.com for game terms, quests, NPCs, places, factions, and lore.",
                "Use other sources only when needed to resolve ambiguity or fill gaps.",
                "Be concise, neutral, spoiler-aware, and suitable for an in-game glossary.",
                "Do not invent facts, quest IDs, patch details, aliases, or source-backed claims.",
                "If the term is ambiguous or source quality is weak, mark readyForDictionaryReview as false.",
                "Include sourceUrls as direct URLs used to support the definition.",
                "If you cannot provide at least one source URL, mark readyForDictionaryReview as false.",
                "Return only JSON with this shape: "
                '{"term": string, "definition": string, "aliases": string[], '
                '"category": string, "spoilerSensitivity": string, '
                '"sourcePatchOrRange": string, "lastVerifiedDate": string, '
                '"readyForDictionaryReview": boolean, "notes": string, '
                '"sourceUrls": string[]}.',
            ]
        ),
        "input": f"Term: {term}",
        "max_output_tokens": max(300, min(max_output_tokens, 4000)),
        "reasoning": {"effort": "low"},
        "store": False,
        "tools": [{"type": "web_search"}],
        "tool_choice": "auto",
        "include": ["web_search_call.action.sources"],
        "text": {
            "format": {
                "type": "json_schema",
                "name": "term_lookup_result",
                "strict": True,
                "schema": TERM_LOOKUP_SCHEMA,
            },
        },
    }

    response = post_json(API_URL, api_key, payload)
    issue = response_issue(response)
    text = extract_output_text(response).strip()
    parsed = parse_json_object(text)
    sources = extract_sources(response)

    if parsed is None:
        notes = "Model did not return parseable JSON."
        if issue:
            notes += f" Response issue: {issue}."
        notes += f" Raw text: {text}"
        return {
            "term": term,
            "definition": "",
            "aliases": [],
            "category": "unknown",
            "spoilerSensitivity": "unknown",
            "sourcePatchOrRange": "",
            "lastVerifiedDate": today_iso(),
            "readyForDictionaryReview": False,
            "notes": notes,
            "sources": sources,
            "responseStatus": response.get("status") if isinstance(response, dict) else None,
            "outputTypes": output_types(response),
        }

    parsed.setdefault("term", term)
    parsed.setdefault("definition", "")
    parsed.setdefault("aliases", [])
    parsed.setdefault("category", "unknown")
    parsed.setdefault("spoilerSensitivity", "unknown")
    parsed.setdefault("sourcePatchOrRange", "")
    parsed.setdefault("lastVerifiedDate", today_iso())
    parsed.setdefault("readyForDictionaryReview", False)
    parsed.setdefault("notes", "")
    parsed.setdefault("sourceUrls", [])
    parsed = normalize_result_text(parsed)
    sources = merge_sources(sources, parsed.get("sourceUrls"))
    parsed["sources"] = sources
    if not sources:
        parsed["readyForDictionaryReview"] = False
        parsed["notes"] = append_note(
            str(parsed.get("notes", "")),
            "No source URLs were captured; validate manually before promotion.",
        )
    if issue:
        parsed["notes"] = append_note(str(parsed.get("notes", "")), f"Response issue: {issue}.")
        parsed["readyForDictionaryReview"] = False
    return parsed


def post_json(url: str, api_key: str, payload: dict[str, Any]) -> dict[str, Any]:
    body = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=90) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exception:
        detail = exception.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"OpenAI request failed ({exception.code}): {detail}") from exception


def extract_output_text(root: Any) -> str:
    if isinstance(root, dict) and isinstance(root.get("output_text"), str):
        return root["output_text"]

    parts: list[str] = []
    visit_for_text(root, parts)
    return "\n".join(parts)


def visit_for_text(value: Any, parts: list[str]) -> None:
    if isinstance(value, dict):
        text = value.get("text")
        value_type = value.get("type")
        if isinstance(text, str) and value_type in {"output_text", "text"}:
            parts.append(text)

        for child in value.values():
            visit_for_text(child, parts)
    elif isinstance(value, list):
        for child in value:
            visit_for_text(child, parts)


def parse_json_object(text: str) -> dict[str, Any] | None:
    try:
        value = json.loads(text)
        return value if isinstance(value, dict) else None
    except json.JSONDecodeError:
        pass

    match = re.search(r"\{.*\}", text, flags=re.DOTALL)
    if not match:
        return None

    try:
        value = json.loads(match.group(0))
    except json.JSONDecodeError:
        return None

    return value if isinstance(value, dict) else None


def response_issue(root: Any) -> str:
    if not isinstance(root, dict):
        return "Response body was not a JSON object"

    status = root.get("status")
    if status in {"incomplete", "failed", "cancelled"}:
        details = root.get("incomplete_details") or root.get("error") or ""
        return f"status={status} details={details}"

    if root.get("error"):
        return f"error={root['error']}"

    return ""


def output_types(root: Any) -> list[str]:
    if not isinstance(root, dict):
        return []

    output = root.get("output")
    if not isinstance(output, list):
        return []

    types: list[str] = []
    for item in output:
        if isinstance(item, dict):
            value = item.get("type")
            if isinstance(value, str):
                types.append(value)

    return types


def extract_sources(root: Any) -> list[dict[str, str]]:
    sources: list[dict[str, str]] = []
    seen: set[str] = set()
    visit_for_sources(root, sources, seen)
    return sources


def merge_sources(sources: list[dict[str, str]], source_urls: Any) -> list[dict[str, str]]:
    merged = list(sources)
    seen = {source["url"].casefold() for source in merged if source.get("url")}
    if not isinstance(source_urls, list):
        return merged

    for item in source_urls:
        if not isinstance(item, str):
            continue

        url = clean_source_url(item)
        if url and url.casefold() not in seen:
            seen.add(url.casefold())
            merged.append({"title": url, "url": url})

    return merged


def visit_for_sources(value: Any, sources: list[dict[str, str]], seen: set[str]) -> None:
    if isinstance(value, dict):
        url = value.get("url")
        title = value.get("title")
        looks_like_source = isinstance(url, str) and (
            value.get("type") == "url_citation" or isinstance(title, str)
        )
        if looks_like_source:
            clean_url = clean_source_url(url)
            if clean_url and clean_url.casefold() not in seen:
                seen.add(clean_url.casefold())
                sources.append({"title": str(title or clean_url), "url": clean_url})

        for child in value.values():
            visit_for_sources(child, sources, seen)
    elif isinstance(value, list):
        for child in value:
            visit_for_sources(child, sources, seen)


def clean_source_url(url: str) -> str:
    return (
        url.replace("?utm_source=openai", "")
        .replace("&utm_source=openai", "")
        .strip()
    )


def normalize_result_text(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: normalize_result_text(child) for key, child in value.items()}
    if isinstance(value, list):
        return [normalize_result_text(child) for child in value]
    if isinstance(value, str):
        return normalize_text(value)
    return value


def normalize_text(value: str) -> str:
    replacements = {
        "\u2018": "'",
        "\u2019": "'",
        "\u201C": '"',
        "\u201D": '"',
        "\u2013": "-",
        "\u2014": "-",
        "\u2011": "-",
        "\u00A0": " ",
    }
    for old, new in replacements.items():
        value = value.replace(old, new)
    return value


def append_note(notes: str, addition: str) -> str:
    notes = notes.strip()
    return f"{notes} {addition}".strip() if notes else addition


def write_output(path: Path, model: str, results: list[dict[str, Any]]) -> None:
    payload = {
        "createdAt": datetime.now(timezone.utc).isoformat(),
        "model": model,
        "results": results,
    }
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def today_iso() -> str:
    return datetime.now(timezone.utc).date().isoformat()


if __name__ == "__main__":
    raise SystemExit(main())
