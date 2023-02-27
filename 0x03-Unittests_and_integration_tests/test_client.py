#!/usr/bin/env python3
""" Test Client Document """
import unittest
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        """Test TestGitHubOrgClients method"""
        with patch.object(GithubOrgClient,
                          'org', new_callable=PropertyMock) as m:
            m.return_value = {"repos_url": "89"}
            test_org = GithubOrgClient('holberton')
            t_rep_url = test_org._public_repos_url
            self.assertEqual(t_rep_url, m.return_value.get('repos_url'))
            m.assert_called_once()
