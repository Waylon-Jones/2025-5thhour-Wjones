#Name:
#Class: 5th Hour
#Assignment: SC3
from selectors import SelectSelector

#You have been transferred to a new team working on a mobile game that allows you to dress up a
#model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.

numberOfPlayers = int(input("How many players?:  "))
ratings = []
for number in range(numberOfPlayers):
    ratings.append(int(input("Rating of player: ")))
    continue
else:
 average = sum(ratings)/numberOfPlayers
 print("The average is: ", average)
