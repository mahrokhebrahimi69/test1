from __future__ import annotations

import pytest

from .qa_helpers import assert_case, case_ids, load_json_cases

CASES = load_json_cases("boundary_cases.json")


def test_boundary_logic_has_minimum_coverage():
    assert len(CASES) >= 100


@pytest.mark.parametrize("case", CASES, ids=case_ids(CASES))
def test_boundary_logic_cases(classify, case):
    """Boundary cases distinguish Golden Rule, unknown, incomplete, and hard overrides."""
    assert_case(classify, case)

