#!/usr/bin/python3

"""
    Searching algorithms
    with unit tests, jff
    Gluhov Alex
"""

# imports
import random
import unittest


# procedures and functions
def sequential_search(search_list, sought_value):
    """
    Sequential search: gives item index in list or -1, if not found
    :param search_list: a list of ints
    :param sought_value: int value to search
    :return: (int) index or -1
    """
    ret_val = -1
    for index in range(0, len(search_list)):
        if search_list[index] == sought_value:
            ret_val = index
            break
    return ret_val


def binary_search(search_list, sought_value):
    """
    Binary search: gives item index in list or -1, if not found
    Array must be sorted before call.
    :param search_list: a list of ints
    :param sought_value: int value to search
    :return: (int) index or -1
    """
    index, first_index = -1, 0
    last_index = len(search_list) - 1

    while first_index <= last_index:
        mid_index = (first_index + last_index) // 2
        if search_list[mid_index] == sought_value:
            index = mid_index
            break
        else:
            if search_list[mid_index] > sought_value:
                last_index = mid_index - 1
            else:
                first_index = mid_index + 1
    return index


def recursive_bsearch(search_list, sought_value, top=0, bottom=0):
    """
    Recursive binary search: gives item index in list or -1, if not found
    Array must be sorted before call.
    :param search_list:  a list of ints
    :param sought_value: int value to search
    :param top: top search border
    :param bottom: bottom search border
    :return: (int) index or -1
    """
    index, mid_index, first_index = -1, 0, 0
    sl_len = len(search_list)
    last_index = sl_len - 1

    if top > 0:
        first_index = top

    if bottom > 0:
        last_index = bottom

    mid_index = (first_index + last_index) // 2

    if sl_len == 0 or mid_index < first_index or mid_index > last_index:
        return index
    else:
        if search_list[mid_index] == sought_value:
            index = mid_index
        else:
            if last_index == 1:
                return index
            if search_list[mid_index] > sought_value:
                index = recursive_bsearch(search_list, sought_value, top, mid_index - 1)
            else:
                index = recursive_bsearch(search_list, sought_value, mid_index + 1, bottom)
    return index
