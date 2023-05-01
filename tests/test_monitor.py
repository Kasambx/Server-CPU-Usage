import unittest
import requests
from unittest.mock import patch
from monitor import main, send_email_alert, send_slack_alert

class TestMonitor(unittest.TestCase):
    @patch('monitor.requests.get')
    def test_website_is_up(self, mock_get):
        mock_get.return_value.status_code = 200
        main()  # Call the main function to monitor the website
        # Assert that no alert was sent
        self.assertEqual(send_email_alert.called, False)
        self.assertEqual(send_slack_alert.called, False)

    @patch('monitor.requests.get')
    def test_website_is_down(self, mock_get):
        mock_get.return_value.status_code = 500
        main()  # Call the main function to monitor the website
        # Assert that an email and Slack alert were sent
        self.assertEqual(send_email_alert.called, True)
        self.assertEqual(send_slack_alert.called, True)

if __name__ == "__main__":
    unittest.main()
