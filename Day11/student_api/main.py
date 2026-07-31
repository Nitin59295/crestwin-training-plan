from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

students = []

class Student(BaseModel):
    id: int
    name: str
    age: int
    course: str



@app.get("/students")
def get_students():
    return students


@app.post("/students")
def create_student(student: Student):
    students.append(student)
    return {
        "message": "Student created successfully",
        "student": student
    }
