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


def compare_values(x, y, z):
    """ Accepts two semantic strings and a comparison operator as values """
    """ Checks if values are valid version strings, failure returns False """
    results = check_valid(x, y)
    if not results:
        raise Exception("Invalid version string")
    else:
        return compare_version(x, y, z)


def compare_version(x, y, z):
    if z == "==":
        return find_equal(x, y)
    elif z == ">":
        return find_greater(x, y)
    elif z == ">=":
        if find_equal(x, y) or find_greater(x, y):
            return True
        else:
            return False
    elif z == "<":
        return find_less(x, y)
    elif z == "<=":
        if find_equal(x, y) or find_less(x, y):
            return True
        else:
            return False
    elif z == "~>":
        return find_pessimistic(x, y)
    else:
        raise Exception("Invalid comparison operator string")


def find_greater(x, y):
    if x > y:
        return True
    else:
        return False


def find_less(x, y):
    if x < y:
        return True
    else:
        return False


def find_equal(x, y):
    if x == y:
        return True
    else:
        return False


def find_pessimistic(x, y):
    if not (find_less(x, y) or find_equal(x, y)):
        return False
    else:
        first = x.split(".")
        second = y.split(".")
        if len(first) > len(second):
            if find_equal(x, y) or find_less(x, y):
                return True
            else:
                return False
        else:
            return True


def check_valid(x, y):
    if not determine_valid(x):
        raise Exception("First value not valid version string")
    elif not determine_valid(y):
        raise Exeption("Second value not valid version string")
    else:
        return True


def determine_valid(x):
    """ Ensure that variables match semantic guidelines """
    version_split = x.split(".")
    """ If version is only one place or more than 3, fail """
    if len(version_split) < 2 or len(version_split) > 3:
        raise Exception("Defies semantic versioning for places")
    """ If version has a zero prefix, fail """
    for place in version_split:
        if (place[:1] == "0") and (len(place) > 1):
            raise Exception("Invalid version, leading zero")
    """ If first two places are zero, fail """
    if len(version_split) >= 2:
        if (version_split[0] == "0") and (version_split[1] == "0"):
            raise Exception("Invalid version, first two places cannot be zero")
    """ If valid string, return True """
    return True
