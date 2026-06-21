from __future__ import annotations

import pytest

from .qa_helpers import assert_case, case_ids, cases_for_reason

REASON = "override_02_political"
CASES = cases_for_reason(REASON)


def test_override_02_political_has_minimum_coverage():
    assert len(CASES) >= 50


@pytest.mark.parametrize("case", CASES, ids=case_ids(CASES))
def test_override_02_political_classifies_political(classify, case):
    output = assert_case(classify, case)
    assert output["label"] == "rejection"
    assert output["reason"] == REASON
