import os
import sqlite3

class Video:
    def __init__(self, database_name):
        # extract filename (no extension, e.g. videos.db -> videos
        self.db_name = os.path.splitext(database_name)[0] 
        self.db = sqlite3.connect(database_name) # Connect to database
        self.cursor = self.db.cursor() # Create cursor
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS 
            {}(Resolution, Name, Aspect_Ratio, 
               Pixel_Size, File_Size, File_Location)""".format(self.db_name))
        self.db.commit() 

    def insert_six(self, resolution, name, aspect_ratio, 
               pixel_size, file_size, file_location):
        self.cursor.execute("""INSERT INTO {} VALUES
            (?,?,?,?,?,?)""".format(self.db_name), (resolution, name, 
                                    aspect_ratio, pixel_size,
                                    file_size, file_location))
        self.db.commit()

    def search_column(self, column, row):
        #return self.cursor.execute("SELECT (?) FROM videos", (column,))
        return self.cursor.execute("""
            SELECT * FROM {} WHERE {} = '{}'""".format(self.db_name,column,row))

def main():
    videos = Video("videos.db") # Create Video object if not yet created
    # Some examples on how to run these python methods
    videos.insert_six("SD","480p","4:3","640x480","100MB","/videos/video1-sd.mkv")
    videos.insert_six("SD","480p","4:3","640x480","100MB","/videos/video2-sd.mkv")
    videos.insert_six("HD","720p","16:9","1280x720","300MB","/videos/video2-hd.mkv")
    res = videos.search_column("Resolution","SD")
    print(res.fetchall()) # prints result of everything that matched with SD
    videos.db.close()

if __name__ == "__main__":
    main()
