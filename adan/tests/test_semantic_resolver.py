import json
from types import SimpleNamespace
from unittest.mock import patch

import pytest

from adan.semantic_resolver import SemanticResolver, SemanticWord


class DummyResponse:
    def __init__(self, data):
        self._data = data

    def read(self):
        return json.dumps(self._data).encode("utf-8")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False


def test_semanticword_properties():
    w = SemanticWord(word="run", score=100, tags=["v", "syn"])    
    assert w.is_verb
    assert not w.is_noun
    assert w.is_synonym


def test_means_like_parses_urlopen(monkeypatch):
    sample = [{"word": "capital", "score": 900, "tags": ["n"]}]
    def fake_urlopen(url, timeout=5):
        return DummyResponse(sample)

    monkeypatch.setattr("urllib.request.urlopen", fake_urlopen)
    r = SemanticResolver()
    results = r.means_like("capital", max_results=5)
    assert isinstance(results, list)
    assert len(results) == 1
    assert results[0].word == "capital"
    assert results[0].score == 900


def test_synonyms_and_related_to_parsing(monkeypatch):
    syn_sample = [{"word": "founder", "score": 800, "tags": ["n"]}]

    def fake_open_syn(url, timeout=5):
        return DummyResponse(syn_sample)

    monkeypatch.setattr("urllib.request.urlopen", fake_open_syn)
    r = SemanticResolver()
    syns = r.synonyms("founder")
    assert syns and syns[0].word == "founder"

    rel_sample = [{"word": "startup", "score": 700, "tags": ["n"]}]

    def fake_open_rel(url, timeout=5):
        return DummyResponse(rel_sample)

    monkeypatch.setattr("urllib.request.urlopen", fake_open_rel)
    rels = r.related_to("startup", "business")
    assert rels and rels[0].word == "startup"


def test_get_semantic_field_and_detect_shape(monkeypatch):
    r = SemanticResolver()

    # Patch means_like to return words that will cause CAPITAL_OF
    def fake_means_like(self, word, max_results=10):
        return [SemanticWord(word="capital", score=900, tags=["n"]), SemanticWord(word="seat", score=800, tags=["n"])]

    monkeypatch.setattr(SemanticResolver, "means_like", fake_means_like)
    field = r.get_semantic_field(["city", "govern"])
    assert "capital" in field

    shape = r.detect_shape("What city does France govern from?")
    assert shape == "CAPITAL_OF"


@pytest.mark.parametrize(
    "query,expected",
    [
        ("What city does France govern from?", "France"),
        ("Who founded Apple?", "Apple"),
        ("who is the president", None),
    ],
)
def test_extract_entity(query, expected):
    r = SemanticResolver()
    assert r.extract_entity(query) == expected
