# 1. Write a program to handle ZeroDivisionError.

a = int(input("Type value of A: "))
b = int(input("Type value of B: "))

try:
    # Write the division here
    result = ...

    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero")


# 2. Create a custom exception called InvalidSalaryError.

class InvalidSalaryError(Exception):
    pass
salary = int(input("Enter your Salary: "))
try:
    if salary <= 0:
        raise InvalidSalaryError("Enter a valid amount")
    print("Salary Added Successfully")
except InvalidSalaryError as e:
    print(e)

# 3. Read a text file using with.

from pathlib import Path

location = Path("Data.txt")

with open(location, "r") as file:
    print(file.read())


# 4. Write data into a file and append another line.

from pathlib import Path

location = Path("Data.txt")
#write
with open(location,"w") as file:
    file.write("Hello my name")
# append
with open(location,"a") as file:
    file.write("\nis Nitin.")


# 5. Check whether a file exists using pathlib.

from pathlib import Path

location = Path("data.txt")
print(location.exists())


# 6. Create a CSV file containing Name and Marks.

import csv

with open("student.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Header
    writer.writerow(["Name", "Marks"])

    # Data
    writer.writerow(["Nitin", 95])


# 7. Read data from a JSON file.

from pathlib import Path
import json

location = Path("data.json")

with open(location, "r") as file:
    data = json.load(file)

print(data)


# 8. Create your own Context Manager using __enter__() and __exit__().

class MyContextManager:

    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")


with MyContextManager():
    print("Inside the with block")






