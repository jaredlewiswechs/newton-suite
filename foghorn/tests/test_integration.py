import pytest

from foghorn import (
    Card,
    add_object,
    get_object_store,
    undo,
    redo,
    execute_service,
)


def test_import_foghorn():
    import importlib

    mod = importlib.import_module("foghorn")
    assert hasattr(mod, "__version__")


def test_add_and_undo_redo_card():
    store = get_object_store()
    initial = store.count()

    c = Card(title="Integration Test Card", content="hello")

    # Add via command helper
    assert add_object(c) is True
    assert store.count() == initial + 1

    # Undo should remove it
    assert undo() is True
    assert store.count() == initial

    # Redo should bring it back
    assert redo() is True
    assert store.count() == initial + 1


def test_echo_service_executes_and_returns_card():
    c = Card(title="Echo Test", content="payload")
    res = execute_service("Echo", c)

    assert res.success is True
    assert res.results is not None
    assert len(res.results) >= 1
    # Result should be a Card-like object
    assert hasattr(res.results[0], "title")
    assert "Echo" in res.results[0].title
