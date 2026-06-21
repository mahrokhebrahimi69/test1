from __future__ import annotations

import pytest

from .qa_helpers import all_json_cases, assert_case, case_ids, normalize_response

CASES = all_json_cases()


def test_confidence_suite_has_large_coverage():
    assert len(CASES) >= 1500


@pytest.mark.parametrize("case", CASES, ids=case_ids(CASES))
def test_confidence_is_between_zero_and_one_and_rounded(classify, case):
    output = assert_case(classify, case)
    assert 0 <= output["confidence"] <= 1
    assert round(output["confidence"], 2) == output["confidence"]


@pytest.mark.parametrize("case", CASES[::17], ids=case_ids(CASES[::17]))
def test_classifier_output_is_deterministic(classify, case):
    first = normalize_response(classify(case["text"]))
    second = normalize_response(classify(case["text"]))
    third = normalize_response(classify(case["text"]))
    assert first["comment"] == second["comment"] == third["comment"] == case["text"]
    assert first["label"] == second["label"] == third["label"]
    assert first["reason"] == second["reason"] == third["reason"]
    assert first["confidence"] == second["confidence"] == third["confidence"]
