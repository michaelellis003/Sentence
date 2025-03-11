"""A third version of a simple sentence class.

This code is primarily from chapter 17 Fluent Python by Luciano Ramalho.

In this implementation, SentenceV4 is 'lazy'. The Sentence implements V1
through V3 are not lazy bedure the __init__ method early builds a list of
all the words in the text, binding it to the self.words attribute. This
requires processing of the entire text and the list may use as much memory
as the text itself. Most of this work will be in vain if the user only iterates
over the first few words of the sentence.

The SentenceV4 class is lazy because it yields words one at a time. The
re.finditer method is a lazy version of re.findall. Instead of a list
re.finditer returns a generator producing re.MatchObject instances on demand.
If there are many matches, re.finditer saves memory because it does not
store the matches in a list.
"""
# ruff: noqa: UP028

import re
import reprlib
from collections.abc import Iterator

RE_WORD = re.compile(r'\w+')


class SentenceV4:
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

        - finditer builds an iterator over the matches of RE_WORD on self.text,
            yielding MatchObject instances.
        - match.group() extracts the matched text from the MatchObject
            instance.

        Yields:
            A word in the sentence.
        """
        for match in RE_WORD.finditer(self.text):
            yield match.group()
