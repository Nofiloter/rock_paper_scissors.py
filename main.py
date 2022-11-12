
#Rock paper scissors
import random
from time import sleep

print("This is a game of rock, paper, scissors. Try to beat the computer!") #First phrase

sleep(1.5)

prompt = "y"
while prompt.upper() == "Y": #While loop for replayability
    play = input("Play (R)ock, (P)aper or (S)cissors by typing the first letter here: ") #players choice

    list = [1, 2, 3]
    x = random.choice(list) #randomizer for computer's move
    
    sleep(1)

    if play.upper() == "R" and x == 3: #Playing Rock
        print("You Win against scissors!")
    elif play.upper() == "R" and x == 2: print("You lost against paper!")
    elif play.upper() == "R" and x == 1: print("You tied with rock!")

    if play.upper() == "P" and x == 1: #Playing paper
        print("You Win against rock!")
    elif play.upper() == "P" and x == 3: print("You lost against scissors!")
    elif play.upper() == "P" and x == 2: print("You tied with paper!")

    if play.upper() == "S" and x == 2: #Playing scissors
        print("You Win against paper!")
    elif play.upper() == "S" and x == 1: print("You lost against rock!")
    elif play.upper() == "S" and x == 3: print("You tied with scissors!")

    prompt = input("Do you want to play again? Y/N: ") #Option to continue or exit loop (play again)
print("Thanks for playing!")
