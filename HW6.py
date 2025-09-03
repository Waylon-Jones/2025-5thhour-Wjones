#Name: Waylond
#Class: 5th Hour
#Assignment: HW6


#1. Import the "random" library
import random

#2. print "Hello World!"
print("Hellow World!")
#3. Create three different variables that each randomly generate an integer between 1 and 10
d10 = random.randint(1,10)
d11 = random.randint(1,10)
d12 = random.randint(1,10)
#4. Print the three variables from #3 on the same line.
print(d10, d11, d12)
#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
d13 = d10 + 2
d14 = d11 - 4
d15 = d12 * 1.5
#6. Print each result from #5 on the same line.
print(d13, d14, d15)
#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
peopleList = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6),]
#8. Sort the list in #7 and print it.
peopleList.sort()
print(peopleList)
#9. Add together the highest three numbers in the list from #7 and print the result.
variableForNumbers = peopleList[1] + peopleList[2] + peopleList[3]
print(variableForNumbers)
#10. Create a list with 5 names of other students in this class and print the list.
nameList = ["Ashton", "Mardi", "Bryson", "Jude", "Diana"]
#11. Shuffle the list in #10 and print the list again.
random.shuffle(nameList)
print(nameList)
#12. Print a random choice from the list of names from #10.
print(random.choice(nameList))