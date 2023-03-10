import os # remove database file once done each test
import sys
# Tell python to search for python files in the previous directory '../'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database import Video # Import Videos class from database.py

# Tests to see if database can be created, then pass if so
def test_init():
    test_db = Video("test.db") 
    os.remove("test.db")
    test_db.db.close()
    pass
     
# Tests to see if insertion is possible, then pass if so
def test_insert_six():
    test_db = Video("test.db")
    test_db.insert_six("Test_SD","Test_480p","Test_4:3",
        "Test_640x480","Test_100MB",
        "Test_/videos/video1-sd.mkv")
    os.remove("test.db")
    test_db.db.close()
    pass
