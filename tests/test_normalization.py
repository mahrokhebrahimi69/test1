from __future__ import annotations

import pytest

from .qa_helpers import assert_case, case_ids, load_json_cases

CASES = load_json_cases("normalization_cases.json")


def test_normalization_has_minimum_coverage():
    assert len(CASES) >= 100


@pytest.mark.parametrize("case", CASES, ids=case_ids(CASES))
def test_normalization_cases(classify, case):
    """Unicode and orthographic variants should classify consistently."""
    assert_case(classify, case)


def test_normalization_equivalence_groups_have_consistent_expectations():
    groups = {}
    for case in CASES:
        groups.setdefault(case.get("equivalence_group"), set()).add((case["expected_label"], case["expected_reason"], case["expected_override"]))
    for group, expectations in groups.items():
        assert group is not None
        assert len(expectations) == 1, f"{group} mixes expectations: {expectations}"

