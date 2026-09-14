#!/usr/bin/env python3
"""Validate local Markdown links and reject credential-shaped text."""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)")
SECRET_PATTERNS = (
    re.compile(r"-----BEGIN [A-Z ]+ PRIVATE KEY-----"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bAIza[0-9A-Za-z_-]{30,}\b"),
)
TEXT_SUFFIXES = {".md", ".txt", ".yml", ".yaml", ".json", ".js", ".ts", ".py", ".sh"}
FAKE_MARKERS = ("not-a-real", "fake", "placeholder", "example", "dummy")
LAB_INDEX = Path("_labs/README.md")
EXPECTED_LAB_LINKS = {
    "lab1.md",
    "lab2.md",
    "lab3.md",
    "lab4.md",
    "lab5.md",
    "lab6.md",
    "lab7-ec.md",
    "lab8-ec.md",
    "capstone.md",
}
EXPECTED_SUPPORT_LINKS = {
    "workshop-map.md",
    "instructor-runbook.md",
    "assessment.md",
    "assessment-answer-key.md",
    "supply-chain.md",
    "optional-coverage.md",
    "metrics-and-roi.md",
    "troubleshooting.md",
    "positioning.md",
}


def markdown_files() -> list[Path]:
    return sorted(ROOT.rglob("*.md"))


def check_markdown_links() -> list[str]:
    errors: list[str] = []
    for path in markdown_files():
        for match in MARKDOWN_LINK.finditer(path.read_text(encoding="utf-8")):
            target = match.group(1)
            if target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            target_path = (path.parent / target.split("#", 1)[0]).resolve()
            if not target_path.exists():
                errors.append(f"{path.relative_to(ROOT)}: missing local link {target}")
    return errors


def check_external_links() -> list[str]:
    errors: list[str] = []
    for path in markdown_files():
        for match in MARKDOWN_LINK.finditer(path.read_text(encoding="utf-8")):
            target = match.group(1)
            if not target.startswith(("http://", "https://")):
                continue
            parsed = urlparse(target)
            if not parsed.netloc or parsed.username or parsed.password:
                errors.append(f"{path.relative_to(ROOT)}: malformed external link {target}")
    return errors


def check_lab_index() -> list[str]:
    index = ROOT / LAB_INDEX
    if not index.exists():
        return [f"missing canonical lab index {LAB_INDEX}"]
    text = index.read_text(encoding="utf-8")
    linked_paths = {
        Path(match.group(1).split("#", 1)[0]).name
        for match in MARKDOWN_LINK.finditer(text)
        if not match.group(1).startswith(("http://", "https://", "#", "mailto:"))
    }
    errors: list[str] = []
    for expected in sorted(EXPECTED_LAB_LINKS | EXPECTED_SUPPORT_LINKS):
        if expected not in linked_paths:
            errors.append(f"{LAB_INDEX}: missing index entry for {expected}")
    return errors


def check_secret_like_content() -> list[str]:
    errors: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pattern in SECRET_PATTERNS:
            for match in pattern.finditer(text):
                context = text[max(0, match.start() - 80) : match.end() + 80].lower()
                if not any(marker in context for marker in FAKE_MARKERS):
                    errors.append(f"{path.relative_to(ROOT)}: secret-like content")
    return errors


def check_yaml() -> list[str]:
    ruby = shutil.which("ruby")
    if ruby is None:
        print("YAML validation skipped: Ruby is not installed; CI runs this check.")
        return []
    files = [str(path) for path in ROOT.rglob("*.yml")] + [
        str(path) for path in ROOT.rglob("*.yaml")
    ]
    result = subprocess.run(
        [ruby, "-e", "require 'yaml'; ARGV.each { |f| YAML.load_file(f) }", *files],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    if result.returncode:
        return [f"YAML validation failed: {result.stderr.strip()}"]
    return []


def main() -> int:
    errors = (
        check_markdown_links()
        + check_external_links()
        + check_lab_index()
        + check_secret_like_content()
        + check_yaml()
    )
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Documentation links, YAML, and secret-like content checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
