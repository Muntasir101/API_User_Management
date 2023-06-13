from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = []
next_id = 1

"""
@app.route('/api/users', methods=['POST'])
def create_user():
    global next_id

    data = request.get_json()

    if 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Name and email are required'}), 400

    user = {
        'id': next_id,
        'name': data['name'],
        'email': data['email']
    }

    users.append(user)
    next_id += 1

    return jsonify({'users': users})
    #return jsonify({'message': 'User created successfully', 'user': user}), 201

"""


@app.route('/api/users', methods=['POST'])
def create_user():
    global next_id

    data = request.get_json()

    if 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Name and email are required'}), 400

    user = {
        'id': next_id,
        'name': data['name'],
        'email': data['email']
    }

    users.append(user)
    next_id += 1

    response = {
        'message': 'User created successfully',
        'user': user,
        'users': users  # Include the full list of users in the response
    }

    return jsonify(response), 201


@app.route('/api/users', methods=['GET'])
def get_users():
    global users

    if not users:
        response = requests.get('http://localhost:5000/api/users')
        if response.status_code == 200:
            users = response.json().get('users', [])

    return jsonify({'users': users})


@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()

    for user in users:
        if user['id'] == user_id:
            user['name'] = data.get('name', user['name'])
            user['email'] = data.get('email', user['email'])
            return jsonify({'message': 'User updated successfully', 'user': user})

    return jsonify({'error': 'User not found'}), 404


@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users

    for user in users:
        if user['id'] == user_id:
            users.remove(user)
            return jsonify({'message': 'User deleted successfully'})

    return jsonify({'error': 'User not found'}), 404


if __name__ == '__main__':
    app.run()
