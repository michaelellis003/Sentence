"""Unit tests for the python_package_template module."""

from sentence import SentenceV1


def test_sentence_v1():
    """Test the sentence_v1 function."""
    s = SentenceV1('"The time has come," the Walrus said.')

    assert s.words == ['The', 'time', 'has', 'come', 'the', 'Walrus', 'said']
    assert s[0] == 'The'
    assert s[5] == 'Walrus'
    assert len(s) == 7
