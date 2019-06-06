#!/usr/bin/python3
"""
    Palindrome check function
    with unit tests, jff
    Gluhov Alex
"""


# imports
from string import punctuation
from python.helper import TYPEERROR_REQUIRES_A_STRING


# classes
class Palindrome(object):
    def __init__(self, s, follow_words=False, case_sensitive=False, ignore_punctuation=True):
        self.text_string = s
        self.is_palindrome = palindrome(self.text_string,
                                        follow_words=follow_words,
                                        case_sensitive=case_sensitive,
                                        ignore_punctuation=ignore_punctuation)

        self.is_not_palindrome = not self.is_palindrome

    def __repr__(self):
        return 'Palindrome check result: ' + self.is_palindrome


# procedures and functions
def palindrome(s, follow_words=False, case_sensitive=False, ignore_punctuation=True):
    """
    Function, checks for palindrome and returns the result
    :param s: input string, empty string returns True
    :param follow_words: check palindrome by words, not by letters (Default: No)
    :param case_sensitive: consider on differentiating between capital and lowercase letters (Default: No)
    :param ignore_punctuation: ignore any punctuation signs (Default: Yes)
    :return: Boolean, None if any middleware error occured
    """

    ret_val = None

    if not isinstance(s, str):
        raise TypeError(TYPEERROR_REQUIRES_A_STRING)

    string_text = ''.join(s.splitlines())

    if ignore_punctuation:
        string_text = string_text.translate(str.maketrans('', '', punctuation))

    if follow_words:
        string_reverse = reverse_words(string_text)
    else:
        string_text = ''.join(string_text.split())
        string_reverse = reverse_string(string_text)

    if case_sensitive:
        ret_val = (string_text == string_reverse)
    else:
        ret_val = (string_text.lower() == string_reverse.lower())

    return ret_val


def reverse_string(string_text):
    ret_val = string_text[::-1]
    return ret_val


def reverse_words(string_text):
    ret_val = ' '.join(reverse_string(string_text.split()))
    return ret_val
