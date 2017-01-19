#!/usr/bin/env python

""" Tests against challenge requirements """

import unittest
from comparison import comparison


class ComparisonValueTest(unittest.TestCase):
    """ Test first value is greater than the second """
    def test_first_value_greater(self):
        self.assertEqual(comparison.compare_values("3.23.1", "3.2.1080"), 1)

    """ Test first value is less than the second """
    def test_first_value_less(self):
        self.assertEqual(comparison.compare_values("3.0.11", "9.100.304"), -1)

    """ Test first value is equal to the second """
    def test_first_value_equal(self):
        self.assertEqual(comparison.compare_values("9.11", "9.11"), 0)

    """ Test that 0.0 version fails """
    def test_invalid_double_zero_version(self):
        self.assertFalse(comparison.compare_values("0.0", "0.1.2"))

    """ Test that version starting with 0.0 fails """
    def test_invalid_double_zero_start_version(self):
        self.assertFalse(comparison.compare_values("0.0.4.99", "0.1.2"))

    """ Test that single placement version fails """
    def test_invalid_single_place(self):
        self.assertFalse(comparison.compare_values("99", "100.1.2"))

    """ Test that placement with leading zero fails """
    def test_invalid_leading_zero(self):
        self.assertFalse(comparison.compare_values("5.0.1.1", "012.34.5"))

if __name__ == '__main__':
    unittest.main()
