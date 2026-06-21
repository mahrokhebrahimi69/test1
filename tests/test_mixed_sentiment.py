from __future__ import annotations

import pytest

from .qa_helpers import assert_case, case_ids, load_json_cases

CASES = load_json_cases("mixed_cases.json")


def test_mixed_sentiment_has_minimum_coverage():
    assert len(CASES) >= 100


@pytest.mark.parametrize("case", CASES, ids=case_ids(CASES))
def test_mixed_sentiment_cases(classify, case):
    """Mixed sentiment remains approval unless an override is present."""
    assert_case(classify, case)

