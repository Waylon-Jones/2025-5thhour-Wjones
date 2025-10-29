#Name: Waylon
#Class: 5th Hour
#Assignment: HW12
import time
import random
from errno import ELOOP

#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.
i = 5
while i >= 1:
    print(i)
    time.sleep(.2)
    i -= 1
else:
    print("Hello World")


#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).
j = 1
while j <= 30:
    j += 1
    if j % 2 == 0:
        print(j)


#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3.
f = 0
while f <= 30:
    f+=1
    if f % 3 == 1:
        print(f)


#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.
u = random.randint(1, 6)
while u <= 6:
    if u == 1:
        continue
    print(u)
    break

#5. Create a while loop that asks for a number input until the user inputs the number 0.
x = int(input())
while x != 0:
    x = (int(input()))


