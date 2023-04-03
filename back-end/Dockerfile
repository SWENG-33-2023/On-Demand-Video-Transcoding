FROM python:3.8-alpine

#WORKDIR /code

# Upgrade python package mamager
RUN pip install --upgrade pip

# Caches the copy of requirements
COPY requirements.txt requirements.txt
# Install python requirements
RUN pip install --no-cache-dir -r requirements.txt

RUN apk --update --no-cache add curl ffmpeg fprobe 

# Copy from current directory to docker
COPY . . 

# api.py uses 4000
EXPOSE 4000

# Run command when docker run
CMD ["flask", "run", "--host=0.0.0.0"]
#CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
