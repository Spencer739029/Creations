import pyautogui
import time

print("Starting to press the spacebar every second. Press Ctrl+C to stop.")

try:
    while True:
        pyautogui.press("space")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nStopped.")