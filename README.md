# Devops Microservice

This microservice allows you to send a message to a recipient with a specified sender and timestamp.

## Requirements
To run this microservice, you will need:

* Python 3.7 or later
* Docker

## Dependencies

This microservice requires Python 3 and the following packages:

- Flask
- PyJWT

## Installation (local)
* Clone this repository:
```shell
$ git clone https://github.com/<your-username>/devops-microservice.git
$ cd devops-microservice
```

* Install the Python dependencies:
```shell
$ pip install -r requirements.txt
```
* Build and run docker
```shell
$ docker build -t mycropython:v1 .
$ docker run --name micropy -d -p 8080:5000 micropython:v1


## API Key and JWT
This microservice requires an API key and JWT for authorization. You can set the API key and JWT in the constants.py file.

### Request Format
The microservice accepts POST requests in JSON format. The following fields are required:

* message: The message to send.
* to: The recipient of the message.
* from: The sender of the message.
* timeToLifeSec: The timestamp for the message.

In addition, the following headers are required:

* X-Parse-REST-API-Key: The API key for authorization.
* X-JWT-KWY: The JWT for authorization.

```
curl -X POST \
  http://localhost:8080/Devops \
  -H 'Content-Type: application/json' \
  -H 'X-Parse-REST-API-Key: 2f5ae96c-b558-4c7b-a590-a501ae1c3f6c' \
  -H "X-JWT-KWY: jwt-token" \
  -H "Content-Type: application/json" \
  -d '{
        "message": "this is a test",
        "to": "Wilmer",
        "from": "Rita Asturia",
        "timeToLifeSec̈́": "2023-04-19T12:00:00Z"
      }'
```

## Response Format
The microservice returns a JSON response in the following format:

```json
{"message":"Hello Wilmer your message will be send"}
```