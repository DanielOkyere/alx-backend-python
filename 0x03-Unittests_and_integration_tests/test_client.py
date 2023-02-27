#!/usr/bin/env python3
""" Test Client Document """
import unittest
from unittest.mock import patch
from parameterized import parameterized

import client
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ Test GithuborgClient """
    @parameterized.expand([
        ("google"), ("abc")
    ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org, mock_org):
        """Test org method"""
        org_test = GithubOrgClient(org)
        t_response = org_test.org
        self.assertEqual(t_response, mock_org.return_value)
        mock_org.asser_called_once()
