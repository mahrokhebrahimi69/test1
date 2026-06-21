from __future__ import annotations

import json
import math
import re
from pathlib import Path
from typing import Any, Callable, Iterable

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
ALLOWED_LABELS = {"approval", "rejection", "unknown"}
OVERRIDE_REASONS = {
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

LABEL_ALIASES = {
    "approve": "approval",
    "approved": "approval",
    "approval": "approval",
    "accept": "approval",
    "accepted": "approval",
    "allow": "approval",
    "allowed": "approval",
    "pass": "approval",
    "ok": "approval",
    "valid": "approval",
    "positive": "approval",
    "تایید": "approval",
    "تایید_شده": "approval",
    "قبول": "approval",
    "مجاز": "approval",
    "reject": "rejection",
    "rejected": "rejection",
    "rejection": "rejection",
    "deny": "rejection",
    "denied": "rejection",
    "block": "rejection",
    "blocked": "rejection",
    "invalid": "rejection",
    "negative": "rejection",
    "رد": "rejection",
    "رد_شده": "rejection",
    "غیرمجاز": "rejection",
    "unknown": "unknown",
    "uncertain": "unknown",
    "ambiguous": "unknown",
    "not_sure": "unknown",
    "not sure": "unknown",
    "نامشخص": "unknown",
    "نامعلوم": "unknown",
}

REASON_ALIASES = {
    "override_01_brand": {"1", "01", "brand", "competitor", "brand_mention", "برند", "رقیب"},
    "override_02_political": {"2", "02", "political", "politics", "سیاست", "سیاسی"},
    "override_03_pii": {"3", "03", "pii", "personal_info", "personal_information", "اطلاعات_شخصی"},
    "override_04_offensive": {"4", "04", "offensive", "insult", "abuse", "توهین", "فحاشی"},
    "override_05_discount": {"5", "05", "discount", "coupon", "promo", "تخفیف", "کد_تخفیف"},
    "override_06_advertising": {"6", "06", "advertising", "ad", "promotion", "تبلیغ", "تبلیغات"},
    "override_07_hygiene": {"7", "07", "hygiene", "health", "sanitation", "بهداشت", "مسمومیت"},
    "override_08_privacy": {"8", "08", "privacy", "private_data", "حریم_خصوصی"},
    "override_09_order_change": {"9", "09", "order_change", "modify_order", "change_order", "تغییر_سفارش"},
    "override_10_comparison": {"10", "comparison", "compare", "مقایسه"},
    "override_11_indirect_advertising": {"11", "indirect_advertising", "indirect_ad", "تبلیغ_غیرمستقیم"},
    "override_12_delivery_problem": {"12", "delivery", "delivery_problem", "late_delivery", "مشکل_تحویل", "تاخیر"},
    "override_13_offtopic": {"13", "offtopic", "off_topic", "irrelevant", "نامرتبط"},
    "override_14_non_persian": {"14", "non_persian", "not_persian", "foreign_language", "غیر_فارسی"},
    "override_15_religious": {"15", "religious", "religion", "مذهبی", "دینی"},
    "override_17_emoji": {"17", "emoji", "emojis", "ایموجی"},
    "override_18_app_problem": {"18", "app", "app_problem", "application_problem", "مشکل_اپ"},
    "override_19_courier": {"19", "courier", "driver", "delivery_person", "پیک"},
    "override_20_incomplete": {"20", "incomplete", "too_short", "gibberish", "ناقص", "نامفهوم"},
}

OUTPUT_KEY_ALIASES = {
    "label": ("label", "decision", "classification", "class", "status", "result", "verdict"),
    "reason": ("reason", "rule", "override", "category", "violation", "rejection_reason"),
    "confidence": ("confidence", "score", "probability", "certainty"),
}


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


def cases_for_reason(reason: str) -> list[dict[str, Any]]:
    return [
        case
        for case in load_json_cases("regression_cases.json")
        if case.get("expected_reason") == reason and "override" in case.get("tags", [])
    ]


def normalize_token(value: Any) -> str:
    text = str(value).strip().lower()
    text = text.replace("-", "_").replace(" ", "_")
    text = re.sub(r"__+", "_", text)
    return text


def normalize_label(value: Any) -> str:
    token = normalize_token(value)
    return LABEL_ALIASES.get(token, token)


def normalize_reason(value: Any) -> str | None:
    if value is None:
        return None
    if isinstance(value, (list, tuple)) and len(value) == 1:
        value = value[0]
    token = normalize_token(value)
    if token in {"", "none", "null", "nil", "no_reason", "بدون_دلیل"}:
        return None
    if token in OVERRIDE_REASONS:
        return token
    for canonical, aliases in REASON_ALIASES.items():
        normalized_aliases = {normalize_token(alias) for alias in aliases}
        if token in normalized_aliases:
            return canonical
        if canonical in token:
            return canonical
    return token


def _plain_response(raw: Any) -> Any:
    if hasattr(raw, "model_dump"):
        return raw.model_dump()
    if hasattr(raw, "dict") and callable(raw.dict):
        return raw.dict()
    if hasattr(raw, "to_dict") and callable(raw.to_dict):
        return raw.to_dict()
    if isinstance(raw, str):
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            return {"label": raw, "reason": None, "confidence": 1.0}
    if isinstance(raw, tuple):
        if len(raw) == 3:
            label, reason, confidence = raw
            return {"label": label, "reason": reason, "confidence": confidence}
        if len(raw) == 2:
            label, reason = raw
            return {"label": label, "reason": reason, "confidence": 1.0}
    return raw


def _lookup(payload: dict[str, Any], field: str) -> Any:
    for key in OUTPUT_KEY_ALIASES[field]:
        if key in payload:
            return payload[key]
    nested = payload.get("classification") or payload.get("output") or payload.get("response")
    if isinstance(nested, dict):
        for key in OUTPUT_KEY_ALIASES[field]:
            if key in nested:
                return nested[key]
    raise AssertionError(f"Classifier output is missing required field '{field}': {payload!r}")


def normalize_response(raw: Any) -> dict[str, Any]:
    payload = _plain_response(raw)
    if not isinstance(payload, dict):
        raise AssertionError(f"Classifier must return a dict, JSON string, dataclass-like object, or tuple; got {type(raw)!r}: {raw!r}")
    confidence = _lookup(payload, "confidence")
    try:
        confidence_value = float(confidence)
    except (TypeError, ValueError) as exc:
        raise AssertionError(f"confidence must be numeric, got {confidence!r}") from exc
    return {
        "label": normalize_label(_lookup(payload, "label")),
        "reason": normalize_reason(_lookup(payload, "reason")),
        "confidence": confidence_value,
        "raw": raw,
    }


def assert_case_schema(case: dict[str, Any]) -> None:
    required = {"id", "text", "expected_label", "expected_reason", "min_confidence", "max_confidence", "tags"}
    missing = required - set(case)
    assert not missing, f"Case {case!r} is missing keys: {sorted(missing)}"
    assert isinstance(case["id"], str) and case["id"].strip(), "case id must be a non-empty string"
    assert isinstance(case["text"], str), f"{case['id']} text must be a string"
    assert case["expected_label"] in ALLOWED_LABELS, f"{case['id']} has invalid expected_label"
    if case["expected_label"] == "rejection":
        assert case["expected_reason"] in OVERRIDE_REASONS, f"{case['id']} rejection must use a canonical override reason"
    else:
        assert case["expected_reason"] is None, f"{case['id']} approval/unknown reason must be null"
    assert isinstance(case["tags"], list) and all(isinstance(tag, str) for tag in case["tags"])
    assert isinstance(case["min_confidence"], (int, float))
    assert isinstance(case["max_confidence"], (int, float))
    assert 0 <= case["min_confidence"] <= case["max_confidence"] <= 1
    if "competing_reasons" in case:
        assert all(reason in OVERRIDE_REASONS for reason in case["competing_reasons"]), f"{case['id']} has invalid competing reason"


def assert_output_schema(output: dict[str, Any]) -> None:
    assert output["label"] in ALLOWED_LABELS, f"unexpected normalized label: {output!r}"
    assert output["reason"] is None or output["reason"] in OVERRIDE_REASONS, f"unexpected normalized reason: {output!r}"
    assert isinstance(output["confidence"], float)
    assert math.isfinite(output["confidence"]), f"confidence must be finite: {output!r}"
    assert 0 <= output["confidence"] <= 1, f"confidence must be between 0 and 1: {output!r}"
    if output["label"] in {"approval", "unknown"}:
        assert output["reason"] is None, f"approval/unknown outputs must not include a reason: {output!r}"
    if output["label"] == "rejection":
        assert output["reason"] in OVERRIDE_REASONS, f"rejection outputs must include a canonical reason: {output!r}"


def assert_case(classify: Callable[[str], Any], case: dict[str, Any]) -> dict[str, Any]:
    assert_case_schema(case)
    output = normalize_response(classify(case["text"]))
    assert_output_schema(output)
    assert output["label"] == case["expected_label"], f"{case['id']} label mismatch for text: {case['text']!r}"
    assert output["reason"] == case["expected_reason"], f"{case['id']} reason mismatch for text: {case['text']!r}"
    assert case["min_confidence"] <= output["confidence"] <= case["max_confidence"], (
        f"{case['id']} confidence {output['confidence']} outside expected range "
        f"[{case['min_confidence']}, {case['max_confidence']}]"
    )
    return output
