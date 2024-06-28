#!/usr/bin/env python3
""" Test cases for the function 'utils.access_nested_map' """
from utils import access_nested_map
from parameterized import parameterized
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """ TestAccessNestedMap to test edge cases for utils.access_nested_map """
    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2)
    ])

    def test_access_nested_map(self, nested_map, path, expected):
        """ Function for the test cases """
        self.assertEqual(access_nested_map(nested_map, path), expected)
