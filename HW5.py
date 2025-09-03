#Name:
#Class: 5th Hour
#Assignment: HW5
from statistics import median

#1. Create a list with 9 different numbers inside.
numList = [1, 2, 3, 4, 5, 6, 7, 8, 44]
#2. Sort the list from highest to lowest.
numList.sort(reverse=True)
#3. Create an empty list.
waylonsList = []
#4. Remove the median number from the first list and add it to the second list.
numberFive = numList[4]
numList.pop(4)
waylonsList.append(numberFive)
#5. Remove the first number from the first list and add it to the second list.
numberOne = numList[0]
numList.pop(0)
waylonsList.append(numberOne)
#6. Print both lists.
print(waylonsList)
print(numList)
#7. Add the two numbers in the second list together and print the result.
Jorge = (waylonsList[0] + waylonsList[1])
print(Jorge)
#8. Move the number back to the first list (like you did in #4 and #5 but reversed).
waylonsList.pop(1)
waylonsList.pop(0)
numList.append(numberFive)
numList.append(numberOne)
#9. Sort the first list from lowest to highest and print it.
numList.sort()
print(numList)