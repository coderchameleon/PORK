'''
Pork, a Zork like game about a pig
Initial code by bombercode
'''
# Importing the art lib to make the game title look a little cooler
from art import *
tprint("PORK", space=3)
tprint("Enter the Madness")
#Creating master function to run game
def runGame():
    print("You are named Hammy\n")
    print("You are a pig and you must make your way through the forest.\n")
    print("Don't become bacon!\n")

#Getting yes or no input for game start
#gameTitle function contains the game start secion so invalid inputs do not result in an exit
def gameTitle():
    gameStart = input("Do you dare enter? (y/n)")
#Actions resulting from input
    if gameStart == "y":
        print("Welcome!")
        runGame() #This launches the main part of the game defined above as runGame for the actual game to start
    elif gameStart == "n":
        print("Farewell!")
        exit()
    else:
        print("Valid inputs are y or n")
        gameTitle() #This allows invalid key inputs to loop back for another input
#Running gameTitle funciton to start the game
gameTitle()
