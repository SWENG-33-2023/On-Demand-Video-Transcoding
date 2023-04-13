import unittest
from unittest.mock import patch
from app import app

class TestTranscoder(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_missing_file(self):
        payload = {
            'mediaName': 'invalid.mp4',
            'mediaScale': '1280:720',
            'mediaEncoding': 'h264',
            'mediaNameOutput': 'video_output.mp4'
        }
        headers = {'Content-Type': 'application/json'}
        response = self.app.post('http://localhost:4000/transcoder', json=payload, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), '"ERROR: Media not found."\n')

if __name__ == '__main__':
    unittest.main()
