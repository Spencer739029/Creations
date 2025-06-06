import random

numbers = input("Enter a list of numbers separated by spaces: ").split()

# Convert strings to integers (you can use float() if you want decimals)
numbers = [int(num) for num in numbers]

numbers.sort()

print(numbers)
