import unittest
from app import app
from io import BytesIO

class ImageControllerTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_generate_image(self):
        with self.app.session_transaction() as sess:
            sess['username'] = 'user1'
        response = self.app.get('/image?width=100&height=100')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'image/png')

    def test_image_generation_unauthorized(self):
        response = self.app.get('/image?width=100&height=100', follow_redirects=True)
        self.assertIn(b'Login', response.data)

if __name__ == '__main__':
    unittest.main()
