import sqlite3, re
from rich.console import Console
from rich.table import Table
import subprocess, re, os

acceptedResolutions = ["640:480", "1280:720","1920:1080","2560:1440","3840:2160"]
acceptedCodecs = ["libx264"]

# Ask to add file, and do so if needed 
# Ensure file conforms to linux naming convention
# Below is essentially main
def getInfo(fileName, fileFolder):
    if fileFolder == "assets":
        boolNameTuple = getFileName(fileName)
    else:
        boolNameTuple = getFileName("TRANSCODED" + fileName)

    if not boolNameTuple[0]: 
        return False;

    if fileFolder == "assets":
        addToDatabase('video-database.db', boolNameTuple[1], fileFolder)
    else: 
        addToDatabase('video-database.db', boolNameTuple[1], fileFolder)

    displayCurrentDatabase("video-database.db")
    return True

# connect to db and add information
def addToDatabase(db, name, path):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    db_query = """INSERT INTO files (file_name, file_scale, file_path) VALUES (?, ?, ?)"""
    db_tuple = (name, getResolution(name, path), path)

    cursor.execute(db_query, db_tuple) # str converts bytes to string

    conn.commit()
    conn.close()

def getResolution(name, fileFolder):
    if fileFolder == "assets":
        getFileInfoCommandArray = ['ffprobe', "-v", "error", "-select_streams", "v", "-show_entries", "stream=width,height", "-of", "csv=p=0:s=x", "./assets/" + name]
        ffprobeProcess = subprocess.Popen(getFileInfoCommandArray, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ffprobeResult, ffprobeError = ffprobeProcess.communicate()

        if ffprobeError:
            print(ffprobeError)
            return "Error: Could not find resolution"
        
        ffprobeResultString = ffprobeResult.decode("utf-8")
        dimensions = ffprobeResultString.split("x")
        return (dimensions[0] + ":" + dimensions[1])
    else:
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        parentDir = os.path.abspath(os.path.join(__location__, os.pardir))
        print(parentDir)
        getFileInfoCommandArray = ['ffprobe', "-v", "error", "-select_streams", "v", "-show_entries", "stream=width,height", "-of", "csv=p=0:s=x", parentDir + "/front-end/output-videos/" + name]
        ffprobeProcess = subprocess.Popen(getFileInfoCommandArray, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ffprobeResult, ffprobeError = ffprobeProcess.communicate()

        if ffprobeError:
            print(ffprobeError)
            return "Error: Could not find resolution"
        
        ffprobeResultString = ffprobeResult.decode("utf-8")
        dimensions = ffprobeResultString.split("x")
        return (dimensions[0] + ":" + dimensions[1])

# Name a file if conforms to linux naming convention
# Return False if it does not, and True if it does
def getFileName(fileName):
    if isForbiddenName(fileName):
        print("Error: Invalid file name.")
        return (False, fileName)
    return (True, fileName)

# Given a Boolean if False print error 
# return the same Boolean
# I may have messed this up - FionnCL
def isForbiddenName(file_name):
    search = re.search("[/><|:& ]", file_name) 
    if search != None:
        print(  "Error: Inputted a character" +
                "that does not conform to linux" +
                "filenaming convention"
                )
        return True
    return False

def displayCurrentDatabase(db):
    conn = sqlite3.connect(db)

    cursor = conn.cursor()

    db_query = """SELECT * FROM files"""
    cursor.execute(db_query)

    # make pretty table of current database
    table = Table(title = db)
    table.add_column("file_name", justify="right", style="cyan", no_wrap=True)
    table.add_column("file_scale", style="magenta")
    table.add_column("file_path", justify="right", style="green")
    for row in cursor:
        table.add_row(row[0], row[1], row[2])
    
    console = Console()
    console.print(table)

    conn.commit()
    conn.close()