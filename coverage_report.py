#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
OVERRIDES = [
    "override_01_brand",
    "override_02_political",
    "override_03_pii",
    "override_04_offensive",
    "override_05_discount",
    "override_06_advertising",
    "override_07_hygiene",
    "override_08_privacy",
    "override_09_order_change",
    "override_10_comparison",
    "override_11_indirect_advertising",
    "override_12_delivery_problem",
    "override_13_offtopic",
    "override_14_non_persian",
    "override_15_religious",
    "override_17_emoji",
    "override_18_app_problem",
    "override_19_courier",
    "override_20_incomplete",
]
MINIMUMS = {
    "boundary_cases.json": 100,
    "sarcasm_cases.json": 100,
    "mixed_cases.json": 100,
    "normalization_cases.json": 100,
}
ALL_DATA_FILES = [
    "regression_cases.json",
    "boundary_cases.json",
    "sarcasm_cases.json",
    "mixed_cases.json",
    "noisy_cases.json",
    "multilingual_cases.json",
    "adversarial_cases.json",
    "normalization_cases.json",
]


def load_cases(filename: str) -> list[dict]:
    with (DATA_DIR / filename).open(encoding="utf-8") as fh:
        return json.load(fh)


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize QA-suite case coverage.")
    parser.add_argument("--strict", action="store_true", help="Return non-zero if minimum coverage is not met.")
    args = parser.parse_args()

    all_cases = []
    for filename in ALL_DATA_FILES:
        cases = load_cases(filename)
        all_cases.extend(cases)
        print(f"{filename}: {len(cases)} cases")

    label_counts = Counter(case["expected_label"] for case in all_cases)
    reason_counts = Counter(case.get("expected_reason") for case in all_cases if case.get("expected_reason"))
    tag_counts = Counter(tag for case in all_cases for tag in case.get("tags", []))

    print("\nExpected label counts:")
    for label, count in sorted(label_counts.items()):
        print(f"  {label}: {count}")

    print("\nOverride coverage in regression_cases.json:")
    regression = load_cases("regression_cases.json")
    failures = []
    for reason in OVERRIDES:
        count = sum(1 for case in regression if case.get("expected_reason") == reason)
        status = "OK" if count >= 50 else "LOW"
        print(f"  {reason}: {count} ({status})")
        if count < 50:
            failures.append(f"{reason} has {count} cases, expected at least 50")

    print("\nRequired data-file minimums:")
    for filename, minimum in MINIMUMS.items():
        count = len(load_cases(filename))
        status = "OK" if count >= minimum else "LOW"
        print(f"  {filename}: {count}/{minimum} ({status})")
        if count < minimum:
            failures.append(f"{filename} has {count} cases, expected at least {minimum}")

    print("\nSelected behavioral tags:")
    for tag in ("golden_rule", "override_precedence", "override_20_precedence", "sarcasm", "mixed_sentiment", "normalization", "adversarial"):
        print(f"  {tag}: {tag_counts[tag]}")

    print(f"\nTotal cases: {len(all_cases)}")
    if failures:
        print("\nCoverage failures:")
        for failure in failures:
            print(f"  - {failure}")
        return 1 if args.strict else 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
