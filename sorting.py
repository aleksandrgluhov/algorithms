# -*- coding: utf-8 -*-
"""
    Sorting algorithms
    with unit tests, jff
    Gluhov Alex
"""
# --------------- imports --------------
import random
import unittest
from helper import rand_int_list


# ------ procedures and functions ------

def bubble_sort(slist):
    """
    Bubble sorting algorithm
    :param slist: unsorted int list
    :return: -
    """
    step = 0
    for top in range(len(slist)-1, 0, -1):
        for i in range(top):
            step += 1
            if slist[i] > slist[i+1]:
                slist[i], slist[i+1] = slist[i+1], slist[i]
    print('--------------------------')
    print('bubble sort: ')
    print(slist)
    print('list length: ', len(slist))
    print('steps taken: ', step)


def selection_sort(slist):
    """
    Selection sorting algorithm
    :param slist: unsorted int list
    :return: -
    """
    step = 0
    for socket in range(len(slist)-1, 0, -1):
        top = 0
        for i in range(1, socket+1):
            if slist[i] > slist[top]:
                top = i
        step += 1
        slist[socket], slist[top] = slist[top], slist[socket]
    print('--------------------------')
    print('selection sort: ')
    print(slist)
    print('list length: ', len(slist))
    print('steps taken: ', step)


def insertion_sort(slist, start=0, delta=1):
    """
    Insertion sorting algorithm
    :param slist: unsorted int list
    :param start: (int) beginning of sublist start index (for shell sort)
    :param delta: (int) sublist length (for shell sort)
    :return: -
    """
    step = 0
    for i in range(start+delta, len(slist), delta):
        pos = i
        cval = slist[pos]
        step += 1
        while pos > 0:
            if slist[pos - 1] < cval:
                break
            slist[pos] = slist[pos-1]
            pos -= 1

        slist[pos] = cval

    print('--------------------------')
    print('insertion sort: ')
    print(slist)
    print('list length: ', len(slist))
    print('steps taken: ', step)


def shell_sort(slist):
    """
    Shell sorting algorithm
    :param slist: unsorted int list
    :return: -
    """
    step = 0
    nested_lcount = len(slist) // 2
    while nested_lcount > 0:
        step += 1
        for start_pos in range(nested_lcount):
            insertion_sort(slist, start_pos, nested_lcount)
        nested_lcount //= 2

    print('--------------------------')
    print('shell sort: ')
    print(slist)
    print('list length: ', len(slist))
    print('steps taken: ', step)


def merge_sort(slist):
    """
    Merge sorting algorithm
    :param slist: unsorted int list
    :return: -
    """
    list_len = len(slist)
    if list_len > 1:
        mid = list_len // 2
        slleft_half = slist[:mid]
        slrigth_half = slist[mid:]

        merge_sort(slleft_half)
        merge_sort(slrigth_half)

        left_len = len(slleft_half)
        right_len = len(slrigth_half)

        i, j, k = 0, 0, 0

        while i < left_len and j < right_len:
            if slleft_half[i] < slrigth_half[j]:
                slist[k] = slleft_half[i]
                i += 1
            else:
                slist[k] = slrigth_half[j]
                j += 1
            k += 1

        def merge_parts(mlist, mpart, part_iter, super_iter):
            while len(mpart) > part_iter:
                mlist[super_iter] = mpart[part_iter]
                part_iter += 1
                super_iter += 1

        merge_parts(slist, slleft_half, i, k)
        merge_parts(slist, slrigth_half, j, k)


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


# --------- program entry point --------
if __name__ == '__main__':
    random.seed()
    unittest.main()
