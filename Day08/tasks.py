# Generators :- A generator is a function that uses yield instead of return. because return gives the output and function dies
# where as yield gives the output and pauses the function and waits for the user for next input

def numbers():
    yield 1
    yield 2
    yield 3

for i in numbers():
    print(i)

# prints out :-
# 1
# 2
# 3


# yield :- yield pauses the function, returns a value, and resumes when user gives next() command
# starts execution from where the program is paused

def count():
    yield 1
    yield 2
    yield 3

gen = count()

print(next(gen))
print(next(gen))
print(next(gen))

# prints out :-
# 1
# 2
# 3


# itertools :- itertools is a built-in module that provides fast and efficient tools for working with iterables

from itertools import chain, islice, groupby

# chain() :- chain() combines multiple iterables into one iterable.

list1 = [1, 2, 3]
list2 = [4, 5, 6]

for i in chain(list1, list2):
    print(i)

# prints out :-
# 1
# 2
# 3
# 4
# 5
# 6


# islice() :- islice() returns a selected portion of an iterable.

numbers = [10, 20, 30, 40, 50]

for i in islice(numbers, 1, 4):
    print(i)

# prints out :-
# 20
# 30
# 40


# groupby() :- groupby() groups similar values together.

names = ["A", "A", "B", "B", "C"]

for key, group in groupby(names):
    print(key, list(group))

# prints out :-
# A ['A', 'A']
# B ['B', 'B']
# C ['C']


# functools :- functools is a built-in module that provides helper functions for working with other functions.

from functools import partial, lru_cache, reduce


# partial() :- partial() fixes some arguments of a function so we do not need to be pass them every time.

from functools import partial

def multiply(a, b):
    return a * b

multiply_by_5 = partial(multiply, b=5)

print(multiply_by_5(10))

# prints out :-
# 50


# lru_cache() :- lru_cache() stores the results of function in memory. if the same input is used again python gives the output instantly  without calculating

from functools import lru_cache

@lru_cache
def square(n):
    print("Calculating...")
    return n * n

print(square(5))
print(square(5))

# prints out :-
# Calculating...
# 25
# 25


# reduce() :- reduce() applies a function to an iterable again and again until a single value remains.

from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda x, y: x + y, numbers)

print(result)

# prints out :-
# 10


# lambda :- it is a small anonymous function created by using keyword lambda.

square = lambda x: x * x

print(square(5))

# prints out :-
# 25


# map() :- map() applies a function to every element of an iterable.

numbers = [1, 2, 3, 4]

result = map(lambda x: x * 2, numbers)

print(list(result))

# prints out :-
# [2, 4, 6, 8]


# filter() :- filter() appies a function to only those elements which satisfies the condition.

numbers = [1, 2, 3, 4, 5, 6]

result = filter(lambda x: x % 2 == 0, numbers)

print(list(result))

# prints out :-
# [2, 4, 6]