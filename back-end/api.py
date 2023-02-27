from flask import Flask
from flask_restful import Resource, Api, reqparse
import sqlite3
import os

# creates api app
app = Flask(__name__)
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

        db_path = os.path.join(__location__, 'video-database.db')
        db_connection = connection(db_path)

        # creates db cursor
        main_cursor = db_connection.cursor()

        # searches for requested file
        file_name = main_cursor.execute("SELECT file_name FROM files WHERE file_name = '" +  args['mediaName'] + "'")
        
        file_name = main_cursor.fetchone()

        # if the file is found
        if(file_name[0] == args['mediaName']):
            # gets the file_path
            file_media = main_cursor.execute("SELECT file_path FROM files WHERE (file_name='" +  args['mediaName'] + "')")
            file_media = main_cursor.fetchone()

            # transcodes video
            os.system(  "ffmpeg -i " + __location__ + "/assets/" + args['mediaName'] + 
                        " -vf scale=" + args['mediaScale'] +
                        " -c:v " + args['mediaEncoding'] + " -preset veryslow"  +
                        " ../front-end/output-videos/" + args['mediaNameOutput'] 
            )           

            #closes database connection
            db_connection.close()

            # success message if video found
            return "Video Transcoded!"
        else:
            # error message if video found
            db_connection.close()
            return "ERROR: Media not found."

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