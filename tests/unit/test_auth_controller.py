import unittest
from flask import session
from app import app

class AuthControllerTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'your_secret_key'
        self.app = app.test_client()

    def test_login_success(self):
        response = self.app.post('/login', data=dict(
            username='user1',
            password='password1'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        with self.app.session_transaction() as sess:
            self.assertEqual(sess['username'], 'user1')

    def test_login_failure(self):
        response = self.app.post('/login', data=dict(
            username='user1',
            password='wrongpassword'
        ), follow_redirects=True)
        self.assertIn(b'Invalid username or password', response.data)

    def test_logout(self):
        with self.app:
            with self.app.session_transaction() as sess:
                sess['username'] = 'testuser'

            response = self.app.get('/logout', follow_redirects=True)

            with self.app.session_transaction() as sess:
                self.assertNotIn('username', sess)

            self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
