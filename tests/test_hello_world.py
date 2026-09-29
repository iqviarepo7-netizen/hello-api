import unittest
from app import main

class TestAppStartup(unittest.TestCase):
    def test_startup_success(self):
        """Ensure the application starts without errors and returns True."""
        result = main.start_app()
        self.assertTrue(result, "The application did not start successfully")

if __name__ == "__main__":
    unittest.main()
