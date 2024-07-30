#!/usr/bin/env python3
'''unittest module for utils.py'''
import unittest
from unittest.mock import Mock, patch
from client import *
from utils import *
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    '''test class for GithubOrgClient'''
    @parameterized.expand(['google', 'abc'])
    @patch('client.get_json')
    def test_org(self, org_name, mock_json_object):
        """
            A test case that test GithubOrgClient.org
            returns the correct value.
        """
        client = GithubOrgClient(org_name)
        full_url = client.ORG_URL.format(org=client._org_name)
        client.org()
        mock_json_object.assert_called_once_with(full_url)
