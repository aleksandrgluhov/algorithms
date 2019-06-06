#!/usr/bin/python3

# imports
import random
import unittest
from python.helper import rand_int_list


# classes
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

        # init random generator
        random.seed()
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
