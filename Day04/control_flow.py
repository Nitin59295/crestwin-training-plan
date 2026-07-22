# Control Flow :- it decides which code runs and how many times it will run.

# if/elif/else :- these are used to make decisions

score = 90

if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 65:
    grade = "C"
else:
    grade = "F"
print(grade)

# FOR LOOP:- we use FOR LOOP when we know how many times to repeat something

for i in range(5):
    print(i)
# prints out :- 0,1,2,3,4

fruits = ["Apple","Banana","Mango"]
for i in fruits:
    print(i)
# prints out:- Apple, Banana, Mango



# WHILE LOOP:- we use while loop when we want our loop to run until the condition becomes failed
count = 1
while count <= 5:
    print(count)
    count+=1
# prints out:- 1,2,3,4,5


# Break :- we use break when we want to stop the loop immediately.

for i in range(5):
    if i == 4:
        break
    print(i)
# prints out:- 0,1,2,3

# Continue :- We use Continue when we want to skip one iteration when looping

for i in range(6):
    if i == 3:
        continue
    print(i)
# prints out :- 0,1,2,4,5


# PASS:- pass is used as a placeholder. so that we can work later on the code if needed.

if True:
    pass





