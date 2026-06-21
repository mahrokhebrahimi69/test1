from __future__ import annotations

import pytest

from .qa_helpers import assert_case, case_ids, load_json_cases

CASES = load_json_cases("sarcasm_cases.json")


def test_sarcasm_has_minimum_coverage():
    assert len(CASES) >= 100


@pytest.mark.parametrize("case", CASES, ids=case_ids(CASES))
def test_sarcasm_cases(classify, case):
    """Sarcasm that demeans or mocks must not be treated as polite criticism."""
    assert_case(classify, case)

