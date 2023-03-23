import sqlite3, re
from rich.console import Console
from rich.table import Table

acceptedResolutions = ["640:480", "1280:720","1920:1080","2560:1440","3840:2160"]
acceptedCodecs = ["libx264"]

# Ask to add file, and do so if needed 
# Ensure file conforms to linux naming convention
# Below is essentially main
def gatherInformationPrompt():
    displayCurrentDatabase("video-database.db")
    currently_adding = True
    while(currently_adding):
        addFilePrompt = str(input("Do you wish to add a file?(y/n) "))
        if addFilePrompt != "y":
            break;
    
        getInfo()

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


def getInfo():
    currently_getting_info = True
    while (currently_getting_info):
        boolNameTuple = getFileName("What is the name of your file?")
        boolPathTuple = "./assets/" + boolNameTuple
        boolScaleTuple = pickElementFromArray(
            "What resolution is this media? Accepted resolutions:", 
            acceptedResolutions, 
            "Error: Forbidden resolution."
        )
        
        if not boolScaleTuple[0]: 
            break;
        
        boolCodecTuple = pickElementFromArray(
            "What encoding is this media in? Accepted codecs:", 
            acceptedCodecs, 
            "Error: Forbidden codec."
            )
        
        if not boolCodecTuple[0]:
            break;
        
        currently_getting_info = False # end while loop

        addToDatabase('video-database.db', boolNameTuple[1], boolScaleTuple[1], boolPathTuple)

# Generic: Ask to gather information array and
# if information is not in array error out and return tuple (False,info)
# If not erroring, return (True,info)
def pickElementFromArray(question, arr, error_str):
    print(question)
    print(arr)
    info = str(input())
    if info not in arr:
        print(error_str)
        return (False,info)
    return (True,info)

# Name a file if conforms to linux naming convention
# Return False if it does not, and True if it does
def getFileName(question):
    file_name = str(input(question))
    addingFile = isForbiddenName(file_name)
    if not addingFile:
        return False
    return (True, file_name)
    # Naming file logic goes here #

def maybe_get_path(question):
    file_path = str(input(question))
    return (file_path)

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
    table.addColumn("file_name", justify="right", style="cyan", no_wrap=True)
    table.addColumn("file_scale", style="magenta")
    table.addColumn("file_path", justify="right", style="green")
    for row in cursor:
        table.addRow(row[0], row[1], row[2])
    
    console = Console()
    console.print(table)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    gatherInformationPrompt()