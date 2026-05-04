import random
import sys

def check():
    guess = input("Guess: ")
    try:
        guess = int(guess)
    except ValueError:
        print("\nEnter a number please!")
        check()
        return
    if guess <= 0 or guess >= 101:
        print("\nGuess between 1 and 100 please!\n")
        check()
    elif guess < num:
        print("\nGuess was too low!\n")
        check()
    elif guess > num:
        print("\nGuess was too high!\n")
        check()
    else:
        print("\nYou guessed it!!!\n")
        playagain()

def startgame():
    global num
    num = random.randint(1, 100)
    print("Welcome to the number guessing game!\n")
    print("Try guessing the number between 1 and 100!\n")
    
    check()

def playagain():
    print("\nPlay again? (y/n)\n")
    playagain = input()
    if playagain == 'y':
        startgame()
    elif playagain == 'n':
        sys.exit()
    else:
        print("\nPlease enter y/n:\n")
        playagain()


startgame()