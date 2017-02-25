# -*- coding: utf-8 -*-
"""
    Helper classes and functions for algorithmic cases
    with unit tests, jff
    Gluhov Alex
"""
# --------------- imports --------------
import random
import unittest


# ------ procedures and functions ------
def rand_int_list(start, end, count):
    """
    Function, generates a list filled with random ints
    :param start: low border (int)
    :param end: high border (int)
    :param count: list size (int)
    :return: list
    """
    return [random.randint(start, end) for i in range(0, count)]


# --------------- classes --------------
class TestRandList(unittest.TestCase):
    """
    Unit test for the rand_int_list function
    """
    def setUp(self):
        """
        setting up the inititals:
        low border, high border, list size and creates the list
        :return:
        """
        self.list_min_val = 11
        self.list_max_val = 999
        self.list_size = 30
        self.test_list = rand_int_list(self.list_min_val,
                                       self.list_max_val,
                                       self.list_size)

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


# --------- program entry point --------
if __name__ == '__main__':
    random.seed()
    unittest.main()
