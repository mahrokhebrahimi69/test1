from __future__ import annotations

import pytest

from .qa_helpers import assert_case, case_ids, load_json_cases

CASES = [case for case in load_json_cases("regression_cases.json") if "positive_review" in case.get("tags", [])]


def test_positive_reviews_has_minimum_coverage():
    assert len(CASES) >= 100


@pytest.mark.parametrize("case", CASES, ids=case_ids(CASES))
def test_positive_reviews_cases(classify, case):
    """Positive reviews and polite criticism must approve with null reason."""
    assert_case(classify, case)

