import random 
import time
import keyboard

minimum = float(input("Enter the minimum value: "))
maximum = float(input("Enter the maximum value: "))
if minimum >= maximum:
    print("Minimum must be less than maximum.")
    exit(1)
Lower = maximum / 2
Upper = maximum / 2
Middle = maximum / 2
lower_count = 0
upper_count = 0
middle_count = 0

print("Press 'q' to quit.")
while True:
    number = random.randint(int(minimum), int(maximum))
    print(number)
    if number < Lower:
        lower_count += 1
    elif number > Upper:
        upper_count += 1
    else:
        middle_count += 1
    
    # Breaks the code if the middle value is reached
    # Comment or delete next lines to get rid of chaos
    if number == Middle:
        minimum = -10000000000
        maximum = 10000000000
        
    time.sleep(0.5)  # Sleep for 0.5 second before generating the next number
    if keyboard.is_pressed('q'):
        print(f"Below {Lower} = {lower_count}\nAbove {Upper} = {upper_count}\nMiddle {Middle} = {middle_count}")
        break
