#!/usr/bin/python3
"""
    Sorting algorithms
    with unit tests, jff
    Gluhov Alex
"""


# procedures and functions
def bubble_sort(slist, order=0, debug=False):
    """
    Bubble sorting algorithm
    :param slist: unsorted int list
    :return: -
    """
    step = 0
    for top in range(len(slist)-1, 0, -1):
        for i in range(top):
            step += 1
            if order <= 0:
                if slist[i] > slist[i + 1]:
                    slist[i], slist[i + 1] = slist[i + 1], slist[i]
            else:
                if slist[i] < slist[i + 1]:
                    slist[i], slist[i + 1] = slist[i + 1], slist[i]
    if debug:
        print('--------------------------')
        print('bubble sort: ')
        print(slist)
        print('list length: ', len(slist))
        print('steps taken: ', step)


def selection_sort(slist, order=0, debug=False):
    """
    Selection sorting algorithm
    :param slist: unsorted int list
    :return: -
    """
    step = 0
    for socket in range(len(slist)-1, 0, -1):
        top = 0
        for i in range(1, socket + 1):
            if order <= 0:
                if slist[i] > slist[top]:
                    top = i
            else:
                if slist[i] < slist[top]:
                    top = i
        step += 1
        slist[socket], slist[top] = slist[top], slist[socket]

    if debug:
        print('--------------------------')
        print('selection sort: ')
        print(slist)
        print('list length: ', len(slist))
        print('steps taken: ', step)


def insertion_sort(slist, start=0, delta=1, order=0, debug=False):
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
    if debug:
        print('--------------------------')
        print('insertion sort: ')
        print(slist)
        print('list length: ', len(slist))
        print('steps taken: ', step)


def shell_sort(slist, order=0, debug=False):
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
            insertion_sort(slist, start_pos, nested_lcount, order, debug)
        nested_lcount //= 2

    if debug:
        print('--------------------------')
        print('shell sort: ')
        print(slist)
        print('list length: ', len(slist))
        print('steps taken: ', step)


def merge_parts(mlist, mpart, part_iter, super_iter):
    while len(mpart) > part_iter:
        mlist[super_iter] = mpart[part_iter]
        part_iter += 1
        super_iter += 1


def merge_sort(slist, order=0, debug=False):
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

        merge_sort(slleft_half, order, debug)
        merge_sort(slrigth_half, order, debug)

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

        merge_parts(slist, slleft_half, i, k)
        merge_parts(slist, slrigth_half, j, k)
