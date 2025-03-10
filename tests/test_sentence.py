"""Unit tests for the python_package_template module."""

import pytest

from sentence import SentenceV1, SentenceV2, SentenceV3


def test_sentence_v1():
    """Test the sentence_v1 function."""
    s = SentenceV1('"The time has come," the Walrus said.')

    s = iter(s)
    assert next(s) == 'The'
    assert next(s) == 'time'
    assert next(s) == 'has'
    assert next(s) == 'come'
    assert next(s) == 'the'
    assert next(s) == 'Walrus'
    assert next(s) == 'said'

    with pytest.raises(StopIteration):
        next(s)


def test_sentence_v2():
    """Test the sentence_v2 function."""
    s = SentenceV2('"The time has come," the Walrus said.')
    s = iter(s)
    assert next(s) == 'The'
    assert next(s) == 'time'
    assert next(s) == 'has'
    assert next(s) == 'come'
    assert next(s) == 'the'
    assert next(s) == 'Walrus'
    assert next(s) == 'said'

    with pytest.raises(StopIteration):
        next(s)


def test_sentence_v3():
    """Test the sentence_v3 function."""
    s = SentenceV3('"The time has come," the Walrus said.')
    s = iter(s)
    assert next(s) == 'The'
    assert next(s) == 'time'
    assert next(s) == 'has'
    assert next(s) == 'come'
    assert next(s) == 'the'
    assert next(s) == 'Walrus'
    assert next(s) == 'said'

    with pytest.raises(StopIteration):
        next(s)


def test_sentence_v4():
    """Test the sentence_v4 function."""
    s = SentenceV3('"The time has come," the Walrus said.')
    s = iter(s)
    assert next(s) == 'The'
    assert next(s) == 'time'
    assert next(s) == 'has'
    assert next(s) == 'come'
    assert next(s) == 'the'
    assert next(s) == 'Walrus'
    assert next(s) == 'said'

    with pytest.raises(StopIteration):
        next(s)
