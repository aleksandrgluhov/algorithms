#!/usr/bin/python3

# imports
import unittest
from python.palindrome import Palindrome, palindrome


# classes
class TestPalindromeFunction(unittest.TestCase):
    """
    Unit test for the palindrome function
    """
    def setUp(self):
        """
        setting up the inititals:
        palindromes list and not-palindromes list
        :return:
        """

        # simple exercises
        self._TESTDATA_LETTER_PALINDROMES = [
            'Anna', 'Lol', 'Wow', 'Dad'
        ]

        self._TESTDATA_LETTER_NOT_PALINDROMES = [
            'Gopher',
            'Truffle',
            'Ambassador'
        ]

        self._TESTDATA_SENTENCE_PALINDROME = """
        Dennis, Nell, Edna, Leon, Nedra, Anita, Rolf, Nora, Alice, Carol, Leo, Jane, Reed, Dena, Dale, Basil, Rae,
        Penny, Lana, Dave, Denny, Lena, Ida, Bernadette, Ben, Ray, Lila, Nina, Jo, Ira, Mara, Sara, Mario, Jan, Ina, 
        Lily, Arne, Bette, Dan, Reba, Diane, Lynn, Ed, Eva, Dana, Lynne, Pearl, Isabel, Ada, Ned, Dee, Rena, Joel,
        Lora, Cecil, Aaron, Flora, Tina, Arden, Noel, and Ellen sinned.
        """

        self._TESTDATA_SENTENCE_WORD_PALINDROME = """
        Step on no pets
        """

        self._TESTDATA_SENTENCE_NOT_PALINDROME = """
        This is totally not a palindrome
        """

    def test_is_palindrome_simple(self):
        """
        palindromes check
        :return:
        """
        for test_val in self._TESTDATA_LETTER_PALINDROMES:
            self.assertEqual(True, palindrome(test_val))

    def test_is_palindrome_simple_case_sensitive(self):
        """
        palindromes check
        :return:
        """
        for test_val in self._TESTDATA_LETTER_PALINDROMES:
            self.assertEqual(False, palindrome(test_val, case_sensitive=True))

    def test_not_palindrome_simple(self):
        """
        not-palindromes check
        :return:
        """
        for test_val in self._TESTDATA_LETTER_NOT_PALINDROMES:
            self.assertEqual(False, palindrome(test_val))

    def test_is_palindrome_multiline_sentence(self):

        self.assertEqual(True, palindrome(self._TESTDATA_SENTENCE_PALINDROME, ignore_punctuation=True))

    def test_is_palindrome_words_sentence(self):

        self.assertEqual(True, palindrome(self._TESTDATA_SENTENCE_WORD_PALINDROME, follow_words=True,
                                          ignore_punctuation=True))

    def test_is_not_palindrome_sentence(self):

        self.assertEqual(False, palindrome(self._TESTDATA_SENTENCE_NOT_PALINDROME, ignore_punctuation=True))


class TestPalindromeClass(TestPalindromeFunction):
    def test_is_palindrome_simple(self):
        """
        palindromes check
        :return:
        """
        for test_val in self._TESTDATA_LETTER_PALINDROMES:
            self.assertEqual(True, Palindrome(test_val).is_palindrome)

    def test_is_palindrome_simple_case_sensitive(self):
        """
        palindromes check
        :return:
        """
        for test_val in self._TESTDATA_LETTER_PALINDROMES:
            self.assertEqual(False, Palindrome(test_val, case_sensitive=True).is_palindrome)

    def test_not_palindrome_simple(self):
        """
        not-palindromes check
        :return:
        """
        for test_val in self._TESTDATA_LETTER_NOT_PALINDROMES:
            self.assertEqual(False, Palindrome(test_val).is_palindrome)

    def test_is_palindrome_multiline_sentence(self):

        self.assertEqual(True, Palindrome(self._TESTDATA_SENTENCE_PALINDROME,
                                          ignore_punctuation=True).is_palindrome)
