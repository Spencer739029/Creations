import random
import time

print("Welcome to the AI Number Guessing Game!") 
print("The AI gets 5 attempts to guess your number between 1 and 100.")

difficulty = int(input("How many attempts does the AI have: "))
attempts = int(difficulty)

correct_number = int(input("Enter the number for the AI to guess: "))

time.sleep(2)  # Simulate thinking time

# Initial guess
guess = 50
print(f"Is the number {guess}?")

while attempts > 0:
    time.sleep(2)

    if guess == correct_number:
        print("AI guessed your number correctly!")
        break
    elif guess < correct_number:
        print("AI's guess is lower than your number.")
        guess += random.randint(1, 10)
    elif guess > correct_number:
        print("AI's guess is higher than your number.")
        guess -= random.randint(1, 10)

    # Keep the guess within bounds
    guess = max(1, min(100, guess))

    attempts -= 1
    print(f"Attempts left: {attempts}")
    time.sleep(2)
    print(f"AI guesses: {guess}")

if guess != correct_number:
    print("AI failed to guess your number.")
