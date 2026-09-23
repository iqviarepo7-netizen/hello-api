"""Test for the post‑login alert feature."""

import unittest
from unittest.mock import patch

from app.main import login

class TestWelcomeAlert(unittest.TestCase):
    def test_alert_called_on_successful_login(self):
        with patch("app.main.alert") as mock_alert:
            result = login("user", "pass")
            self.assertTrue(result)
            mock_alert.assert_called_once_with("Welcome World")

    def test_no_alert_on_failed_login(self):
        with patch("app.main.alert") as mock_alert:
            result = login("user", "wrong")
            self.assertFalse(result)
            mock_alert.assert_not_called()

if __name__ == "__main__":
    unittest.main()
