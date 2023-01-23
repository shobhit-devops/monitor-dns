import unittest
from unittest.mock import patch

import monitor_dns_script as script


class TestDNSMonitor(unittest.TestCase):

    @patch('script.dns.resolver.query')
    def test_substring_found(self, mock_query):
        mock_query.return_value = [("google-site",)]
        script.monitor_dns('futurestay.com', 1, 'google-site')
        self.assertTrue(mock_query.called)

    @patch('script.dns.resolver.query')
    def test_substring_not_found(self, mock_query):
        mock_query.return_value = [("not-found",)]
        script.monitor_dns('futurestay.com', 1, 'google-site')
        self.assertTrue(mock_query.called)

    @patch('script.dns.resolver.query')
    def test_dns_error(self, mock_query):
        mock_query.side_effect = script.dns.resolver.NXDOMAIN
        script.monitor_dns('futurestay.com', 1, 'google-site')
        self.assertTrue(mock_query.called)


if __name__ == '__main__':
    unittest.main()
