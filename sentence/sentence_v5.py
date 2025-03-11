"""A third version of a simple sentence class.

This code is primarily from chapter 17 Fluent Python by Luciano Ramalho.

In this implementation, SentenceV5 is the same as SentenceV4, but uses a
generator expression in the __iter__ method to build a generator over the
words in the sentence and return it.
"""

import re
import reprlib
from collections.abc import Iterator

RE_WORD = re.compile(r'\w+')


class SentenceV5:
    """A class to represent a sentence as a sequence of words.

    Attributes:
        text: A string representing the sentence.
    """

    def __init__(self, text: str) -> None:
        """Initializes the Sentence class with a text string.

        Args:
            text: A string representing the sentence.
        """
        self.text = text

    def __repr__(self) -> str:
        """Returns a string representation of the Sentence class.

        Returns:
            A string representation of the Sentence class. reprlib.repr is
            used to generate an abbreviated string representation of the text.
        """
        return f'Sentence({reprlib.repr(self.text)})'

    def __iter__(self) -> Iterator[str]:
        """Returns an iterator over the words in the sentence.

        Returns:
            An generator expression to build a generator
                over the words in the sentence.
        """
        return (match.group() for match in RE_WORD.finditer(self.text))
