import unittest
from flask_testing import TestCase
from api import app

class TestAPI(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Sample Api Project!')

    def test_api_endpoint(self):
        response = self.client.get('/api')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'This is my API endpoint'})

if __name__ == '__main__':
    unittest.main()
