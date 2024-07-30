#!/usr/bin/env python3
'''unittest module for utils.py'''
import unittest
from unittest.mock import Mock, patch
from utils import *
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

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, nested_map, path):
        '''testing for KeyError'''
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''testing class for get_json'''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        '''testing get_json'''
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        test = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(test, test_payload)
