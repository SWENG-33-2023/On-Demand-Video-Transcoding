FROM python:3.8-alpine

WORKDIR /code/back-end
# Copy from current directory to docker
COPY . .

ENV FLASK_APP=api.py
ENV FLASK_RUN_HOST=0.0.0.0

# Upgrade python package mamager
RUN pip install --upgrade pip

# Caches the copy of requirements commented out cos all copied in above
#COPY requirements.txt requirements.txt
# Install python requirements
RUN pip install -r requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt

# added the update / installation of ffmpeg
RUN apk --update --no-cache add curl ffmpeg fprobe 

# adding in sqlite
RUN apk --update --no-cache add curl sqlite

# Copy from current directory to docker
#COPY . .

# api.py uses 4000
EXPOSE 4000

# Run command when docker run
CMD ["python", "api.py"]


