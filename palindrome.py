# -*- coding: utf-8 -*-
"""
    Palindrome check function
    with unit tests, jff
    Gluhov Alex
"""
# --------------- imports --------------
import unittest


# ------ procedures and functions ------
def palindrome(string_word):
    """
    Function, checks for palindrome and returns the result
    :param string_word:
    :return: boolean
    """
    rev = ''.join([string_word[i-1] for i in range(len(string_word), 0, -1)])
    return string_word.lower() == rev.lower()


# --------------- classes --------------
class TestPalindrome(unittest.TestCase):
    """
    Unit test for the palindrome function
    """
    def setUp(self):
        """
        setting up the inititals:
        palindromes list and not-palindromes list
        :return:
        """
        self.palindromes = [
            'Anna',
            'Lol',
            'Wow'
        ]
        self.notpalindromes = [
            'Gopher',
            'Truffle',
            'Ambassador'
        ]

    def test_ispalindrome_check(self):
        """
        palindromes check
        :return:
        """
        for test_val in self.palindromes:
            self.assertEqual(True, palindrome(test_val))

    def test_notpalindrome_check(self):
        """
        not-palindromes check
        :return:
        """
        for test_val in self.notpalindromes:
            self.assertEqual(False, palindrome(test_val))


# --------- program entry point --------
if __name__ == '__main__':
    unittest.main()
