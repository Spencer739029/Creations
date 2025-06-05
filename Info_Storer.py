# Info Storer
# Name, Surname, Age, Address, Phone, Email and Password        
import time

while True:
    print("Welcome to Info Storer!")
    print("This program will store your personal information securely.")
    print("Please enter the following details:")
    a = input("Name: ")
    time.sleep(0.3)
    b = input("Surname: ")
    time.sleep(0.3)
    c = input("Age: ")
    time.sleep(0.3)
    d = input("Address: ")
    time.sleep(0.3)
    e = input("Phone: ")
    time.sleep(0.3)
    f = input("Email: ")
    time.sleep(0.3)
    g = input("Password: ")
    time.sleep(0.3)
    while True:
        h = input("Confirm password: ")
        time.sleep(0.3)
        i = input("What things do the passwords access: ")
        time.sleep(0.3)
        if g != h:
            print("Passwords don't match")
            print("Please try again.")
            time.sleep(0.3)
            continue
        elif g == h:
            print("Passwords match")
            break

        print("Storing your info...")
        time.sleep(3)
        print("Hello " + a + " " + b + "!")
        time.sleep(0.3)
        store = input("Would you like to store your info? (Yes/No) ").lower().strip()
        if store == "yes":
            file = open("Info Storer.txt", "a")
            file.write("Name: " + a + "\n")
            file.write("Surname: " + b + "\n")
            file.write("Age: " + c + "\n")
            file.write("Address: " + d + "\n")
            file.write("Phone: " + e + "\n")
            file.write("Email: " + f + "\n")
            file.write("Access: " + i + "\n")
            file.write("g: " + g + "\n")
            file.close()
            time.sleep(0.3)
            print("Your info has been stored!")
        else:
            print("Your info has not been stored!")
            time.sleep(1)
            print("Thank you for using Info Storer!")