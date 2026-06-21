from __future__ import annotations

import pytest

from .qa_helpers import (
    REQUIRED_DATA_FILES,
    all_json_cases,
    assert_case,
    assert_case_schema,
    assert_output_schema,
    case_ids,
    load_json_cases,
    normalize_response,
)

ALL_CASES = all_json_cases()


@pytest.mark.parametrize("filename", REQUIRED_DATA_FILES)
def test_data_file_contains_valid_case_schema(filename):
    cases = load_json_cases(filename)
    assert cases, f"{filename} must not be empty"
    seen_ids = set()
    for case in cases:
        assert_case_schema(case)
        assert case["id"] not in seen_ids, f"duplicate id {case['id']} in {filename}"
        seen_ids.add(case["id"])


@pytest.mark.parametrize("case", ALL_CASES[::23], ids=case_ids(ALL_CASES[::23]))
def test_classifier_output_json_schema_validity(classify, case):
    output = normalize_response(classify(case["text"]))
    assert_output_schema(output)


@pytest.mark.parametrize("case", ALL_CASES[::19], ids=case_ids(ALL_CASES[::19]))
def test_label_reason_consistency(classify, case):
    output = assert_case(classify, case)
    if output["label"] in {"approval", "unknown"}:
        assert output["reason"] is None
    if output["label"] == "rejection":
        assert output["reason"] == case["expected_reason"]


def test_reason_is_null_for_all_approval_and_unknown_expected_cases():
    for case in ALL_CASES:
        if case["expected_label"] in {"approval", "unknown"}:
            assert case["expected_reason"] is None
