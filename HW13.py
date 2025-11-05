#Name:
#Class: 5th Hour
#Assignment: HW13

#A common exercise in computer science is "FizzBuzz". The rules of
#the game are simple. Count from 1 to 100 but with every number that
#is divisible by 3 you say "Fizz" instead of the number,
#every number divisible by 5 you say "Buzz" instead,
#and if it's divisible by both you say "FizzBuzz".

#Create a while loop that follows the rules of the game.

w = 1
while w <= 100:
    if w % 3 == 0 and w % 5 == 0:
        print("FizzBuzz")
    elif w % 3 == 0:
        print("Fizz")
    elif w % 5 == 0:
        print("Buzz")
    else:
        print(w)
    w += 1




