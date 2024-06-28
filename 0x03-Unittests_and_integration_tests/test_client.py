#!/usr/bin/env python3
"""
A module for testing the clents module.
"""
import unittest
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, MagicMock
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """ Class to test GithubOrgClient class """

    @patch('client.get_json', return_value={'login': 'mocked'})
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    def test_org(self, org_name, mocked_get):
        """
        Test for GithubOrgClient.org method.

        Uses patch to mock get_json and parameterized to test with different org names.
        """
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org()["login"], "mocked")
        mocked_get.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """
        Test for GithubOrgClient._public_repos_url property.

        Uses patch as a context manager to mock GithubOrgClient.org and asserts the expected URL.
        """
        with patch('client.GithubOrgClient.org', return_value={'repos_url': 'mocked_url'}):
            client = GithubOrgClient("mocked_org")
            self.assertEqual(client._public_repos_url, 'mocked_url')

    @patch('client.get_json', return_value=TEST_PAYLOAD[0][1])  # Assuming first entry in TEST_PAYLOAD has repos data
    @patch('client.GithubOrgClient._public_repos_url', new_callable=unittest.mock.PropertyMock)
    def test_public_repos(self, mocked_url, mocked_get):
        """
        Test for GithubOrgClient.public_repos method.

        Uses patch to mock get_json and PropertyMock for _public_repos_url.
        Asserts the returned list of repositories based on the mocked payload.
        """
        mocked_url.return_value = "mocked_url"
        client = GithubOrgClient("mocked_org")
        repos = client.public_repos(license="apache-2.0")
        expected_repos = [repo['name'] for repo in TEST_PAYLOAD[0][1] if 'license' in repo and repo['license']['key'] == 'apache-2.0']
        self.assertEqual(repos, expected_repos)
        mocked_get.assert_called_once_with("mocked_url")

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test for GithubOrgClient.has_license method.

        Parameterized test with different repo and license_key inputs.
        Asserts the expected returned value.
        """
        self.assertEqual(GithubOrgClient.has_license(repo, license_key), expected)


@parameterized_class('payload', [
    {'payload': {'org': {'repos_url': 'https://api.github.com/orgs/google/repos'}, 'repos': TEST_PAYLOAD[0][1], 'expected_repos': [repo['name'] for repo in TEST_PAYLOAD[0][1]]}},
])


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Class to test TestIntegrationGithubOrgClient class """

    @classmethod
    def setUpClass(cls):
        """
        Set up class-level fixtures for TestIntegrationGithubOrgClient.

        Mocks get_json with side_effect to return different payloads based on URL.
        """
        cls.get_patcher = patch('client.get_json', side_effect=cls.mocked_get_json)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """
        Tear down class-level fixtures for TestIntegrationGithubOrgClient.

        Stops the patcher for get_json.
        """
        cls.get_patcher.stop()

    @staticmethod
    def mocked_get_json(url):
        """
        Mocked method to return different payloads based on URL.

        Used as side_effect for patching get_json in TestIntegrationGithubOrgClient.
        """
        if url == 'https://api.github.com/orgs/google/repos':
            return TEST_PAYLOAD[0][1]
        else:
            raise ValueError(f'Unexpected URL: {url}')

    def test_public_repos(self):
        """
        Integration test for GithubOrgClient.public_repos method.

        Uses fixture data to simulate API responses and asserts the expected result.
        """
        client = GithubOrgClient("mock_org")
        repos = client.public_repos()
        self.assertEqual(repos, self.payload['expected_repos'])
