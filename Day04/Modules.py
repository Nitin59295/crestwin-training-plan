# Modules :- A module is a Python file that contains reusable code (functions, variables, etc.).

# import :- Used to bring a module into your program.

import math

print(math.sqrt(25))
# prints out :- 5.0



# Standard Library (stdlib) :- A collection of built-in Python modules. No installation is required.
# Examples: math, os, sys, pathlib



# os Module :- Used to work with files, folders, and directories.

import os

print(os.getcwd())
# prints out :- Current Working Directory



# sys Module :- Provides information about the Python interpreter.

import sys

print(sys.version)
# prints out :- Python version



# pathlib Module :- Used to work with file and folder paths in a simple way.

from pathlib import Path

file = Path("notes.txt")

print(file.exists())
# prints out :- True (if file exists)
# prints out :- False (if file doesn't exist)