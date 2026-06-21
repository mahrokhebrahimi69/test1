from __future__ import annotations

import pytest

from .qa_helpers import assert_case, case_ids, cases_for_override

OVERRIDE_ID = "override_10_comparison"
EXPECTED_REASON = "مقایسه_دو_مجموعه_با_یکدیگر"
CASES = cases_for_override(OVERRIDE_ID)


def test_override_10_comparison_has_minimum_coverage():
    assert len(CASES) >= 50


@pytest.mark.parametrize("case", CASES, ids=case_ids(CASES))
def test_override_10_comparison_classifies_comparison(classify, case):
    output = assert_case(classify, case)
    assert output["label"] == "disapproval"
    assert output["reason"] == EXPECTED_REASON
    assert case["expected_override"] == OVERRIDE_ID
