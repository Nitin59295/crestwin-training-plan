# Dunder Methods (Magic Methods) :- Special methods that Python calls automatically to perform specific operations.

# __str__() :- Defines how an object is displayed when using print().

class Student:
    def __str__(self):
        return "Student: Nitin"

s1 = Student()

print(s1)

# prints out :-
# Student: Nitin



# __repr__() :- Defines the official string representation of an object.
# It is mainly used for debugging.

class Student:
    def __repr__(self):
        return "Student(name='Nitin', age=22)"

s1 = Student()

print(repr(s1))

# prints out :-
# Student(name='Nitin', age=22)



# __eq__() :- Defines how two objects are compared using ==.
# while using __eq__
class Student:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

s1 = Student("Nitin")
s2 = Student("Nitin")

print(s1 == s2)

# prints out :-
# True

# Without using __eq__

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Nitin")
s2 = Student("Nitin")

print(s1 == s2)

# prints out :-
# False