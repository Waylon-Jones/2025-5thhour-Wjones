#Name:
#Class: 5th Hour
#Assignment: HW10
from operator import truediv

#1. Print Hello World!
print("Hello World!")
#2. Create three different boolean variables named wifi, login, and admin.
wifi = False
Login = False
Admin = False
#3. Create a separate integer variable that denotes the number of times
#someone with admin credentials has logged in.
adminLogin =  52

#4. Create a nested if statement that checks to see if wifi is true,
#login is true, and admin is true. If they are all true, print a
#welcome message and increase the integer variable by one. If one of them
#is false, print an error message telling them which one they are "missing".
if wifi == True:
    if Login == True:
        if Admin == True:
            print("Welcome Admin")
            adminLogin += 1
        else:
            print("You don't have permission to do that")
    else:
        print("Login Credentials Wrong")
else:
    print("You don't have an Internet Connection")



