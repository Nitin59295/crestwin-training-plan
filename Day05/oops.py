# Oops :- oops is a way of writing code using CLASS and OBJECTS for making code organized, reusable and easy to manage

# class :- A class is a blueprint or template for creating Objects. it defines what variables and functions an object should have

class Student:
    pass
s1 = Student()

# object = An object is an instance of class

class Student:           # CLASS
    pass
s1 = Student()           # OBJECT
s2 = Student()           #OBJECT


# Encapsulation:- it is a process of wrapping VARIABLES and FUNCTIONS inside a class and restricting access to the class:
#Types:- 1. public, 2. protected(_), 3. private(__)

class BankAccount:
    def __init__(self):
        self.__balance = 1000

    def deposit(self,amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
account = BankAccount()
account.deposit(500)
print(account.get_balance())


# Abstraction : it is a process of hiding internal details and showing only necessary features to the user

class CoffeeMachine:
    def make_coffee(self):
        print("Coffee is ready!")

machine = CoffeeMachine()
machine.make_coffee()

# Inheritance : it is a process in which one child class acquires properties of another class
# Types : 1. Single, 2. Multiple, 3. Multilevel, 4. Hierarchical, 5. Hybrid

class Animal:
    def sound(self):
        print("Animal sound")
class Dog(Animal):
    def sound(self):
        pass
d = Dog()
d.sound()


# super() :- super() is used to call the parent class constructor or methods from the child class

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

d = Dog("Tommy")

print(d.name)

# prints out :-
# Tommy


# Polymorphism :- it is a process where the same method behaves differently in different classes

class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

d = Dog()
c = Cat()

d.sound()
c.sound()

# prints out :-
# Dog barks
# Cat meows

# MRO (Method Resolution Order) :- MRO tells the order in which Python searches for methods in inheritance.

class A:
    def show(self):
        print("Class A")

class B(A):
    pass

class C(B):
    pass

obj = C()
obj.show()

# prints out :-
# Class A

print(C.mro())

# prints out :-
# [<class '__main__.C'>,
#  <class '__main__.B'>,
#  <class '__main__.A'>,
#  <class 'object'>]
