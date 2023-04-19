from flask import Flask, request, jsonify
from constants import API_KEY


app = Flask(__name__)

@app.before_request
def authenticate():
    if request.headers.get("X-Parse-REST-API-Key") != API_KEY:
        return jsonify({"error": "Invalid API key"}), 401
    
@app.route('/Devops', methods=['POST'])
def handle_devops():
    data = request.get_json()
    message = 'Hello ' + data['to'] + ' your message will be send'

    response = {'message': message}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5000)