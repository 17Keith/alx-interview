#!/usr/bin/python3

""" Minimum operations """


def minOperations(n):
    """ Function that checks the minimum operations in a file """
    pasted = 1
    copied = 0
    operations = 0

    while pasted < n:
        if copied == 0:
            copied = pasted
            operations += 1

        if pasted == 1:
            pasted += copied
            operations += 1
            continue

        rem = n - pasted
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
