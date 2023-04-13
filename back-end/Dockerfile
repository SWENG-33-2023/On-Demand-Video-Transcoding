FROM python:3.8-alpine

WORKDIR /code/back-end

# *Caches* the copy of requirements 
COPY requirements.txt requirements.txt

# Copy from current directory to docker (this can't be cached)
COPY . . 

# Upgrade python package mamager
RUN pip install --upgrade pip

# Install python requirements
RUN pip install -r requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt

# added the update / installation of ffmpeg
RUN apk --update --no-cache add curl ffmpeg fprobe 

# api.py uses 4000
EXPOSE 4000

# Run command when docker run
CMD ["flask", "run", "--host=0.0.0.0", "--port=4000"]
