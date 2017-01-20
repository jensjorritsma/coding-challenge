# coding-challenge

Usage:
from comparison import comparison

Method:
compare_values(x, y, z)

The compare_values method takes two semantic version strings and a comparison operator as variables and compares them.  Valid operators are <, >, ==, <=, >=, ~>.  Returns True when first string compares to second string, if not, returns false.  For invalid values of versions or operator, returns exception.

compare_values("3.2.1", "1.2.3", "==")

http://semver.org/ - Version guidelines
