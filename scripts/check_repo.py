#!/usr/bin/env python3
"""Run deterministic structural checks for the LPIC-1 study repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_FILES = sorted(ROOT.rglob("*.md"))
OBJECTIVES = [
    "101.1", "101.2", "101.3",
    "102.1", "102.2", "102.3", "102.4", "102.5", "102.6",
    "103.1", "103.2", "103.3", "103.4", "103.5", "103.6", "103.7", "103.8",
    "104.1", "104.2", "104.3", "104.5", "104.6", "104.7",
    "105.1", "105.2",
    "106.1", "106.2", "106.3",
    "107.1", "107.2", "107.3",
    "108.1", "108.2", "108.3", "108.4",
    "109.1", "109.2", "109.3", "109.4",
    "110.1", "110.2", "110.3",
]
WEIGHTS = {
    "101.1": 2, "101.2": 3, "101.3": 3,
    "102.1": 2, "102.2": 2, "102.3": 1, "102.4": 3, "102.5": 3, "102.6": 1,
    "103.1": 4, "103.2": 2, "103.3": 4, "103.4": 4, "103.5": 4, "103.6": 2,
    "103.7": 3, "103.8": 3,
    "104.1": 2, "104.2": 2, "104.3": 3, "104.5": 3, "104.6": 2, "104.7": 2,
    "105.1": 4, "105.2": 4,
    "106.1": 2, "106.2": 1, "106.3": 1,
    "107.1": 5, "107.2": 4, "107.3": 3,
    "108.1": 3, "108.2": 4, "108.3": 3, "108.4": 2,
    "109.1": 4, "109.2": 4, "109.3": 4, "109.4": 2,
    "110.1": 3, "110.2": 3, "110.3": 4,
}


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def numbered_items(path: Path) -> list[int]:
    return [
        int(match.group(1))
        for match in re.finditer(r"(?m)^(\d+)\.\s", path.read_text(encoding="utf-8"))
    ]


def mock_objective_counts(path: Path) -> dict[str, int]:
    text = path.read_text(encoding="utf-8")
    headings = list(re.finditer(r"(?m)^### Objective (\d{3}\.\d) ", text))
    counts: dict[str, int] = {}
    for index, heading in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        section = text[heading.end():end]
        counts[heading.group(1)] = len(re.findall(r"(?m)^\d+\.\s", section))
    return counts


def check_relative_links(errors: list[str]) -> None:
    pattern = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
    for path in MARKDOWN_FILES:
        text = path.read_text(encoding="utf-8")
        for raw_target in pattern.findall(text):
            raw_target = raw_target.strip()
            if raw_target.startswith(("http://", "https://", "mailto:")):
                continue
            target, _, fragment = raw_target.partition("#")
            destination = path.resolve() if not target else (path.parent / target).resolve()
            if not destination.exists():
                fail(f"broken relative link: {path.relative_to(ROOT)} -> {raw_target}", errors)
                continue
            if fragment and destination.suffix == ".md":
                headings = destination.read_text(encoding="utf-8")
                anchors = {
                    github_anchor(match.group(1))
                    for match in re.finditer(r"(?m)^#{1,6} +(.*)$", headings)
                }
                if fragment not in anchors:
                    fail(
                        f"broken relative anchor: {path.relative_to(ROOT)} -> {raw_target}",
                        errors,
                    )


def github_anchor(heading: str) -> str:
    """Return the GitHub-style slug used by headings in this repository."""
    heading = re.sub(r"[`*_~]", "", heading.strip().lower())
    heading = re.sub(r"[^\w\- ]", "", heading)
    return re.sub(r" +", "-", heading)


def main() -> int:
    errors: list[str] = []

    chapter_text = "\n".join(
        path.read_text(encoding="utf-8") for path in sorted((ROOT / "docs").glob("1*.md"))
    )
    found_objectives = set(re.findall(r"(?m)^## (\d{3}\.\d)\b", chapter_text))
    expected_objectives = set(OBJECTIVES)
    if found_objectives != expected_objectives:
        fail(
            "objective headings differ: "
            f"missing={sorted(expected_objectives - found_objectives)}, "
            f"unexpected={sorted(found_objectives - expected_objectives)}",
            errors,
        )

    worked_paths = sorted((ROOT / "worked-examples").glob("1*.md"))
    worked_text = "\n".join(path.read_text(encoding="utf-8") for path in worked_paths)
    worked_objectives = set(re.findall(r"(?m)^## (\d{3}\.\d)\b", worked_text))
    if worked_objectives != expected_objectives:
        fail(
            "worked-example objectives differ: "
            f"missing={sorted(expected_objectives - worked_objectives)}, "
            f"unexpected={sorted(worked_objectives - expected_objectives)}",
            errors,
        )
    worked_examples = len(re.findall(r"(?m)^### Worked example \d+:", worked_text))
    explanations = len(re.findall(r"(?m)^\*\*Line-by-line explanation:\*\*$", worked_text))
    verification_notes = len(re.findall(r"(?m)^\*\*What to verify:\*\*", worked_text))
    if worked_examples != 126:
        fail(f"expected 126 worked examples, found {worked_examples}", errors)
    if explanations != worked_examples:
        fail(
            f"expected one line-by-line explanation per example, found {explanations}",
            errors,
        )
    if verification_notes != worked_examples:
        fail(
            f"expected one verification note per example, found {verification_notes}",
            errors,
        )

    matrix = (ROOT / "OBJECTIVES.md").read_text(encoding="utf-8")
    for objective in OBJECTIVES:
        if f"**{objective}**" not in matrix:
            fail(f"objective missing from matrix: {objective}", errors)

    for exam in ("101", "102"):
        mock_path = ROOT / "exercises" / f"mock-{exam}.md"
        questions = numbered_items(mock_path)
        answers = numbered_items(ROOT / "exercises" / f"mock-{exam}-answers.md")
        expected = list(range(1, 61))
        if questions != expected:
            fail(f"mock {exam} question numbering is not exactly 1..60: {questions}", errors)
        if answers != expected:
            fail(f"mock {exam} answer numbering is not exactly 1..60: {answers}", errors)
        counts = mock_objective_counts(mock_path)
        expected_counts = {
            objective: WEIGHTS[objective]
            for objective in OBJECTIVES
            if (exam == "101" and int(objective.split(".", 1)[0]) <= 104)
            or (exam == "102" and int(objective.split(".", 1)[0]) >= 105)
        }
        if counts != expected_counts:
            fail(
                f"mock {exam} objective allocation differs from official weights: "
                f"found={counts}, expected={expected_counts}",
                errors,
            )

    answer_text = (ROOT / "exercises" / "answers.md").read_text(encoding="utf-8")
    chapter_answers = re.findall(r"\*\*\d{3}-Q\d+:\*\*", answer_text)
    if len(chapter_answers) != 71:
        fail(f"expected 71 chapter answers, found {len(chapter_answers)}", errors)

    mixed_questions = numbered_items(ROOT / "exercises" / "questions.md")
    if mixed_questions != list(range(1, 41)):
        fail("mixed assessment numbering is not exactly 1..40", errors)

    for path in MARKDOWN_FILES:
        text = path.read_text(encoding="utf-8")
        fence_count = len(re.findall(r"(?m)^```", text))
        if fence_count % 2:
            fail(f"unbalanced fenced code block: {path.relative_to(ROOT)}", errors)
        for line_number, line in enumerate(text.splitlines(), start=1):
            if line.endswith((" ", "\t")):
                fail(f"trailing whitespace: {path.relative_to(ROOT)}:{line_number}", errors)

    check_relative_links(errors)

    if errors:
        print("Repository checks failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        "Repository checks passed: "
        "42 objectives, 126 explained examples, two 60-question mocks, 71 chapter answers, "
        "40 mixed questions, balanced fences, and valid relative links."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
