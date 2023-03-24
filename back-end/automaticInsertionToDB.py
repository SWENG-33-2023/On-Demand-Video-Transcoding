import sqlite3, re
from rich.console import Console
from rich.table import Table

acceptedResolutions = ["640:480", "1280:720","1920:1080","2560:1440","3840:2160"]
acceptedCodecs = ["libx264"]

# Ask to add file, and do so if needed 
# Ensure file conforms to linux naming convention
# Below is essentially main
def gatherInformationPrompt(fileName, fileScale, fileEncoding, filePath):
    displayCurrentDatabase("video-database.db")
    getInfo(fileName, fileScale, fileEncoding, filePath)

# connect to db and add information
def addToDatabase(db, name, scale, path):
    conn = sqlite3.connect(db)

    cursor = conn.cursor()

    db_query = """INSERT INTO files
            (file_name, file_scale, file_path) VALUES (?, ?, ?)"""
    db_tuple = (name, scale, path)
    cursor.execute(db_query, db_tuple) # str converts bytes to string

    conn.commit()
    conn.close()


def getInfo(fileName, fileScale, fileEncoding):
    gettingInfo = True
    while (gettingInfo):
        boolNameTuple = getFileName(fileName)

        if not boolNameTuple[0]: 
            break;
        
        filePath = "./assets/" + boolNameTuple[0]
        boolScaleTuple = pickElementFromArray(fileScale, acceptedResolutions)
        
        if not boolScaleTuple[0]: 
            break;
        
        boolCodecTuple = pickElementFromArray(fileEncoding, acceptedCodecs)
        
        if not boolCodecTuple[0]:
            break;

        addToDatabase('video-database.db', boolNameTuple[1], boolScaleTuple[1], filePath)

        gettingInfo = False # end while loop

# Generic: Ask to gather information array and
# if information is not in array error out and return tuple (False,info)
# If not erroring, return (True,info)
def pickElementFromArray(arrayElement, arr):
    if arrayElement not in arr:
        print("Error: Invalid entry (" + arrayElement + ")")
        return (False, arrayElement)
    return (True, arrayElement)

# Name a file if conforms to linux naming convention
# Return False if it does not, and True if it does
def getFileName(fileName):
    addingFile = isForbiddenName(fileName)
    if not addingFile:
        print("Error: Invalid file name.")
        return False
    return (True, fileName)

# Given a Boolean if False print error 
# return the same Boolean
def isForbiddenName(file_name):
    search = re.search("/><|:&", file_name) 
    if search:
        print(  "Error: Inputted a character" +
                "that does not conform to linux" +
                "filenaming convention"
                )
    return search

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