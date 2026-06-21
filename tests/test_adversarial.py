from __future__ import annotations

import pytest

from .qa_helpers import assert_case, case_ids, load_json_cases

CASES = load_json_cases("adversarial_cases.json")


def test_adversarial_has_minimum_coverage():
    assert len(CASES) >= 100


@pytest.mark.parametrize("case", CASES, ids=case_ids(CASES))
def test_adversarial_cases(classify, case):
    """Prompt injection instructions must not override classification rules."""
    assert_case(classify, case)

