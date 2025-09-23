#Name:Waylon Jones
#Class: 5th Hour
#Assignment: HW7

#1. Print Hello World!
print("Hello World!")
#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
myDictionary = {
        "Waylon" : [2008, 2025, 2100],
        "Mardi" : "One",
        "Merlin" : "Two",}
print(myDictionary)

#3. Print the keys of the dictionary from #2.
print(myDictionary.keys())
#4. Print the values of the dictionary from #2
print(myDictionary.values())
#5. Print one of the three numbers from the list by itself
print(myDictionary["Waylon"])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
myDictionary.update({"Ashton" : "Three"})
#7. Print the entire dictionary from #2 with the updated key and value.
print(myDictionary)
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
fifth_hour_class = {
    "Student 1" : {
        "Name" : "Mardi",
        "Age" : "18",
        "Bday" : "08-17-07",
    },
    "Student 2" : {
        "Name" : "DanDan",
        "Age" : "17",
        "Bday" : "02-14-08",
    },
    "Student 3" : {
        "Name" : "Bryson",
        "Age" : "15",
        "Bday" : "12-02-2009"
    }
}
#9. Print the names of all three classmates on the same line.
print(fifth_hour_class.keys())
#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.
fifth_hour_class.pop("Student 3")
print(fifth_hour_class)
