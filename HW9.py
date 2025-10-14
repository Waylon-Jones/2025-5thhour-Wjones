#Name:Waylon Jones
#Class: 6th Hour
#Assignment: HW9
import random

#1. Print "Hello World!"
print("Hello World!")
#2. Create a list with three variables that each randomly generate a number between 1 and 100

v1 = random.randint(1, 100)
v2 = random.randint(1, 100)
v3 = random.randint(1, 100)

randomlist = [v1, v2, v3]
#3. Print the list.
print(randomlist)
#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if randomlist[v1] >= randomlist[v2] and randomlist[v1] >= randomlist[v3]:
    print("V1 is highest number")
elif randomlist[v2] >= randomlist[v1] and randomlist[v2] >= randomlist[v3]:
    print("V2 is highest number")
elif randomlist[v3] >= randomlist[v1] and randomlist[v3] >= randomlist[v2]:
    print("V3 is highest number")

#5. Tie the result (the largest number) from #4 to a variable called "num".
num = max(randomlist)

#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.
if num % 2 == 0:
    print("it is divisible by 2")
elif num % 3 == 0:
    print("it is divisible by 3")
elif num % 2 and num % 3 == 0:
    print("it is divisible by both")
else:
    print("Neither")