import unittest
from app.main import app
from bs4 import BeautifulSoup

class WelcomeModalTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_modal_html_present(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.data, 'html.parser')
        modal = soup.find('div', {'id': 'welcomeModal'})
        self.assertIsNotNone(modal, 'Modal div should be present')
        self.assertIn('welcome home', modal.get_text())

if __name__ == '__main__':
    unittest.main()
