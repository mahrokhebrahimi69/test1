from __future__ import annotations

import pytest

from .qa_helpers import assert_case, case_ids, load_json_cases

CASES = load_json_cases("multilingual_cases.json")


def test_code_switching_has_minimum_coverage():
    assert len(CASES) >= 100


@pytest.mark.parametrize("case", CASES, ids=case_ids(CASES))
def test_code_switching_cases(classify, case):
    """Non-Persian content is rejected except allowed English food item names."""
    assert_case(classify, case)

