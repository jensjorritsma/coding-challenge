#!/usr/bin/env python

'''
Create a Python library from scratch that will compare two semantic version
strings. A successful implementation will be able to test two strings for the
following:
    Equal (==)
    Greater than (>)
    Greater than or equal to (>=)
    Pessimistic (~>)
    Less than (<)
    Less than or equal to (<=)
Constraints:
    Only use libraries built into Python itself (ie. os, sys, etc). Nothing
        from pypi or other external sources.
    Use Python 2.7 or 3+
'''


def compare_values(x, y):
    check_valid(x, y)
    return compare_version(x,y)


def compare_version(x, y):
    if x > y:
        return 1
    elif x < y:
        return -1
    elif x == y:
        return 0
    else:
        return "wat?"


def check_valid(x, y):
    determine_valid(x)
    determine_valid(y)


def determine_valid(x):
    version_split = x.split(".")
    if len(version_split) < 2:
        return False
    for place in version_split:
        if (place[:1] == "0") and (len(place) > 1):
            return False
    if len(version_split) >= 2:
        if (version_split[0] == "0") and (version_split[1] == "0"):
            return False


if __name__ == '__main__':
    test = compare_values("0.9.11", "0.10.0")
    print test
