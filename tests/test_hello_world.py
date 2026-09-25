import unittest
from app.main import app

class TestRunPipeline(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_run_pipeline_popup(self):
        """Verify that the /run-pipeline endpoint returns the expected
        welcome message and a 200 OK status.
        """
        response = self.client.get('/run-pipeline')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'welcome home')

if __name__ == '__main__':
    unittest.main()
