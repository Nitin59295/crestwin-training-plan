# @staticmethod :- A method that does not use self or cls.
# It behaves like a normal function inside a class.

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

print(Calculator.add(5, 3))

# prints out :-
# 8



# @classmethod :- A method that uses cls to access class variables.

class Calculator:
    operation = "Addition"
    @classmethod
    def add(cls, a, b):
        print(f"Operation: {cls.operation}")
        return a + b

print(Calculator.add(5, 3))
'''
prints out :- Operation: Addition
                8
'''
