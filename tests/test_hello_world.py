import unittest
from app.main import get_greeting

class TestGreeting(unittest.TestCase):
    def test_greeting(self):
        self.assertEqual(get_greeting(), "Welcome home")

if __name__ == "__main__":
    unittest.main()
