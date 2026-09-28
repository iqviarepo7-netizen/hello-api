import unittest
from app.main import app

class WelcomeModalTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_modal_html_present(self):
        """Ensure the modal div and message are present in the rendered page"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        html = response.get_data(as_text=True)
        # Check modal container exists
        self.assertIn('id="welcomeModal"', html)
        # Check the exact message is present
        self.assertIn('welcome home', html)
        # Check the Run Pipeline button exists
        self.assertIn('id="runPipelineBtn"', html)

if __name__ == '__main__':
    unittest.main()
