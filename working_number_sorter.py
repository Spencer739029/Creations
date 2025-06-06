# Uncomment the next line to use random numbers for testing
# import random

# Uncomment the next line to generate a list of random numbers
# numbers = [random.randint(1, 100) for _ in range(10)]
numbers = input("Enter a list of numbers separated by spaces: ").split()

# Convert strings to integers (you can use float() if you want decimals)
numbers = [int(num) for num in numbers]

numbers.sort()

print(numbers)
