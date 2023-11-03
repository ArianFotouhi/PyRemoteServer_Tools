from flask import Flask, request, jsonify
from auth import token_required, login

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def user_login():
    data = request.get_json()
    if 'username' in data and 'password' in data:
        username = data['username']
        password = data['password']
        token = login(username, password)
        if token:
            return jsonify({'token': token})
    return {'message': 'Invalid username or password'}, 401

@app.route('/route1')
@token_required
def route1():
    return {'message': 'Welcome to route1'}

@app.route('/route2')
@token_required
def route2():
    return {'message': 'Welcome to route2'}

if __name__ == '__main__':
    app.run(debug=True, port=8080)
