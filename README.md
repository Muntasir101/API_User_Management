# User Management API

This is a RESTful API project built with Python Flask for managing users. It provides endpoints for creating, listing, updating, and deleting user records.

## Prerequisites

- Python 3.7 or higher
- Flask web framework
- Virtual environment (recommended)

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/user-management-api.git
   
2. Navigate to the project directory:
  cd user-management-api
3. Create and activate a virtual environment (optional but recommended):
  python3 -m venv env
  source env/bin/activate
4. Install the required dependencies:
  pip install -r requirements.txt
5. Run the Flask development server:
  flask run
6. The API will be available at http://localhost:5000

## API Endpoints
Create a User
Endpoint: POST /users
Request Body:
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
Response:
{
  "message": "User created successfully",
  "user": {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
}
List Users
Endpoint: GET /users
Response:
{
  "users": [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    },
    {
      "id": 2,
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
  ]
}
Update a User
Endpoint: PUT /users/{user_id}
Request Body:
{
  "name": "Updated Name"
}
Response:
{
  "message": "User updated successfully"
}
Delete a User
Endpoint: DELETE /users/{user_id}
Response:
{
  "message": "User deleted successfully"
}
## Feel free to contribute to this project by opening issues or submitting pull requests. 
If you have any questions or suggestions, please contact your-email@example.com


Make sure to replace the placeholders (`your-username`, `your-email@example.com`) with your actual GitHub username and email address. Customize any other sections or details according to your project's requirements.

Feel free to include additional information, such as project structure, deployment instructions, or any specific considerations relevant to your API project.



