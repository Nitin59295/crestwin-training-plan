# Async Python :- Async python is a way of running tasks without blocking the program.
# python can start working on another task instead of waiting for another task to finish

import asyncio

async def greet():
    print("Hello")
    await asyncio.sleep(2)
    print("Welcome")

asyncio.run(greet())

# prints out :-
# Hello
# (waits 2 seconds)
# Welcome


# async :- async tells python "this function can run asynchronously or continuously"

import asyncio

async def hello():
    print("Hello World")

asyncio.run(hello())

# prints out :-
# Hello World


# await :- it pauses the function until this task finishes. but let other async tasks continue to function.


import asyncio

async def task():
    print("Task Started")
    await asyncio.sleep(2)
    print("Task Finished")

asyncio.run(task())

# prints out :-
# Task Started
# (waits 2 seconds)
# Task Finished


# Event Loop :- Event loop is the core engine behind the Async python. its job it too:
# 1. manage all async tasks
# 2. checks which one is running and which one are not.
# 3. runs the tasks on the right time
# 4. schedules the tasks


import asyncio

async def greet():
    print("Hello")

asyncio.run(greet())

# asyncio.run() creates the Event Loop,
# runs the coroutine and closes the loop.


# asyncio.run() :-
# 1. used to create event loop
# 2. run the async function
# 3. close the event loop

import asyncio

async def main():
    print("Program Started")

asyncio.run(main())

# prints out :-
# Program Started


# asyncio.gather() :-
# 1. used to run multiple async functions continuously
# 2. waits until all of them are finished
import asyncio

async def task1():
    await asyncio.sleep(2)
    print("Task 1 Finished")

async def task2():
    await asyncio.sleep(2)
    print("Task 2 Finished")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())

# prints out :-
# Task 1 Finished
# Task 2 Finished


# asyncio.create_task() :- Starts an async task in the background.

import asyncio

async def task():
    await asyncio.sleep(2)
    print("Background Task Finished")

async def main():
    t = asyncio.create_task(task())

    print("Doing Other Work")

    await t

asyncio.run(main())

# prints out :-
# Doing Other Work
# Background Task Finished


# Threading :- Threading runs multiple threads inside one process.
# Threads share the same memory.

import threading
import time

def work():
    print("Working...")
    time.sleep(2)
    print("Done")

t = threading.Thread(target=work)

t.start()
t.join()

# prints out :-
# Working...
# Done


# Multiprocessing :- Multiprocessing runs multiple independent processes.
# Each process has its own memory.

from multiprocessing import Process
import time

def work():
    print("Working...")
    time.sleep(2)
    print("Done")

p = Process(target=work)

p.start()
p.join()

# prints out :-
# Working...
# Done


# Type Hints :- Type hints specify the expected data types of variables,
# function parameters and return values.

def add(a: int, b: int) -> int:
    return a + b

print(add(10, 20))

# prints out :-
# 30


# list[str] :- list[str] represents a list containing only strings.

names: list[str] = ["Nitin", "Rahul", "Aman"]

print(names)

# prints out :-
# ['Nitin', 'Rahul', 'Aman']


# Union :- Union allows a variable or parameter to accept
# more than one data type.

from typing import Union

def display(value: Union[int, str]):
    print(value)

display(10)
display("Hello")

# prints out :-
# 10
# Hello


# Optional :- Optional means the value can either be a given type
# or None.

from typing import Optional

def show(name: Optional[str]):
    print(name)

show("Nitin")
show(None)

# prints out :-
# Nitin
# None


# mypy :- mypy is a static type checker that checks type hints
# before the program runs.

def multiply(a: int, b: int) -> int:
    return a * b

multiply("5", 10)

# mypy output :-
# Argument 1 has incompatible type "str"; expected "int"