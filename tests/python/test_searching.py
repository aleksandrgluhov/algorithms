#!/usr/bin/python3

# imports
import random
import unittest
from python.helper import rand_int_list
from python.searching import sequential_search, binary_search, recursive_bsearch


# classes
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
