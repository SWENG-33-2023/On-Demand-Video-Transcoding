# On-Demand-Video-Transcoding

Software Engineering Project with ShutterStock  
Project is from a Trinity Module for third and second years

## Project Information

We have been tasked with creating an on demand video transcoding application.
We will be using ReactJS for the front end and a Python API using flask for the majority of the back end.

### Project Installation
* The simplest way to run the project is to have docker and docker-compose installed in the system and 
  running the script named `./runDocker.sh` which will install and setup the enviornment for running the application.
* The programme can also be run locally, this requires installing the libraries manually, which can be found in
  `back-end/requirement.txt`, `ffmpeg` and `fprobe` manually for the back-end, and `npm ci --omit=dev`. Open two terminals, one for back-end, one
  for front-end and run the applications, `flask run --host=0.0.0.0 --port=4000`, and for front-end inside the `src/`
  directory run with `node App.js`.

### Contributors

* Third Years
  * Shohinabonu Shamshodova
  * Stephen Day
  * Alexander Sepelenco
  * Al-Ani Ali
* Second Years
  * Kate O Neill
  * Fionn Camacho Lenihan
  * Shaurya Gaurav Varma
  * Nalin Verma
  * Rehann Viswanathan
  * Yuxin Wan
