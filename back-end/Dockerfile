<<<<<<< HEAD
FROM python:3.8
WORKDIR /app
ADD back-end .
ADD requirements.txt .
=======
FROM python:3.8-alpine

WORKDIR /code

ENV FLASK_APP=api.py
ENV FLASK_RUN_HOST=0.0.0.0

# Upgrade python package mamager
RUN pip install --upgrade pip

# api.py uses 4000
EXPOSE 4000

# Caches the copy of requirements
COPY requirements.txt requirements.txt
# Install python requirements
>>>>>>> e9909238fb6681cdd0fb342a0a044f4ee481c8af
RUN pip install -r requirements.txt

# Copy from current directory to docker
COPY . .

# Run command when docker run
CMD ["python", "api.py"]
