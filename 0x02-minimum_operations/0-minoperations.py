#!/usr/bin/python3

""" Minimum operations of Copy and Paste """


def minOperations(n):
    """ Function that checks the minimum operations in a file 
    Returns: An integer of 0 if impossible"""

    pasted = 1  # Characters that are present in a file
    copied = 0
    operations = 0  # Counter

    while pasted < n:
        # the copy operation
        if copied == 0:
            copied = pasted
            operations += 1

        if pasted == 1:
            pasted += copied
            operations += 1
            continue

        rem = n - pasted  # remaining to be pasted
        if rem < copied:
            return 0

        if rem % pasted != 0:
            pasted += copied
            operations += 1

        else:
            copied = pasted
            pasted += copied
            operations += 2

        if pasted == n:
            return operations
        else:
            return 0
