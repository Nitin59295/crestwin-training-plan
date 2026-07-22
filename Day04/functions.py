# Functions :- function is a reusable block of code that executes a specific task only when it is called

# Define :- def is used to create or define a function

def greet():
    print("Hello!")

greet() #-- > prints out Hello!


# Return :- return sends a value back from a function when it is called

def add(a,b):
    return a+b
result = add(5,10)
print(result)
#prints out:- 15



# args:- these arguments allow any number of positional arguments.these are dependent upon the position itself.

def total(a,b,c):
    print(f"a: {a},b: {b},c: {c}")
total(3,2,4)
# prints out a: 3, b: 2, c: 4


def total(a,b,c):
    print(f"a: {a},b: {b},c: {c}")
total(3,2)
# prints out :- ERROR!
# Traceback (most recent call last):
#   File "<main.py>", line 3, in <module>
# TypeError: total() missing 1 required positional argument: 'c'



# *kwagrs :- these let function accept any number of keyword arguments

def student(**details):
    print(details)
student(name="Nitin", age=22)

# prints out :- {'name': 'Nitin', 'age': 22}



# Scope (LEGB Rule):- this tells where a variable can be accessed.
##-- Order -> Local -> Enclosing -> Global -> Built-in(LEGB)

x = 10      # Global variable:- can be used by anyone

def show():
    x = 20  # Local variable:- can only be used inside the function
    print(x)

show()
print(x)

