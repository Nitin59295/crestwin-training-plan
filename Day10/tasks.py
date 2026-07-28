# FastAPI :- FastAPI is a modern Python framework used to build fast and high-performance REST APIs quickly and effectively

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello FastAPI"}

# Visit :-
# http://127.0.0.1:8000/


# uvicorn :-it is an ASGI server it runs our fast api application

# Run the application using :- uvicorn main:app --reload

# main -> filename (main.py)
# app -> FastAPI object
# --reload -> Automatically restarts the server when code changes


# CORS (Cross-Origin Resource Sharing) :- it is a browser security feature that control whether a frontend from one origin is allowed to access a backend from different origin

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Routing :- it is a process of connecting URL's to a specific function

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome"}

@app.post("/student")
def create_student():
    return {"message": "Student Created"}

@app.put("/student")
def update_student():
    return {"message": "Student Updated"}

@app.delete("/student")
def delete_student():
    return {"message": "Student Deleted"}


# GET :- Used to retrieve data.

@app.get("/users")
def get_users():
    return {"users": ["Nitin", "Rahul"]}


# POST :- Used to create new data.

@app.post("/users")
def create_user():
    return {"message": "User Created"}


# PUT :- Used to update existing data.

@app.put("/users")
def update_user():
    return {"message": "User Updated"}

# PATCH :- partially updates the existing data


@app.patch("/users")
def update_user():
    return {"message": "User Updated"}


# DELETE :- Used to delete data.

@app.delete("/users")
def delete_user():
    return {"message": "User Deleted"}


# Path Parameters :- Values passed inside the URL.

@app.get("/students/{student_id}")
def get_student(student_id: int):
    return {"Student ID": student_id}

# Example :-
# /students/101


# Query Parameters :- Values passed after '?' in the URL.

@app.get("/students")
def get_student(age: int):
    return {"Age": age}

# Example :-
# /students?age=22


# Multiple Query Parameters

@app.get("/employee")
def employee(name: str, age: int):
    return {
        "Name": name,
        "Age": age
    }

# Example :-
# /employee?name=Nitin&age=22


# APIRouter :- APIRouter is used to organize routes into separate files. instead of writing all API's in one main.py we can divide them into multiple files.

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def users():
    return {"message": "Users Route"}

# Connect in main.py using :-
# app.include_router(router)


# Prefix :- Adds the same URL prefix to all routes.

from fastapi import APIRouter

router = APIRouter(prefix="/users")

@router.get("/")
def get_users():
    return {"message": "All Users"}

# URL :-
# /users


# Tags :- Groups related APIs in Swagger documentation.

from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/")
def get_users():
    return {"message": "Users"}


# Pydantic :- Pydantic validates incoming request data using BaseModel.

from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int


# BaseModel :- BaseModel defines the structure of request data.

from pydantic import BaseModel

class Employee(BaseModel):
    name: str
    salary: float


# Field :- Field() adds validation rules to model fields.

from pydantic import BaseModel, Field

class Student(BaseModel):

    name: str = Field(min_length=3, max_length=20)

    age: int = Field(gt=18)


# Validators :- Validators are used for custom validation.

from pydantic import BaseModel, field_validator

class Student(BaseModel):

    name: str

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):

        if len(value) < 3:
            raise ValueError("Name is too short")

        return value


# Nested Models :- A model can contain another model.

from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str

class Student(BaseModel):
    name: str
    age: int
    address: Address

# Example JSON :-
# {
#   "name": "Nitin",
#   "age": 22,
#   "address": {
#       "city": "Mandi",
#       "state": "Himachal Pradesh"
#   }
# }