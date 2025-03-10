"""Unit tests for the python_package_template module."""

import pytest

from sentence import SentenceV1, SentenceV2, SentenceV3, SentenceV4, SentenceV5


def test_sentence_v1_through_v5():
    """Test all of the sentence implementations function."""
    test_string = '"The time has come," the Walrus said.'

    # Create all sentence objects
    sentence_classes = [
        SentenceV1,
        SentenceV2,
        SentenceV3,
        SentenceV4,
        SentenceV5,
    ]
    sentences = [iter(cls(test_string)) for cls in sentence_classes]

    # Expected words to iterate through
    expected_words = ['The', 'time', 'has', 'come', 'the', 'Walrus', 'said']

    # Test that each implementation yields the same words
    for word in expected_words:
        for s in sentences:
            assert next(s) == word

    # Test that all iterators are exhausted
    for s in sentences:
        with pytest.raises(StopIteration):
            next(s)
