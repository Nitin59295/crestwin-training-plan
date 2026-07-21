# unpacking(*) -- it is a process of assigning the elements of a list, tuple or other iterables to multiple variables in a single line
#              it is used to assign elements to list and tuples or other mutables in a single statement

numbers = [10,20,30]

a,b,c = numbers

print(a) #-- 10
print(b) #-- 20
print(c) #-- 30


#Example 2
a,b,c = (40,50,60)
print(a,b,c) #--a = 40, b = 50, c = 60



#Example 3

first, *rest = [1,2,3,4]
print(first) #-- prints 1
print(rest) #-- prints 2,3,4


#Example 4

*first, rest = [1,2,3,4,5,6]
print(first)
print(rest)


#Example 5

first, *middle, rest = [1,2,3,4,5,6,7,8]
print(first)
print(middle)
print(rest)




