# CRUD API :- A CRUD Api is a web service which allows users to perform 4 basic operations: Create, Read, Update, Delete

# CRUD APIs :- CRUD stands for Create, Read, Update and Delete.
# These are the four basic operations performed on data in a REST API.

# C -> Create (POST)
# R -> Read (GET)
# U -> Update (PUT)
# D -> Delete (DELETE)

# Example :-
# POST   /students      -> Create a student
# GET    /students      -> Read all students
# PUT    /students/1    -> Update student with ID 1
# DELETE /students/1    -> Delete student with ID 1


# Request Body :- A Request Body is the data sent by the client to the server, usually in JSON format.
# FastAPI automatically converts the JSON data into a Python object using pydantic models(base model)

request_body = {
   "name": "Nitin",
   "age": 22
}

# Example :-
# Client sends:
# {
#     "name": "Nitin",
#     "age": 22
# }


# Status Codes :- It is a 3digit numbers which are used to tell the users if the request is successful or not

# Common Status Codes

# 200 -> OK (Request Successful)
# 201 -> Created (New Resource Created)
# 204 -> No Content (Deleted Successfully)
# 400 -> Bad Request (Invalid Request)
# 401 -> Unauthorized (Authentication Required)
# 403 -> Forbidden (Permission Denied)
# 404 -> Not Found (Resource Does Not Exist)
# 422 -> Unprocessable Entity (Validation Failed)
# 500 -> Internal Server Error (Server Error)

# Example :-
# Student created     -> 201 Created
# Student not found   -> 404 Not Found


# HTTPException :- HTTPException is used to return an HTTP error
# response when something goes wrong.

# It allows you to:
# - Stop the execution of the current request.
# - Return an appropriate HTTP status code.
# - Send a meaningful error message to the client.

# Common uses:
# - Resource not found (404)
# - Invalid request (400)
# - Unauthorized access (401)
# - Permission denied (403)

# Example :-

raise HTTPException(
     status_code=404,
     detail="Student not found")


# CRUD Operations Summary

# GET    -> Read Data
# POST   -> Create Data
# PUT    -> Update Existing Data
# DELETE -> Delete Data


# Status Code Summary

# GET Success       -> 200 OK
# POST Success      -> 201 Created
# PUT Success       -> 200 OK
# DELETE Success    -> 204 No Content
# Resource Missing  -> 404 Not Found
# Invalid Request   -> 400 Bad Request
# Validation Failed -> 422 Unprocessable Entity
# Server Error      -> 500 Internal Server Error



# Dependency Injection (DI) :- it is a design pattern where an function get the required resources from outside. instead of creating itself
# In FastAPI, Dependency Injection is implemented using Depends().

# It helps to:
# - Reuse code
# - Avoid duplicate code
# - Make the application clean and easy to maintain


# Depends() :- Depends() tells FastAPI to execute another function
# before running the current route.

# Syntax :-

# parameter = Depends(function_name)


# Example :-

from fastapi import FastAPI, Depends

app = FastAPI()

def get_name():
    return "Nitin"

@app.get("/")
def home(name = Depends(get_name)):
    return {"name": name}


# Reusable Dependencies :- A reusable dependency is a function that can
# be used by multiple API routes.

from fastapi import FastAPI, Depends

app = FastAPI()

def check_login():
    return "User Verified"

@app.get("/students")
def get_students(user = Depends(check_login)):
    return {"message": user}

@app.get("/teachers")
def get_teachers(user = Depends(check_login)):
    return {"message": user}


# Common Uses of Dependency Injection

# - Database Connection
# - User Authentication
# - JWT Token Verification
# - API Key Validation
# - Logging
# - Configuration


# Benefits of Dependency Injection

# - Reusable code
# - Less code duplication
# - Cleaner code
# - Easier testing
# - Easier maintenance

# OpenAPI :- OpenAPI is a standard used to describe REST APIs. it endpoints,requests,bodies,responses etc
# FastAPI automatically generates API documentation using OpenAPI.

# Auto-generated Documentation

# /docs  -> Swagger UI (Interactive API Documentation)
# /redoc -> ReDoc (Read-only API Documentation)

# Visit:
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc


# Swagger (/docs)

# - Interactive API documentation
# - Allows testing APIs from the browser
# - Displays request body, responses and status codes


# ReDoc (/redoc)

# - Clean and readable API documentation
# - Mainly used for viewing API documentation
# - Does not focus on testing APIs


# Benefits of OpenAPI

# - Automatically generates API documentation
# - No need to write documentation manually
# - Easy API testing
# - Improves collaboration between frontend and backend developers

# Postman :- Postman is an API testing tool used to send HTTP requests
# and test APIs without creating a frontend application.


# Manual Endpoint Testing :- Manual Endpoint Testing means sending requests
# to API endpoints manually and checking the responses.

# It can be used to test:
# - GET Requests
# - POST Requests
# - PUT Requests
# - DELETE Requests
# - Request Body
# - Headers
# - Query Parameters
# - Path Parameters
# - Authorization


# Collections :- A Collection is a folder used to organize multiple
# API requests related to the same project.

# Example:
# Student API Collection
# ├── GET Students
# ├── POST Student
# ├── PUT Student
# └── DELETE Student


# Benefits of Postman

# - Test APIs without a frontend
# - Supports all HTTP methods
# - Organize requests using collections
# - Easy debugging and API testing
# - Share collections with team members

