#-- Data Types in python
from logging.config import dictConfig

x = 10 #-- int
y = 3.14 #-- float
name = "Nitin Bhatia" #-- string
is_valid = True #-- Boolean
z = None #-- None-type
print(type (x))
print(type(y))
print(type(is_valid))
print(type(z))

#--- Collections(List, Tuple, Dict, Set)

list = [1,2,3,4] #-- List
tuple = (1,2,3) #-- Tuple
dictionary = {"name":"Nitin","age":26} #-- Dict
Set = {1,2,3,4} #-- Set
print(type(list))
print(type(tuple))
print(type(dictionary))
print(type(Set))

print(f"Hi! i am {dictionary["name"]}, i am {dictionary["age"]} yr's old")

