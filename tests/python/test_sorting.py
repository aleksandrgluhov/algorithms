#!/usr/bin/python3

# imports
import random
import unittest
from python.helper import rand_int_list
from python.sorting import bubble_sort, selection_sort, insertion_sort, shell_sort, merge_sort


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

    def test_bubble_sort(self):
        """
        Bubble sort test
        :return:
        """
        self.test_list = rand_int_list(self.list_min_val,
                                       self.list_max_val,
                                       self.list_size)
        bubble_sort(self.test_list)
        for i in range(0, len(self.test_list)):
            if i > 0:
                self.assertLessEqual(self.test_list[i-1], self.test_list[i])

    def test_selection_sort(self):
        """
        Selection sort test
        :return:
        """
        self.test_list = rand_int_list(self.list_min_val,
                                       self.list_max_val,
                                       self.list_size)
        selection_sort(self.test_list)
        for i in range(0, len(self.test_list)):
            if i > 0:
                self.assertLessEqual(self.test_list[i-1], self.test_list[i])

    def test_insertion_sort(self):
        """
        Insertion sort test
        :return:
        """
        self.test_list = rand_int_list(self.list_min_val,
                                       self.list_max_val,
                                       self.list_size)
        insertion_sort(self.test_list)
        for i in range(0, len(self.test_list)):
            if i > 0:
                self.assertLessEqual(self.test_list[i-1], self.test_list[i])

    def test_shell_sort(self):
        """
        Shell sort test
        :return:
        """
        self.test_list = rand_int_list(self.list_min_val,
                                       self.list_max_val,
                                       self.list_size)
        shell_sort(self.test_list)
        for i in range(0, len(self.test_list)):
            if i > 0:
                self.assertLessEqual(self.test_list[i-1], self.test_list[i])

    def test_merge_sort(self):
        """
        Merge sort test
        :return:
        """
        self.test_list = rand_int_list(self.list_min_val,
                                       self.list_max_val,
                                       self.list_size)
        merge_sort(self.test_list)
        for i in range(0, len(self.test_list)):
            if i > 0:
                self.assertLessEqual(self.test_list[i-1], self.test_list[i])
