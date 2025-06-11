while True:
    input1 = input("Enter a number: ")
    number2 = input("Would you like to enter another number? (yes/no): ")
    if number2.lower() == "yes":
        input2 = input("Enter another number: ")
    else:
        input2 = 0
    descision = input("What would you like to do? (add, subtract, multiply, divide, etc): ")
    if descision == "add":
        result = int(input1) + int(input2)
    elif descision == "subtract":
        result = int(input1) - int(input2)
    elif descision == "multiply":
        result = int(input1) * int(input2)
    elif descision == "divide":
        result = int(input1) / int(input2)
    elif descision == "modulus":
        result = int(input1) % int(input2)
    elif descision == "exponent":
        result = int(input1) ** int(input2)
    elif descision == "floor division":
        result = int(input1) // int(input2)
    elif descision == "square root":
        result = int(input1) ** 0.5
    elif descision == "cube root":
        result = int(input1) ** (1/3)
    elif descision == "absolute":
        result = abs(int(input1))
    elif descision == "factorial":
        import math
        result = math.factorial(int(input1))
    elif descision == "logarithm":
        import math
        if int(input1) > 0:
            result = math.log(int(input1))
        else:
            result = "Logarithm undefined for non-positive numbers"
    else:
        result = "Invalid input"
    print(result)
    restart = input("Would you like to restart? (yes/no): ")
    if restart.lower() == "no":
        break
