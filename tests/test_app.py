''' sample docstring'''
import unittest
from flask import Flask
from flask.testing import FlaskClient
from unittest.mock import patchy
from flask_wtf import CSRFProtect                         #use CSRFProtect module
from flask_sslify import SSLify
from app import index

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        csrf = CSRFProtect(app)
        sslify = SSLify(app)
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = True      #enabled for testing
        self.client = self.app.test_client()

    def test_index(self):
        with patch('socket.gethostname') as mock_gethostname:
            mock_gethostname.return_value = 'test-hostname'
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Test Hostname:', response.data)
            self.assertIn(b'test-hostname', response.data)

    def test_index_exception(self):
        with patch('socket.gethostname') as mock_gethostname:
            mock_gethostname.side_effect = Exception('Test Exception')
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Error:', response.data)
            self.assertIn(b'Test Exception', response.data)

if __name__ == '__main__':
    unittest.main()
