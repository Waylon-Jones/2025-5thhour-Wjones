#Name: Waylon
#Class: 5th Hour
#Assignment: HW4


#1. Print Hello World!
print("Hello World!")

#1. Create a list with 5 strings containing 5 different names in it.
mardisList = ["Mardi", "Waylon", "Ashton", "Diana", "Tucker" ]
#2. Append a new name onto the Name List.
mardisList.append("Timothy")
#3. Print out the 4th name on the list.
print(mardisList[3])
#4. Create a list with 4 different integers in it.
waylonsList = [1, 5, 8, 23,]
#5. Insert a new integer into the 2nd spot and print the new list.
waylonsList.insert(2, 22)
print(waylonsList)
#6. Sort the list from lowest to highest and print the sorted list.
waylonsList.sort()
print(waylonsList)
#7. Add the 1st three numbers on the sorted list together and print the sum.
print(waylonsList[0] + waylonsList[1] + waylonsList[2])
#8. Create a list with two strings, two variables, and too boolean values.
horsePowerList = ["Ferrari", "Dodge", 14, 15, True, True]
print(horsePowerList)

#9. Create a print statement that asks the user to input their own index value for the list on #8.
print(horsePowerList.append(input("Insert Whatever You Want Here: ")))
