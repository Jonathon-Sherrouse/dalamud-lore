#!/usr/bin/env python
"""Create a reviewable Lore Explain draft from an exported request.

This helper is intentionally deterministic for now. It turns a plugin-exported
request into a Markdown artifact that a human or LLM-backed workflow can fill in
with researched, cited explanation details.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create a Lore Explain Markdown draft from a request JSON file."
    )
    parser.add_argument("request", type=Path, help="Path to a Lore Explain request JSON file.")
    parser.add_argument(
        "--dictionary",
        type=Path,
        default=Path("NpcDialogueLinks") / "terms.json",
        help="Path to terms.json for local known-term context.",
    )
    parser.add_argument(
        "--out",
        type=Path,
        help="Output Markdown path. Defaults to the request path with a .md extension.",
    )

    args = parser.parse_args()
    request = load_json(args.request)
    dictionary = load_dictionary(args.dictionary)
    output_path = args.out or args.request.with_suffix(".md")

    markdown = build_markdown(request, dictionary)
    output_path.write_text(markdown, encoding="utf-8")
    print(output_path)
    return 0


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8-sig") as handle:
        value = json.load(handle)

    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object.")

    return value


def load_dictionary(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}

    with path.open("r", encoding="utf-8") as handle:
        raw = json.load(handle)

    if not isinstance(raw, dict):
        return {}

    entries: dict[str, str] = {}
    for canonical_name, value in raw.items():
        if isinstance(value, str):
            entries[canonical_name] = value.strip()
            continue

        if isinstance(value, dict):
            definition = value.get("definition")
            if isinstance(definition, str):
                entries[canonical_name] = definition.strip()

            aliases = value.get("aliases")
            if isinstance(aliases, list):
                for alias in aliases:
                    if isinstance(alias, str) and isinstance(definition, str):
                        entries[alias] = definition.strip()

    return entries


def build_markdown(request: dict[str, Any], dictionary: dict[str, str]) -> str:
    dialogue = str(request.get("dialogue", "")).strip()
    question = str(request.get("question", "")).strip()
    source = str(request.get("source", "unknown")).strip()
    created_at = str(request.get("createdAt", "unknown")).strip()
    known_terms = normalize_terms(request.get("knownTerms"))

    lines = [
        "# Lore Explain Draft",
        "",
        f"- Source: `{source}`",
        f"- Created: `{created_at}`",
        "",
        "## Dialogue",
        "",
        blockquote(dialogue or "(missing dialogue)"),
        "",
        "## User Question",
        "",
        question or "(none provided)",
        "",
        "## Short Explanation",
        "",
        "Research and summarize what this passage means in 2-5 plain-language sentences. If a user question is provided, answer it directly before adding broader context.",
        "",
        "## Relevant Context",
        "",
    ]

    if known_terms:
        for term in known_terms:
            definition = dictionary.get(term, "").strip()
            lines.extend(
                [
                    f"### {term}",
                    "",
                    f"- Local dictionary: {definition or '(no local dictionary entry found)'}",
                    "- Why it matters here: TODO",
                    "- Sources: TODO",
                    "",
                ]
            )
    else:
        lines.extend(
            [
                "No local dictionary terms were detected. Add only context that is necessary to understand the passage.",
                "",
            ]
        )

    lines.extend(
        [
            "## Dictionary Proposals",
            "",
            "Add proposed entries only after research. Do not paste unsourced model output into `terms.json`.",
            "",
            "```json",
            "[]",
            "```",
            "",
            "## Review Notes",
            "",
            "- Source quality or conflicts: TODO",
            "- Spoiler sensitivity: TODO",
            "- Ready for dictionary review: no",
            "",
        ]
    )

    return "\n".join(lines)


def normalize_terms(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []

    terms: list[str] = []
    seen: set[str] = set()
    for item in value:
        term = str(item).strip()
        key = term.casefold()
        if term and key not in seen:
            seen.add(key)
            terms.append(term)

    return terms


def blockquote(value: str) -> str:
    return "\n".join(f"> {line}" for line in value.splitlines())


if __name__ == "__main__":
    raise SystemExit(main())
