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
    """ Accepts two semantic strings as values """
    results = check_valid(x, y)
    if not results:
        return False
    else:
         return compare_version(x, y)


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
    if not determine_valid(x):
        return False
    elif not determine_valid(y):
        return False
    else:
        return True


def determine_valid(x):
    """ Ensure that variables match semantic guidelines """
    version_split = x.split(".")
    """ If version is only one place, fail """
    if len(version_split) < 2:
        return False
    """ If version has a zero prefix, fail """
    for place in version_split:
        if (place[:1] == "0") and (len(place) > 1):
            return False
    """ If first two places are zero, fail """
    if len(version_split) >= 2:
        if (version_split[0] == "0") and (version_split[1] == "0"):
            return False
    return True
