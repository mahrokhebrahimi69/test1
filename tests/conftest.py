from __future__ import annotations

import importlib
import inspect
import os
from collections.abc import Callable
from typing import Any

import pytest

COMMON_CLASSIFIER_TARGETS = (
    "classifier:classify",
    "classifier:classify_review",
    "review_classifier:classify",
    "review_classifier:classify_review",
    "src.classifier:classify",
    "src.classifier:classify_review",
    "app.classifier:classify",
    "main:classify",
    "main:classify_review",
)


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--classifier-target",
        action="store",
        default=None,
        help="Classifier callable as module:function. Overrides CLASSIFIER_UNDER_TEST.",
    )


def _load_target(target: str) -> Callable[..., Any]:
    module_name, sep, attr_path = target.partition(":")
    if not sep:
        module_name, _, attr_path = target.rpartition(".")
    if not module_name or not attr_path:
        raise ImportError(f"Classifier target must be 'module:function', got {target!r}")
    module = importlib.import_module(module_name)
    obj: Any = module
    for part in attr_path.split("."):
        obj = getattr(obj, part)
    if not callable(obj):
        raise TypeError(f"Classifier target {target!r} is not callable")
    return obj


def _discover_classifier(target: str | None) -> Callable[..., Any]:
    attempted: list[str] = []
    candidates = [target] if target else []
    candidates.extend(COMMON_CLASSIFIER_TARGETS)
    for candidate in candidates:
        if not candidate:
            continue
        attempted.append(candidate)
        try:
            return _load_target(candidate)
        except (ImportError, AttributeError, TypeError):
            continue
    formatted = "\n  - ".join(attempted)
    raise AssertionError(
        "Could not load the classifier under test. Set CLASSIFIER_UNDER_TEST or pass "
        "--classifier-target as 'module:function'. Attempted:\n  - " + formatted
    )


def _invoke(fn: Callable[..., Any], text: str) -> Any:
    attempts = [
        lambda: fn(text),
        lambda: fn(review=text),
        lambda: fn(text=text),
        lambda: fn(comment=text),
        lambda: fn({"text": text, "review": text, "comment": text}),
    ]
    last_error: TypeError | None = None
    for attempt in attempts:
        try:
            result = attempt()
            if inspect.isawaitable(result):
                import asyncio

                return asyncio.run(result)
            return result
        except TypeError as exc:
            last_error = exc
            continue
    raise AssertionError(f"Classifier callable could not be invoked with a review text: {last_error}")


@pytest.fixture(scope="session")
def classifier_callable(pytestconfig: pytest.Config) -> Callable[..., Any]:
    target = pytestconfig.getoption("--classifier-target") or os.getenv("CLASSIFIER_UNDER_TEST")
    return _discover_classifier(target)


@pytest.fixture(scope="session")
def classify(classifier_callable: Callable[..., Any]) -> Callable[[str], Any]:
    def _classify(text: str) -> Any:
        return _invoke(classifier_callable, text)

    return _classify
