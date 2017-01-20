#!/usr/bin/env python

""" Tests against challenge requirements """

import unittest
from comparison import comparison


class ComparisonValueTest(unittest.TestCase):
    """ Test first value is greater than the second """
    def test_first_value_greater(self):
        self.assertTrue(comparison.compare_values("3.23.1", "3.2.1080", ">"))

    """ Test first value is less than the second """
    def test_first_value_less(self):
        self.assertTrue(comparison.compare_values("3.0.11", "9.100.304", "<"))

    """ Test first value is equal to the second """
    def test_first_value_equal(self):
        self.assertTrue(comparison.compare_values("9.11", "9.11", "=="))

    """ Test first value is greater or equalthan the second """
    def test_first_value_greater_equal(self):
        self.assertTrue(comparison.compare_values("3.23.1", "3.2.1080", ">="))

    """ Test first value is less than the second """
    def test_first_value_less_equal(self):
        self.assertTrue(comparison.compare_values("3.0.11", "9.100.304", "<="))

    """ Test invalid comparison operator """
    def test_invalid_comparison_operator(self):
        with self.assertRaisesRegexp(Exception, "Invalid comparison"):
            comparison.compare_values("4.0.99", "0.1.2", "!=")

    """ Test that 0.0 version fails """
    def test_invalid_double_zero_version(self):
        with self.assertRaisesRegexp(Exception, "first two places"):
            comparison.compare_values("0.0", "0.1.2", "==")

    """ Test that version starting with 0.0 fails """
    def test_invalid_double_zero_start_version(self):
        with self.assertRaisesRegexp(Exception, "first two places"):
            comparison.compare_values("0.0.1", "0.1.2", "==")

    """ Test that single placement version fails """
    def test_invalid_single_place(self):
        with self.assertRaisesRegexp(Exception, "versioning for places"):
            comparison.compare_values("99", "0.1.2", "==")

    """ Test that more than three placements version fails """
    def test_invalid_four_place(self):
        with self.assertRaisesRegexp(Exception, "versioning for places"):
            comparison.compare_values("0.1.2.3", "0.1.2", "==")

    """ Test that placement with leading zero fails """
    def test_invalid_leading_zero(self):
        with self.assertRaisesRegexp(Exception, "leading zero"):
            comparison.compare_values("3.2.01", "0.1.2", "==")

if __name__ == '__main__':
    unittest.main()
