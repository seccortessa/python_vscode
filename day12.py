""" 

In this game the system ask the user for guess a number. 
firs, the console shoudl print "Welcome to the number Guessing game!
I'm thingking of a number between 1 and 100
Choose a difficulty. Type 'easy' or 'hard':"

If the user type is 'easy', it will have 10 attempts to guess. anh 5 attempts for 'hard'

If the number typed is less than the number to guess, print "too less" and "to hignh" if it is greater.




"""
import random

def playGame(number,diff):
    win = False
    if diff == "easy":
        attempts =10
    else:
        attempts = 5
    while attempts >= 0:
        print("You have",attempts, " attempts remaining to guess the number.")
        numberG = int(input("Guess a number: "))
        if numberG == number:
            win = True
            break
        elif numberG > number:
            print("Too high")
            attempts = attempts - 1
        else:
            print("Too low")
            attempts = attempts - 1
    return win        

playOn = True

while playOn:
    print("Welcome to the number Guessing game!")

    number = random.randint(1,100)

    print("I'm thingking of a number between 1 and 100")

    diff = input("Choose a difficulty. Type 'easy' or 'hard':")

    win = playGame(number,diff)

    if win:
        print("Congratulations, you won! The number was ",number)
    else:
        print("You lose!, the number was ",number)
        
    playagain = input("Do you want to play again? 'y', 'n' ")

    if playagain == "y":
        playOn = True
    else:
        playOn = False
    