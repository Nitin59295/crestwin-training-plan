# ABC (Abstract Base Class) :- Abstract base class is a blueprint of other class. but it does not create an object.
# it forces other class to follow or implement certain methods

from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def work(self):
        pass


class Developer(Employee):

    def work(self):
        print("Writing Code")


d = Developer()
d.work()

# prints out :-
# Writing Code


# Protocol :- A Protocol defines what methods or attributes a class should have.
# if a class already have required methods then it does not need to inherit from another class
# "if a class has required methods it follows the protocol"

from typing import Protocol

class Animal(Protocol):

    def sound(self):
        pass


class Dog:

    def sound(self):
        print("Dog barks")


def make_sound(animal: Animal):
    animal.sound()


d = Dog()
make_sound(d)

# prints out :-
# Dog barks


# Composition :- Composition is a "has-a" relationship where one class contains an object of another class instead of inheriting from it.

class Engine:

    def start(self):
        print("Engine Started")


class Car:

    def __init__(self):
        self.engine = Engine()

    def drive(self):
        self.engine.start()
        print("Car is moving")


car = Car()
car.drive()

# prints out :- Engine Started , Car is moving


# Decorator :- A decorator is a function that wraps around another function to adds extra functionality without changing its original code.

def decorator(func):

    def wrapper(a, b):
        print("Calculation Started")
        func(a, b)

    return wrapper


@decorator
def add(a, b):
    print(a + b)


add(5, 3)

# prints out :- Calculation Started, 8


# Decorator Chaining :- Decorator chaining means applying multiple decorators to the same function.

def decorator1(func):

    def wrapper():
        print("Decorator 1")
        func()

    return wrapper


def decorator2(func):

    def wrapper():
        print("Decorator 2")
        func()

    return wrapper


@decorator1
@decorator2
def greet():
    print("Hello")


greet()

# prints out :-
# Decorator 1
# Decorator 2
# Hello


# PEP 8 :- PEP 8 is Python's official style guide for writing
# clean, readable and consistent code.


# Black :- Black is an automatic code formatter that formats
# Python code according to PEP 8.


# isort :- isort automatically sorts and organizes Python imports.


# Google Docstrings :- Google Docstrings provide a standard format for documenting functions and classes.

def add(a, b):
    """
    Adds two numbers.

    Args:
        a: First number.
        b: Second number.

    Returns:
        Sum of a and b.

    return a + b
    """


# Logging :- Logging records what happens while a program runs. It is mainly used for debugging and monitoring applications.

import logging

logging.basicConfig(level=logging.INFO)

logging.info("Application Started")
logging.warning("Low Battery")
logging.error("File Not Found")

# prints out :-
# INFO:root:Application Started
# WARNING:root:Low Battery
# ERROR:root:File Not Found


# Logging Levels :-
# DEBUG    -> Detailed debugging information.
# INFO     -> Normal program events.
# WARNING  -> Something unexpected happened.
# ERROR    -> An operation failed.
# CRITICAL -> A serious error that may stop the program.


# Handlers :- Handlers decide where log messages are sent.
# Example: Console, File, Email.


# Formatters :- Formatters decides how our log message should look like to the developer



