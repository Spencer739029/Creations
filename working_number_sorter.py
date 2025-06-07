# Uncomment the next line to use random numbers for testing
# import random
import time

print("Welcome to the Number Sorter!")
print("This program will sort a list of numbers for you.")

def start():
    # Uncomment the next line to generate a list of random numbers
    # numbers = [random.randint(1, 100) for _ in range(10)]
    while True:
        try:
            numbers = input("Enter a list of numbers separated by spaces: ").split()
            numbers = [int(num) for num in numbers]
            break
        except ValueError:
            print("Invalid input. Please enter a list of numbers separated by spaces.")

    # Convert strings to integers (you can use float() if you want decimals
    numbers = [int(num) for num in numbers]

    numbers.sort()

    time.sleep(2)  # Simulate a delay for sorting
    print("Sorting complete!")
    time.sleep(2)
    print("Sorted Numbers:")
    time.sleep(0.5)
    print(numbers)
    restart = input("Would you like to sort another list of numbers? (yes/no): ")
    if restart.lower() == "yes":
        start()
    else:
        print("Thank you for using the Number Sorter!")

start()
