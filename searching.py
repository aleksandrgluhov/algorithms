# -*- coding: utf-8 -*-
"""
    Searching algorithms
    with unit tests, jff
    Gluhov Alex
"""
# --------------- imports --------------
import random
import unittest
from helper import rand_int_list


# ------ procedures and functions ------
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


# --------------- classes --------------
class TestSearch(unittest.TestCase):
    """
    Unit test for the searching functions
    """
    def setUp(self):
        """
        setting up the inititals:
        low border, high border, list size and creates the list
        setting up the search values.
        :return:
        """
        self.list_min_val = 11
        self.list_max_val = 999
        self.list_size = 30
        self.test_list = rand_int_list(self.list_min_val,
                                       self.list_max_val,
                                       self.list_size)

        self.test_list.sort()
        self.rnd_sval = random.choice(self.test_list)
        self.min_sval = self.test_list[0]
        self.max_sval = self.test_list[self.list_size - 1]
        self.min_notinlist = self.list_min_val // 2
        self.max_notinlist = self.list_max_val * 2
        self.listrange_notinlist = self.test_list[0] + 1

    def test_rand_list(self):
        """
        check type and list size
        :return:
        """
        self.assertIsInstance(self.test_list, list)
        self.assertEqual(self.list_size, len(self.test_list))

    def test_list_val(self):
        """
        check type and border compliance
        :return:
        """
        for test_val in self.test_list:
            self.assertIsInstance(test_val, int)
            self.assertGreaterEqual(test_val, self.list_min_val)
            self.assertLessEqual(test_val, self.list_max_val)

    def test_sequential_search(self):
        """
        testing sequential_search()
        :return:
        """
        self.assertEqual(self.rnd_sval, self.test_list[sequential_search(self.test_list, self.rnd_sval)])
        self.assertEqual(0, sequential_search(self.test_list, self.min_sval))
        self.assertEqual(self.list_size - 1, sequential_search(self.test_list, self.max_sval))
        self.assertEqual(-1, sequential_search(self.test_list, self.min_notinlist))
        self.assertEqual(-1, sequential_search(self.test_list, self.max_notinlist))
        self.assertEqual(-1, sequential_search(self.test_list, self.listrange_notinlist))

    def test_binary_search(self):
        """
        testing binary_search()
        :return:
        """
        self.assertEqual(self.rnd_sval, self.test_list[binary_search(self.test_list, self.rnd_sval)])
        self.assertEqual(0, binary_search(self.test_list, self.min_sval))
        self.assertEqual(self.list_size - 1, binary_search(self.test_list, self.max_sval))
        self.assertEqual(-1, binary_search(self.test_list, self.min_notinlist))
        self.assertEqual(-1, binary_search(self.test_list, self.max_notinlist))
        self.assertEqual(-1, binary_search(self.test_list, self.listrange_notinlist))

    def test_recursive_bsearch(self):
        """
        testing recursive_bsearch()
        :return:
        """
        self.assertEqual(self.rnd_sval, self.test_list[recursive_bsearch(self.test_list, self.rnd_sval)])
        self.assertEqual(0, recursive_bsearch(self.test_list, self.min_sval))
        self.assertEqual(self.list_size - 1, recursive_bsearch(self.test_list, self.max_sval))
        self.assertEqual(-1, recursive_bsearch(self.test_list, self.min_notinlist))
        self.assertEqual(-1, recursive_bsearch(self.test_list, self.max_notinlist))
        self.assertEqual(-1, recursive_bsearch(self.test_list, self.listrange_notinlist))


# --------- program entry point --------
if __name__ == '__main__':
    random.seed()
    unittest.main()
