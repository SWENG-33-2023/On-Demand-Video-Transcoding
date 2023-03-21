import sqlite3
import unittest

from createTableInDB import add_table_to_db

class TestAddTableToDB(unittest.TestCase):
    def setUp(self):
        self.test_db = sqlite3.connect('video-database.db')
        self.test_db_cursor = self.test_db.cursor()

    def tearDown(self):
        self.test_db.close()

    def test_add_table_to_db(self):
        add_table_to_db('video-database.db')

        self.test_db_cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='files'")
        result = str(self.test_db_cursor.fetchone())
        self.assertIsNotNone(result, "Table 'files' not found in the database")

        self.test_db_cursor.execute("PRAGMA table_info('files')")
        columns = self.test_db_cursor.fetchall()
        self.assertIsNotNone(columns)

        #self.test_db_cursor.execute("DROP TABLE 'files'")
        #self.test_db.commit()

if __name__ == '__main__':
    unittest.main()
