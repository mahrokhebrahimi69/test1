from __future__ import annotations

import pytest

from .qa_helpers import assert_case, case_ids, load_json_cases

CASES = load_json_cases("noisy_cases.json")


def test_noise_has_minimum_coverage():
    assert len(CASES) >= 100


@pytest.mark.parametrize("case", CASES, ids=case_ids(CASES))
def test_noise_cases(classify, case):
    """Noisy punctuation and elongation should not hide policy signals."""
    assert_case(classify, case)

