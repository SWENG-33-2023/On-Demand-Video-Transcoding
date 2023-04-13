import unittest
import json
from app import app

class TestTranscoder(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # executed after each test
    def tearDown(self):
        pass

    def test_transcode_video(self):
        # mock input data
        payload = {'mediaName': 'test.mp4','mediaScale': '1280:720','mediaEncoding': 'h264','mediaNameOutput': 'video_output.mp4'}
        headers = {'Content-Type': 'application/json'}
        response = self.app.post('http://localhost:4000/transcoder', json=payload, headers=headers)
        self.assertEqual(response.status_code, 200)
    
    def test_upload_video(self):
        payload = {'mediaName': 'test.mp4'}
        headers = {'Content-Type': 'application/json'}
        response = self.app.post('http://localhost:4000/addToDatabase', json=payload, headers=headers)
        self.assertEqual(response.status_code, 200)
        
    def test_transcode_video_error(self):
        # mock input data
        payload = {'mediaScale': '1280:720','mediaEncoding': 'h264','mediaNameOutput': 'video_output.mp4'}
        headers = {'Content-Type': 'application/json'}
        response = self.app.post('http://localhost:4000/transcoder', json=payload, headers=headers)
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
