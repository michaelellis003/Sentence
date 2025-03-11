"""A third version of a simple sentence class.

This code is primarily from chapter 17 Fluent Python by Luciano Ramalho.

In this implementation, we avoid the need for a separate SentenceIterator class
by using a generator.
"""
# ruff: noqa: UP028

import re
import reprlib
from collections.abc import Iterator

RE_WORD = re.compile(r'\w+')


class SentenceV3:
    """A class to represent a sentence as a sequence of words.

    Attributes:
        text: A string representing the sentence.
        words: A list of words in the sentence.
    """

    def __init__(self, text: str) -> None:
        """Initializes the Sentence class with a text string.

        Args:
            text: A string representing the sentence.
        """
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self) -> str:
        """Returns a string representation of the Sentence class.

        Returns:
            A string representation of the Sentence class. reprlib.repr is
            used to generate an abbreviated string representation of the text.
        """
        return f'Sentence({reprlib.repr(self.text)})'

    def __iter__(self) -> Iterator[str]:
        """Returns an iterator over the words in the sentence.

        Yields:
            A word in the sentence.
        """
        for word in self.words:
            yield word
