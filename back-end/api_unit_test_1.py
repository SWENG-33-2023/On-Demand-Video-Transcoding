import unittest
from unittest.mock import patch
from api import app
import os

class TestTranscoder(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_transcoder(self):
        payload = {'mediaName': 'meerkats.mp4','mediaScale': '1280:720','mediaEncoding': 'h264','mediaNameOutput': 'video_output.mp4'}
        headers = {'Content-Type': 'application/json'}
        response = self.app.post('http://localhost:5000/transcoder', json=payload, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), '"Video Transcoded!"\n')
        print('transcoding status : ',response.data.decode('utf-8'))
        os.remove('../front-end/output-videos/video_output.mp4')

if __name__ == '__main__':
    unittest.main()
