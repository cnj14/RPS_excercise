# game.py

import random

def Main(): 
    print("-----------------------------")
    print("Rock, Paper, Scissors, Shoot!")
    print("-----------------------------")
    name = input("What is your name? ")
    print("Welcome, " + name)
    Game()

def Game():    
    options = ["rock", "paper", "scissors"]
    choice = input("Please select either " + options[0] + ", " + options[1] + ", or " + options[2] + ": ")
    print("\n")
    if choice.lower() in options:
        print("You chose: " + choice.title())
        n = random.randint(0,2)
        opp = options[n]
        print("The computer chose: " + opp.title())
        if choice.lower() == "rock":
            if opp == "rock":
                print("The result is a draw.")
            elif opp == "paper":
                print("The computer has won this round.")
            elif opp == "scissors":
                print("You win!")
        elif choice.lower() == "paper":
            if opp == "rock":
                print("You win!")
            elif opp == "paper":
                print("The result is a draw.")
            elif opp == "scissors":
                print("The computer has won this round.")
        elif choice.lower() == "scissors":
            if opp == "rock":
                print("The computer has won this round.")
            elif opp == "paper":
                print("You win!")
            elif opp == "scissors":
                print("The result is a draw.")
        cont = input("Would you like to play again? ")
        if cont.lower() == "yes":
            print("\n")
            Game()
        else:
            print("Thanks for playing!")
            exit()
    else:
        print("Your choice does not compute. Please try again.")
        cont = input("Would you like to play again? ")
        if cont.lower() == "yes":
            print("\n")
            Game()
        else:
            print("Thanks for playing!")
            exit()


Main()
