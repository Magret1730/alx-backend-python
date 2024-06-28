#!/usr/bin/env python3
""" Test cases for the function 'utils.access_nested_map' """
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize
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

    @parameterized.expand([
        ({}, ["a"]),
        ({"a": 1}, ["a", "b"])
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ Test for KeyError exceptions """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test cases for the function 'utils.get_json'"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Test get_json with different URLs and payloads"""
        with patch('utils.requests.get') as mocked_get:
            # Create a mock response object with a json method
            mocked_response = Mock()
            mocked_response.json.return_value = test_payload
            mocked_get.return_value = mocked_response

            # Call get_json and check the result
            result = get_json(test_url)
            self.assertEqual(result, test_payload)

            # Ensure the mocked get method was called once with the test_url
            mocked_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """ Test cases on memoization """

    def test_memoize(self):
        """ Test cases on memoization function """

        class TestClass:
            """ Test Class cases """
            def a_method(self):
                """ Function to return 42 """
                return 42

            @memoize
            def a_property(self):
                """ Funtion to return a_method function """
                return self.a_method()

        obj = TestClass()

        with patch.object(obj, 'a_method', return_value=lambda: 42,) as mocked:

            # Call a_property twice
            result1 = obj.a_property()
            result2 = obj.a_property()

            # Assert that a_method was called only once
            mocked.assert_called_once()

            # Assert that both results are correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
