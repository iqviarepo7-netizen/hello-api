"""Tests for the hello world alert function."""

import unittest
from unittest.mock import patch

from app.main import show_hello_world

class TestHelloWorld(unittest.TestCase):
    @patch("tkinter.messagebox.showinfo")
    def test_show_hello_world_calls_showinfo(self, mock_showinfo):
        # Call the function under test
        show_hello_world()
        # Assert that showinfo was called with the expected title and message
        mock_showinfo.assert_called_once_with("Hello", "Hello World")

if __name__ == "__main__":
    unittest.main()
