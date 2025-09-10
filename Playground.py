import random
from operator import truediv

balance = 1000
balance = int(balance)
winnings = 0
winnings = int(winnings)

def betcheck(betamount):
    if betamount.isdigit() == True:
        betamount = int(betamount)
        rightbet = True
    else:
        rightbet = False
print("please enter a whole number for your bet")
def betlimit(betamount):
    if betamount > balance == False:
        goodlimit = False
        print("That bet is too high!")
    else:
        goodlimit = True
        return goodlimit
def askinputcheck(answerinput):
    if answerinput == "Yes" or answerinput == "yes" or answerinput == "y" or answerinput == "No" or answerinput == "no" or answerinput == "n":
        rightanswerinput = True
    else:
        rightanswerinput = False
        print
        "This is an incorrect input, please type an appropriate answer in."
    return rightanswerinput

Validbet = False
while Validbet == False:
    betamount = raw_input("Please enter amount you wish to bet: ")
    Validbet = betcheck(betamount)


#Spinmachine =(int(input("gambling amount")))




winningOptions = ["Gold" , "Silver" , "Bronze", "7s"]
print(random.choice(winningOptions))
random.shuffle(winningOptions)
print(random.choice(winningOptions))
random.shuffle(winningOptions)
print(random.choice(winningOptions))

