# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

# Define environment variables
ENV FLASK_APP=devops.py

# Run the command to start the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]