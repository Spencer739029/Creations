import pyautogui
import time

print("Starting to click and hold every second. Press Ctrl+C to stop.")

try:
    while True:
        pyautogui.mouseDown()       # Press mouse button down
        time.sleep(0.5)             # Hold for 0.5 seconds
        pyautogui.mouseUp()         # Release mouse button
        time.sleep(0.5)             # Wait remaining time to complete 1 second loop
except KeyboardInterrupt:
    print("\nStopped.")
