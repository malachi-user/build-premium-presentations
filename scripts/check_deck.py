#!/usr/bin/env python3
"""Dependency-free structural, security (SRI/secrets), word-budget, and zero-AI-tell preflight for a Reveal.js presentation."""

from __future__ import annotations

import argparse
import html as html_lib
import re
import sys
from pathlib import Path

SLIDE_BODY_WORD_LIMIT = 30

CHECKS = {
    "doctype": re.compile(r"<!doctype html>", re.I),
    "language": re.compile(r"<html[^>]+lang=[\"'][^\"']+[\"']", re.I),
    "direction": re.compile(r"<html[^>]+dir=[\"'](?:rtl|ltr)[\"']", re.I),
    "viewport": re.compile(r"name=[\"']viewport[\"']", re.I),
    "reveal": re.compile(r"Reveal\.initialize\s*\("),
    "slides": re.compile(r"class=[\"'][^\"']*slides"),
    "reduced_motion": re.compile(r"prefers-reduced-motion"),
}

UNVERIFIED_RE = re.compile(r"\[(?:לאמת|להשלים|VERIFY|COMPLETE|TODO)[^\]]*\]", re.I)
TRAILING_ARROW_RE = re.compile(r"[→←↗↘➜➔]\s*$", re.M)
WORD_RE = re.compile(r"[\w\u0590-\u05FF]+", re.U)


def strip_tags(fragment: str) -> str:
    cleaned = re.sub(r"<!--.*?-->", " ", fragment, flags=re.S)
    cleaned = re.sub(r"<(?:script|style|svg|aside)\b[^>]*>.*?</(?:script|style|svg|aside)>", " ", cleaned, flags=re.I | re.S)
    cleaned = re.sub(r"<[^>]+>", " ", cleaned)
    return html_lib.unescape(cleaned)


def strip_headings_and_notes(section_html: str) -> str:
    body = re.sub(r"<h[12]\b[^>]*>.*?</h[12]>", " ", section_html, flags=re.I | re.S)
    body = re.sub(r"<div\b[^>]*class=[\"'][^\"']*(?:notes|credit)[^\"']*[\"'][^>]*>.*?</div>", " ", body, flags=re.I | re.S)
    return strip_tags(body)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("deck", type=Path)
    args = parser.parse_args()
    root = args.deck.resolve()
    index_path = root / "index.html"
    if not index_path.is_file():
        print("ERROR: index.html not found", file=sys.stderr)
        return 2

    index_html = index_path.read_text(encoding="utf-8", errors="replace")
    combined = "\n".join(
        p.read_text(encoding="utf-8", errors="replace")
        for p in [index_path, *sorted(root.glob("*.css")), *sorted(root.glob("*.js"))]
    )
    errors: list[str] = []
    warnings: list[str] = []

    for name, pattern in CHECKS.items():
        if not pattern.search(combined):
            errors.append(f"missing {name}")

    ids = re.findall(r"<section\b[^>]*\bid=[\"']([^\"']+)[\"']", index_html, re.I)
    if not ids:
        errors.append("slides need stable section IDs")
    duplicates = sorted({item for item in ids if ids.count(item) > 1})
    if duplicates:
        errors.append("duplicate slide IDs: " + ", ".join(duplicates))

    sections = re.findall(r"(<section\b([^>]*)>(.*?)</section>)", index_html, re.I | re.S)
    missing_time = sum("data-time-hint" not in attrs for _, attrs, _ in sections)
    if missing_time:
        warnings.append(f"{missing_time} slide(s) lack data-time-hint")

    for idx, (_full, attrs, inner) in enumerate(sections, start=1):
        sid_match = re.search(r"\bid=[\"']([^\"']+)[\"']", attrs, re.I)
        label = sid_match.group(1) if sid_match else f"#{idx}"
        visible_text = strip_tags(inner)
        if "—" in visible_text or "–" in visible_text:
            errors.append(f"slide '{label}' contains em/en-dash AI tell (—/–) in visible text")
        if "·" in visible_text:
            errors.append(f"slide '{label}' contains middle-dot AI tell (·) in visible text")
        if TRAILING_ARROW_RE.search(visible_text):
            errors.append(f"slide '{label}' contains trailing arrow AI tell in visible text")
        unverified = UNVERIFIED_RE.search(visible_text)
        if unverified:
            errors.append(f"slide '{label}' contains unresolved verification marker: {unverified.group(0)}")

        body_text = strip_headings_and_notes(inner)
        body_words = len(WORD_RE.findall(body_text))
        if body_words > SLIDE_BODY_WORD_LIMIT:
            warnings.append(
                f"slide '{label}' body has {body_words} words (target <= {SLIDE_BODY_WORD_LIMIT} words; tighten or split)"
            )

    for tag_match in re.finditer(r"<(?:script|link)\b[^>]+>", index_html, re.I):
        tag = tag_match.group(0)
        url_match = re.search(r"(?:src|href)=[\"'](https?://cdn\.jsdelivr\.net/[^\"']+)[\"']", tag, re.I)
        if url_match and "integrity=" not in tag.lower():
            warnings.append(f"CDN resource missing SRI integrity attribute: {url_match.group(1)}")

    refs = re.findall(r"(?:src|href)=[\"']([^\"'#?]+)", index_html, re.I)
    for ref in refs:
        if re.match(r"(?:https?:|data:|mailto:|tel:)", ref, re.I):
            continue
        candidate = (root / ref).resolve()
        try:
            candidate.relative_to(root)
        except ValueError:
            errors.append(f"asset escapes deck root: {ref}")
            continue
        if not candidate.exists():
            errors.append(f"missing local asset: {ref}")

    forbidden = re.compile(r"(?:api[_-]?key|secret|token)\s*[:=]\s*[\"'][^\"']{8,}", re.I)
    if forbidden.search(combined):
        errors.append("possible embedded secret")

    for item in warnings:
        print(f"WARN: {item}")
    for item in errors:
        print(f"ERROR: {item}")
    if errors:
        return 1
    print(f"OK: {len(ids)} slides passed structural and zero-AI-tell preflight")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
