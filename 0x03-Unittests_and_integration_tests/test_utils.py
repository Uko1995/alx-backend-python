#!/usr/bin/env python3
'''unittest module for utils.py'''
import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    '''test class for access_nested_map'''
    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])

    def test_access_nested_map(self, nested_map, path, expected):
        '''testing the access_nested_map function'''
        self.assertEqual(access_nested_map(nested_map, path), expected)