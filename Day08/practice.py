# 1. Create a generator that prints numbers from 1 to 10 using yield.

def gen():
    for i in range(1,11):
        yield (i)
g = gen()

for num in g:
    print(num)

# 2. Create a generator expression to generate squares of numbers from 1 to 20.


g = (i ** 2 for i in range(1, 21))

for num in g:
    print(num)


# 3. Combine three lists using chain().

from itertools import chain

l1 = [1,2,3,4,5]
l2 = [6,7,8,9]
l3 = [10,11,12,13]

for i in chain(l1,l2,l3):
    print(i)


# 4. Print only the first five elements of a list using islice().
from itertools import islice
l = [1,2,3,4,5,6,7]

for i in islice(l,0,5):
    print(i)

# 5. Group repeated numbers using groupby().

from itertools import groupby

numbers = [1, 2, 1, 3, 4, 4, 5, 6, 2]
numbers.sort()

for key, group in groupby(numbers):
    print(key, list(group))

# 6. Create a partial() function to always add 10 to a number.
from functools import partial

def add(a,b):
    return a+b

add_10 = partial(add, b =10)

print(add_10(5))
print(add_10(10))
print(add_10(15))

# 7. Use lru_cache() to cache the result of a factorial function.

from functools import lru_cache


@lru_cache
def factorial(n):
    print("Calculating...")

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result

print(factorial(5))
print(factorial(5))


# 8. Find the product of all numbers in a list using reduce().
from functools import reduce
l =[2,3,4]

res = reduce(lambda x,y: x*y,l)
print(res)


