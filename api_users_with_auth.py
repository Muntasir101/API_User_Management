from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

users = []
next_id = 1

# A dictionary to store the API tokens and their corresponding users
api_tokens = {
    'secret_token': 'admin',
    'another_token': 'user'
}

# Endpoint for creating a new user
@app.route('/api/users', methods=['POST'])
def create_user():
    # Check if the API token is provided in the request headers
    if 'Authorization' not in request.headers:
        return jsonify({'error': 'Missing authorization token'}), 401

    # Extract the token from the request headers
    token = request.headers['Authorization']

    # Check if the token is valid
    if token not in api_tokens:
        return jsonify({'error': 'Invalid authorization token'}), 401

    # Get the user from the request body
    user = request.json.get('user')

    # Perform user creation logic (e.g., save the user to a database)
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

    return jsonify({'message': 'User created successfully'}), 201

@app.route('/api/users', methods=['GET'])
def get_users():
    # Check if the API token is provided in the request headers
    if 'Authorization' not in request.headers:
        return jsonify({'error': 'Missing authorization token'}), 401

    # Extract the token from the request headers
    token = request.headers['Authorization']

    # Check if the token is valid
    if token not in api_tokens:
        return jsonify({'error': 'Invalid authorization token'}), 401

    global users

    if not users:
        response = requests.get('http://localhost:5000/api/users')
        if response.status_code == 200:
            users = response.json().get('users', [])

    return jsonify({'users': users})

@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    # Check if the API token is provided in the request headers
    if 'Authorization' not in request.headers:
        return jsonify({'error': 'Missing authorization token'}), 401

    # Extract the token from the request headers
    token = request.headers['Authorization']

    # Check if the token is valid
    if token not in api_tokens:
        return jsonify({'error': 'Invalid authorization token'}), 401

    data = request.get_json()

    for user in users:
        if user['id'] == user_id:
            user['name'] = data.get('name', user['name'])
            user['email'] = data.get('email', user['email'])
            return jsonify({'message': 'User updated successfully', 'user': user})

    return jsonify({'error': 'User not found'}), 404

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    # Check if the API token is provided in the request headers
    if 'Authorization' not in request.headers:
        return jsonify({'error': 'Missing authorization token'}), 401

    # Extract the token from the request headers
    token = request.headers['Authorization']

    # Check if the token is valid
    if token not in api_tokens:
        return jsonify({'error': 'Invalid authorization token'}), 401

    global users

    for user in users:
        if user['id'] == user_id:
            users.remove(user)
            return jsonify({'message': 'User deleted successfully'})

    return jsonify({'error': 'User not found'}), 404


if __name__ == '__main__':
    app.run()
