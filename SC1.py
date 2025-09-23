#Name:
#Class: 5th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#It is up to you to decide what properties are important and the theme of the game.

Enemiesdict = {"Ashton" : {
        "Ability" : "Flying",
         "Damage" : 10,
        "Health" : 100},
        "Mardi" : {
        "Ability" : "Victim",
        "Damage" : 5,
        "Health" : 100},
        "Hogan" : {
        "Ability" : "Telekenisis",
        "Damage" : 4,
        "Health" : 100,},
        "Fred" : {
        "Ability" : "Poison",
        "Damage" : 10,
        "Health" : 100,},
        "Viking" : {
        "Ability" : "Floating",
        "Damage" : 5,
        "Health" : 100,
}}
Enemiesdict["Ashton"]["Damage"] = int(input("Ashton's Damage: "))
print(Enemiesdict["Ashton"])
Enemiesdict["Mardi"]["Damage"] = int(input("Mardi's Damage: "))
print(Enemiesdict["Mardi"])
Enemiesdict["Hogan"]["Damage"] = int(input("Hogan's Damage: "))
print(Enemiesdict["Hogan"])
Enemiesdict["Fred"]["Damage"] = int(input("Fred's Damage: "))
print(Enemiesdict["Fred"])
Enemiesdict["Viking"]["Damage"] = int(input("Viking's Damage: "))
print(Enemiesdict["Viking"])

