#-- List Comprehensions:- It is a concise way of writing a list using loops and conditional statements.
#                         these are used make code clutter free and easy to read and manage.

squares = [x ** 2 for x in range(5)]
print(squares)


evens = [x for x in range(11) if x%2==0]
print(evens)

odds = [x for x in range(11) if x%2!=0]
print(odds)

#-- dict comprehensions

squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)

#-- set comprehension

odd_set = {x for x in range(10) if x%2!=0}
print(odd_set)




