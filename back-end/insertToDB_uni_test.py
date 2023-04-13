import sqlite3
import unittest
from unittest.mock import patch
from insertToDB import maybe_add_gather_file_and_info

class TestAddInformationToDB(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect('video-database.db')
        self.cursor = self.db.cursor()
        #self.cursor.execute('CREATE TABLE files (file_name text, file_scale text, file_path text)')

    def test_add_information_to_db(self):
        #add_information_to_db(self.db, 'test_file.mp4', '1920:1080', '/path/to/test_file.mp4')
        maybe_add_gather_file_and_info()
        self.cursor.execute('SELECT * FROM files WHERE file_name = ?', ('meerkats.mp4',))
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[1], '1920:1080')
        self.assertEqual(result[2], './assets/meerkats.mp4')
        self.cursor.execute('DELETE FROM files where file_name = ?', ('meerkats.mp4',))

    def tearDown(self):
        self.db.close()

if __name__ == '__main__':
    unittest.main()
