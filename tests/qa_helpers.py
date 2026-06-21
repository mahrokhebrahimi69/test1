from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any, Callable, Iterable

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
ALLOWED_LABELS = {"approval", "disapproval", "unknown"}
REASON_CODES = {
    "استفاده_از_کلمات_نامناسب",
    "انتقاد_و_پیشنهاد",
    "برخورد_نامناسب_پیک",
    "تبلیغات",
    "درخواست_ویرایش_سفارش",
    "دیدگاه_نامرتبط",
    "مشکلات_اپلیکیشن",
    "مقایسه_دو_مجموعه_با_یکدیگر",
    "موارد_بهداشتی",
    "موارد_مرتبط_با_کد_تخفیف",
    "نقض_حریم_شخصی",
    "سياسي",
}
OVERRIDE_IDS = {
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
}
REQUIRED_OUTPUT_KEYS = {"comment", "label", "reason", "confidence"}
REQUIRED_DATA_FILES = (
    "regression_cases.json",
    "boundary_cases.json",
    "sarcasm_cases.json",
    "mixed_cases.json",
    "noisy_cases.json",
    "multilingual_cases.json",
    "adversarial_cases.json",
    "normalization_cases.json",
)


def load_json_cases(filename: str) -> list[dict[str, Any]]:
    path = DATA_DIR / filename
    with path.open(encoding="utf-8") as fh:
        payload = json.load(fh)
    assert isinstance(payload, list), f"{filename} must contain a JSON array"
    return payload


def all_json_cases() -> list[dict[str, Any]]:
    cases: list[dict[str, Any]] = []
    for filename in REQUIRED_DATA_FILES:
        cases.extend(load_json_cases(filename))
    return cases


def case_ids(cases: Iterable[dict[str, Any]]) -> list[str]:
    return [str(case.get("id", "case")) for case in cases]


def cases_with_tag(tag: str, filename: str = "regression_cases.json") -> list[dict[str, Any]]:
    return [case for case in load_json_cases(filename) if tag in case.get("tags", [])]


def cases_for_override(override_id: str) -> list[dict[str, Any]]:
    return [
        case
        for case in load_json_cases("regression_cases.json")
        if case.get("expected_override") == override_id and "override" in case.get("tags", [])
    ]


def _plain_response(raw: Any) -> dict[str, Any]:
    if hasattr(raw, "model_dump"):
        raw = raw.model_dump()
    elif hasattr(raw, "dict") and callable(raw.dict):
        raw = raw.dict()
    elif hasattr(raw, "to_dict") and callable(raw.to_dict):
        raw = raw.to_dict()
    elif isinstance(raw, str):
        try:
            raw = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise AssertionError(f"Classifier must return a valid JSON object string, got: {raw!r}") from exc
    if not isinstance(raw, dict):
        raise AssertionError(f"Classifier output must be a JSON object/dict, got {type(raw)!r}: {raw!r}")
    return raw


def normalize_response(raw: Any) -> dict[str, Any]:
    payload = _plain_response(raw)
    keys = set(payload.keys())
    assert keys == REQUIRED_OUTPUT_KEYS, f"Classifier output must contain exactly {sorted(REQUIRED_OUTPUT_KEYS)}, got {sorted(keys)}: {payload!r}"
    confidence = payload["confidence"]
    assert not isinstance(confidence, bool) and isinstance(confidence, (int, float)), f"confidence must be numeric: {payload!r}"
    confidence_value = float(confidence)
    return {
        "comment": payload["comment"],
        "label": payload["label"],
        "reason": payload["reason"],
        "confidence": confidence_value,
        "raw": payload,
    }


def assert_case_schema(case: dict[str, Any]) -> None:
    required = {"id", "text", "expected_label", "expected_reason", "expected_override", "min_confidence", "max_confidence", "tags"}
    missing = required - set(case)
    assert not missing, f"Case {case!r} is missing keys: {sorted(missing)}"
    assert isinstance(case["id"], str) and case["id"].strip(), "case id must be a non-empty string"
    assert isinstance(case["text"], str), f"{case['id']} text must be a string"
    assert case["expected_label"] in ALLOWED_LABELS, f"{case['id']} has invalid expected_label"
    if case["expected_label"] == "disapproval":
        assert case["expected_reason"] in REASON_CODES, f"{case['id']} disapproval must use an exact reason code"
        if case["expected_override"] is not None:
            assert case["expected_override"] in OVERRIDE_IDS, f"{case['id']} has invalid expected_override"
    else:
        assert case["expected_reason"] is None, f"{case['id']} approval/unknown reason must be null"
        assert case["expected_override"] is None, f"{case['id']} approval/unknown override must be null"
    assert isinstance(case["tags"], list) and all(isinstance(tag, str) for tag in case["tags"])
    assert isinstance(case["min_confidence"], (int, float))
    assert isinstance(case["max_confidence"], (int, float))
    assert 0 <= case["min_confidence"] <= case["max_confidence"] <= 1
    if "competing_overrides" in case:
        assert all(override in OVERRIDE_IDS for override in case["competing_overrides"]), f"{case['id']} has invalid competing override"


def assert_output_schema(output: dict[str, Any]) -> None:
    assert isinstance(output["comment"], str), f"comment must be a string: {output!r}"
    assert output["label"] in ALLOWED_LABELS, f"label must be exactly one of {sorted(ALLOWED_LABELS)}: {output!r}"
    assert output["reason"] is None or output["reason"] in REASON_CODES, f"reason must be null or an exact reason code: {output!r}"
    assert isinstance(output["confidence"], float)
    assert math.isfinite(output["confidence"]), f"confidence must be finite: {output!r}"
    assert 0 <= output["confidence"] <= 1, f"confidence must be between 0 and 1: {output!r}"
    assert round(output["confidence"], 2) == output["confidence"], f"confidence must be rounded to 2 decimals: {output!r}"
    if output["label"] in {"approval", "unknown"}:
        assert output["reason"] is None, f"approval/unknown outputs must use null reason: {output!r}"
    if output["label"] == "disapproval":
        assert output["reason"] in REASON_CODES, f"disapproval outputs must include an exact reason code: {output!r}"


def assert_case(classify: Callable[[str], Any], case: dict[str, Any]) -> dict[str, Any]:
    assert_case_schema(case)
    output = normalize_response(classify(case["text"]))
    assert_output_schema(output)
    assert output["comment"] == case["text"], f"{case['id']} must preserve the original review text exactly in comment"
    assert output["label"] == case["expected_label"], f"{case['id']} label mismatch for text: {case['text']!r}"
    assert output["reason"] == case["expected_reason"], f"{case['id']} reason mismatch for text: {case['text']!r}"
    assert case["min_confidence"] <= output["confidence"] <= case["max_confidence"], (
        f"{case['id']} confidence {output['confidence']} outside expected range "
        f"[{case['min_confidence']}, {case['max_confidence']}]"
    )
    return output
