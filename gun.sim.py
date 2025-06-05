import time

count = 20
while True:
    print(f"Fa Ammo: {count}\nBANG!")
    if count > 0:
        count -= 1
        time.sleep(0.5)
    else:
        count = 20
        print("Reloading...")
        time.sleep(2)
        break

