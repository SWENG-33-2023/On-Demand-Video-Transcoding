from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse
import sqlite3
import os

<<<<<<< HEAD
=======
# automatic database insertion file
from automaticInsertionToDB import getInfo

>>>>>>> e9909238fb6681cdd0fb342a0a044f4ee481c8af
# creates api app
app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])
api = Api(app)

# location of the back-end folder on our machines
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

class transcoder(Resource):
    def post(self):
        parser = reqparse.RequestParser() # checks for requirements
        parser.add_argument('mediaName', required = True)
        parser.add_argument('mediaScale', required = True)
        parser.add_argument('mediaEncoding', required = True)
        parser.add_argument('mediaNameOutput', required = True)

        args = parser.parse_args()

<<<<<<< HEAD
=======
        # automatically stores the user's video to the database
        if not getInfo(args['mediaName'], "assets"):
            return "Video cannot be added to database."
        
>>>>>>> e9909238fb6681cdd0fb342a0a044f4ee481c8af
        db_path = os.path.join(__location__, 'video-database.db')
        db_connection = connection(db_path)

        # creates db cursor
        main_cursor = db_connection.cursor()

        # searches for requested file
        file_name = main_cursor.execute("SELECT file_name FROM files WHERE file_name = '" +  args['mediaName'] + "'")
        
        file_name = main_cursor.fetchone()

        # if the file is found
<<<<<<< HEAD
        if (file_name[0] != args['mediaName']):
            db_connection.close()
            return "ERROR: Media not found."
        # else gets the file_path
        file_media = main_cursor.execute("SELECT file_path FROM files WHERE (file_name='" +  args['mediaName'] + "')")
        file_media = main_cursor.fetchone()

        # transcode video (unless it's a duplicate output filename)
        os.system(  "ffmpeg -n -i " + __location__ + "/assets/" + args['mediaName'] +
                    " -vf scale=" + args['mediaScale'] +
                    " -c:v " + args['mediaEncoding'] + " -preset veryslow"  +
                    " ../front-end/output-videos/" + args['mediaNameOutput']
                  )

        #closes database connection
        db_connection.close()

        # success message if video found
        return "Video Transcoded!"
=======
        if(file_name[0] == args['mediaName']):
            # transcodes video
            os.system(  "ffmpeg -i " + __location__ + "/assets/" + args['mediaName'] + 
                        " -vf scale=" + args['mediaScale'] +
                        " -c:v " + args['mediaEncoding'] + " -preset veryslow"  +
                        " ../front-end/output-videos/" + "TRANSCODED" + args['mediaNameOutput'])           

            #closes database connection
            db_connection.close()

            # adds transcoded file to db
            getInfo(args['mediaName'], "output-videos")

            # success message if video found
            return "Video Transcoded!"
        else:
            # error message if video found
            db_connection.close()
            return "ERROR: Media not found."
>>>>>>> e9909238fb6681cdd0fb342a0a044f4ee481c8af

# API endpoint
api.add_resource(transcoder, '/transcoder')

# db connection 
# NOTE: Should probably have a try catch statement
def connection(db):
    conn = sqlite3.connect(db)
    return conn

# runs program if running from this file
if __name__ == '__main__':
    app.run(port=4000, debug=True)
