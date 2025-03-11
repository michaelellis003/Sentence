"""A second version of a simple sentence class.

This code is primarily from chapter 17 Fluent Python by Luciano Ramalho. This
second implementation defines the Sentence class as an iterator protocol. That
means the class implements the __iter__ method and the __next__ method.

This implementation helps make the difference between an iterable and an
iterator clear. In this case, SetneceIterator is an iterator because it
implements __iter__ and __next__ and Sentence is an iterable because it
implements a __iter__ method that returns SetneceIterator, an Iterator.

A common mistake to avoid is to make an Iterable an Iterator for iterselg by
implementing __next__ in the Iterable.
"""

import re
import reprlib

RE_WORD = re.compile(r'\w+')


class SentenceV2:
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

    def __iter__(self) -> 'SentenceIterator':
        """Returns an iterator over the words in the sentence.

        Returns:
            An iterator over the words in the sentence.
        """
        return SentenceIterator(self.words)


class SentenceIterator:
    """An iterator over the words in a sentence.

    Attributes:
        words: A list of words in the sentence.
        index: An integer representing the current index in the list of words.
    """

    def __init__(self, words: list) -> None:
        """Initializes the SentenceIterator class with a list of words.

        Args:
            words: A list of words in the sentence.
        """
        self.words = words
        self.index = 0

    def __next__(self) -> str:
        """Returns the next word in the sentence.

        Returns:
            A string representing the next word in the sentence.

        Raises:
            StopIteration: If there are no more words in the sentence.
        """
        try:
            word = self.words[self.index]
        except IndexError as exc:
            raise StopIteration() from exc
        self.index += 1
        return word

    # Implementing __iter__ is not required, but it is a best practice to do
    # so. Iterators are susposed to implement both __iter__ and __next__ and
    # doing so makes the iterator pass the issubclass(SentenceIterator,
    # abc.Iterable) test.
    def __iter__(self) -> 'SentenceIterator':
        """Returns an iterator over the words in the sentence.

        Returns:
            An iterator over the words in the sentence.
        """
        return self
