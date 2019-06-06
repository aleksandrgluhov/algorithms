#!/usr/bin/python3
"""
    Helper classes and functions for algorithmic cases
    with unit tests, jff
    Gluhov Alex
"""
# imports
import random


# constants
TYPEERROR_REQUIRES_A_STRING = 'Function requires a string to operate'


# procedures and functions
def rand_int_list(start, end, count):
    """
    Function, generates a list filled with random ints
    :param start: low border (int)
    :param end: high border (int)
    :param count: list size (int)
    :return: list
    """
    return [random.randint(start, end) for i in range(0, count)]
