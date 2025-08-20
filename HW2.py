#Name: Waylon Jones
#Class: 5th Hour
#Assignment: HW2
from tkinter.constants import ROUND

#1. Print "Hello World!"
print("Hello World!")

#2. Create three different variables with distinct names and values: one with an integer, one with a string, one with a boolean.
CoachMack = 6
Ashton = True
Mardi = "Jones"

#3. Print all three variables on the same print function (at the same time).
print(CoachMack, Ashton, Mardi)
#4. Create a variable that asks the user to input an integer
waylon = (int(input("Insert Integer Here")))
print(waylon)
#5. Add the integer variable from #2 with the integer from #4 and print the result.
fontFairly = (waylon + CoachMack)
print(fontFairly)

#6. Take the result from #5 and divide it by 2. Print the result.
print(fontFairly / 2)
#7. Change the value of the boolean variable to the opposite value (if true then make false, or vice versa).
Ashton = False
#8. Print the value of the boolean variable.
print(Ashton)
#9. Create a variable with a number that contains decimals.
Controller = 7.2
#10. Round the number from #9 up or down using the round function.
print(round(Controller))