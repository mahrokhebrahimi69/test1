from __future__ import annotations

import pytest

from .qa_helpers import assert_case, case_ids, cases_with_tag

GOLDEN_CASES = cases_with_tag("golden_rule")
NEAR_MISS_CASES = cases_with_tag("near_miss")
OVERRIDE_PRECEDENCE_CASES = cases_with_tag("override_precedence")


def test_golden_rule_has_broad_regression_coverage():
    assert len(GOLDEN_CASES) >= 100


@pytest.mark.parametrize("case", GOLDEN_CASES, ids=case_ids(GOLDEN_CASES))
def test_golden_rule_approves_complete_polite_food_reviews(classify, case):
    output = assert_case(classify, case)
    assert output["label"] == "approval"
    assert output["reason"] is None


@pytest.mark.parametrize("case", NEAR_MISS_CASES, ids=case_ids(NEAR_MISS_CASES))
def test_golden_rule_precedence_over_plain_negative_sentiment(classify, case):
    """Complete calm criticism is approval even when it contains negative food-quality words."""
    output = assert_case(classify, case)
    assert output["label"] == "approval"
    assert output["reason"] is None


@pytest.mark.parametrize("case", OVERRIDE_PRECEDENCE_CASES, ids=case_ids(OVERRIDE_PRECEDENCE_CASES))
def test_hard_overrides_and_override_20_preempt_sentiment(classify, case):
    output = assert_case(classify, case)
    assert output["label"] == "disapproval"
    assert output["reason"] == case["expected_reason"]
