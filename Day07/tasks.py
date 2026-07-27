# Exception Handling :- it is used to handle exceptions(errors) in our program while running.
#  it does not let programs to crash even if there is an error in the program.

try:
    num = 10 / 2
    print(num)

except ZeroDivisionError:
    print("Cannot divide by zero")

# prints out :-
# 5.0


# try :- The try block contains the code that may cause an exception.

try:
    print(10 / 0)

except ZeroDivisionError:
    print("Error occurred")

# prints out :-
# Error occurred


# except :- The except block executes only if an exception occurs.

try:
    print(10 / 0)

except ZeroDivisionError:
    print("Cannot divide by zero")

# prints out :-
# Cannot divide by zero


# else :- The else block executes only when no exception occurs.

try:
    print(10 / 2)

except ZeroDivisionError:
    print("Error")

else:
    print("Division Successful")

# prints out :-
# 5.0
# Division Successful


# finally :- The finally block executes not matter what.

try:
    print(10 / 0)

except ZeroDivisionError:
    print("Error")

finally:
    print("Program Finished")

# prints out :-
# Error
# Program Finished


# raise :- raise is used to create an exception manually.

age = 15

if age < 18:
    raise ValueError("Age must be 18 or above")

# prints out :-
# ValueError: Age must be 18 or above


# Custom Exception :- A custom exception is a user-defined exception
# created by inheriting from the Exception class.

class InvalidAgeError(Exception):
    pass

age = 16

if age < 18:
    raise InvalidAgeError("Invalid Age")

# prints out :-
# InvalidAgeError: Invalid Age


# Context Manager :- A Context Manager automatically manages resources
# it is used to open files and closes them automatically after use.

with open("sample.txt", "w") as file:
    file.write("Hello World")

# sample.txt is automatically closed.


# __enter__() :- __enter__() executes when entering the with block.

class Demo:

    def __enter__(self):
        print("Started")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Finished")

with Demo():
    print("Inside Block")

# prints out :-
# Started
# Inside Block
# Finished


# File Handling :- File handling is used to create, open, read, write, update and closing files using python
#instead of storing data inside variable which deletes the data after program ends we can use file which saves the data permanently

file = open("data.txt", "w")
file.write("Hello")
file.close()


# Reading a File:- read, r

with open("data.txt", "r") as file:
    print(file.read())


# Writing a File:- write, w

with open("data.txt", "w") as file:
    file.write("Python")


# Appending to a File:- write, a

with open("data.txt", "a") as file:
    file.write("\nBackend")

# Reading Entire file:- .read()

with open("data.txt","r") as file:
    print(file.read())

# Reading one line:

with open("data.txt", "r") as file:
    print(file.readline())

# Reading Multiple lines:

with open("data.txt", "r") as file:
    print(file.readlines())


# pathlib.Path :- Path is used to work with file and folder paths.

from pathlib import Path

path = Path("data.txt")

print(path.exists())

# prints out :- True


# CSV Files :- CSV stores data in rows and columns separated by commas.
# comma separated values

import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age"])
    writer.writerow(["Nitin", 22])


# JSON Files :- JSON stores data in key-value pairs.
# JavaScript object notation

import json

student = {
    "name": "Nitin",
    "age": 22
}

with open("student.json", "w") as file:
    json.dump(student, file)


# breakpoint() :- breakpoint() pauses the program and opens the debugger.

x = 10
y = 20

breakpoint()

print(x + y)


# traceback :- A traceback shows where an exception occurred
# and helps identify the exact line causing the error.

print(10 / 0)

# Traceback (most recent call last):
#   File "main.py", line 3
# ZeroDivisionError: division by zero