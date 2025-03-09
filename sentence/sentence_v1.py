"""A simple sentence class.

This code is primarily from chapter 17 Fluent Python by Luciano Ramalho. The
main purpose is to learn how iterators and generators work in Python. This
first implementation defines the Sentence class as a sequence protocol. That
means the class implements the __getitem__ method and the __len__ method. The
class is iterable because all sequences are iterable.
"""

import re
import reprlib

RE_WORD = re.compile(r'\w+')


class SentenceV1:
    """A class to represent a sentence as a sequence of words.

    Attributes:
        text: A string representing the sentence.
        words: A list of words in the sentence.
    """

    def __init__(self, text):
        """Initializes the Sentence class with a text string.

        Args:
            text: A string representing the sentence.
        """
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        """Returns the word at the given index.

        Args:
            index: An integer representing the index of the word.

        Returns:
            A string representing the word at the given index.
        """
        return self.words[index]

    def __len__(self):
        """Returns the number of words in the sentence.

        Returns:
            An integer representing the number of words in the sentence.
        """
        return len(self.words)

    def __repr__(self):
        """Returns a string representation of the Sentence class.

        Returns:
            A string representation of the Sentence class. reprlib.repr is
            used to generate an abbreviated string representation of the text.
        """
        return f'Sentence({reprlib.repr(self.text)})'
