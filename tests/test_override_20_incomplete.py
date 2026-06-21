from __future__ import annotations

import pytest

from .qa_helpers import assert_case, case_ids, cases_for_override

OVERRIDE_ID = "override_20_incomplete"
EXPECTED_REASON = "دیدگاه_نامرتبط"
CASES = cases_for_override(OVERRIDE_ID)


def test_override_20_incomplete_has_minimum_coverage():
    assert len(CASES) >= 50


@pytest.mark.parametrize("case", CASES, ids=case_ids(CASES))
def test_override_20_incomplete_classifies_incomplete(classify, case):
    output = assert_case(classify, case)
    assert output["label"] == "disapproval"
    assert output["reason"] == EXPECTED_REASON
    assert case["expected_override"] == OVERRIDE_ID


PRECEDENCE_CASES = [case for case in CASES if "override_20_precedence" in case.get("tags", [])]


@pytest.mark.parametrize("case", PRECEDENCE_CASES, ids=case_ids(PRECEDENCE_CASES))
def test_override_20_precedence_over_all_other_signals(classify, case):
    output = assert_case(classify, case)
    assert output["label"] == "disapproval"
    assert output["reason"] == "دیدگاه_نامرتبط"
