import random

# Enter numbers for the algorithm to sort
numbers = []
# Uncomment the next line to generate random numbers
for i in range(1000):
    numbers.append(random.randint(0, 10000))
print(sorted(numbers))
