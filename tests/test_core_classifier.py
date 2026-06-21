from __future__ import annotations

import pytest

try:
    from .qa_helpers import (
        REASON_CODES,
        assert_case,
        assert_case_schema,
        assert_output_schema,
        case_ids,
        load_json_cases,
        normalize_response,
    )
except ImportError:  # pragma: no cover - supports running tests as loose files.
    from qa_helpers import (  # type: ignore
        REASON_CODES,
        assert_case,
        assert_case_schema,
        assert_output_schema,
        case_ids,
        load_json_cases,
        normalize_response,
    )


CASES = load_json_cases("core_cases.json")


def test_core_suite_has_reasonable_size():
    assert 120 <= len(CASES) <= 250


def test_core_cases_have_valid_schema_and_unique_ids():
    seen_ids = set()
    for case in CASES:
        assert_case_schema(case)
        assert case["id"] not in seen_ids
        seen_ids.add(case["id"])


def test_core_cases_cover_all_reason_codes():
    reasons = {case["expected_reason"] for case in CASES if case["expected_reason"]}
    assert reasons == REASON_CODES


def test_core_cases_cover_main_behavior_groups():
    tags = {tag for case in CASES for tag in case.get("tags", [])}
    required_tags = {
        "approval",
        "golden_rule",
        "unknown",
        "override_20",
        "override_20_precedence",
        "sarcasm",
        "mixed_sentiment",
        "adversarial",
        "normalization",
    }
    assert required_tags <= tags


@pytest.mark.parametrize("case", CASES, ids=case_ids(CASES))
def test_core_classifier_cases(classify, case):
    assert_case(classify, case)


@pytest.mark.parametrize("case", CASES[::11], ids=case_ids(CASES[::11]))
def test_core_output_schema_is_exact(classify, case):
    output = normalize_response(classify(case["text"]))
    assert_output_schema(output)
    assert set(output["raw"].keys()) == {"comment", "label", "reason", "confidence"}


@pytest.mark.parametrize("case", CASES[::13], ids=case_ids(CASES[::13]))
def test_core_output_is_deterministic(classify, case):
    first = normalize_response(classify(case["text"]))
    second = normalize_response(classify(case["text"]))
    assert first["comment"] == second["comment"] == case["text"]
    assert first["label"] == second["label"]
    assert first["reason"] == second["reason"]
    assert first["confidence"] == second["confidence"]


@pytest.mark.parametrize("case", CASES, ids=case_ids(CASES))
def test_core_reason_is_null_for_approval_and_unknown(classify, case):
    output = assert_case(classify, case)
    if output["label"] in {"approval", "unknown"}:
        assert output["reason"] is None
