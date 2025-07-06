import time
import datetime
import pygame
import os

# Initialize pygame and its mixer
pygame.init()
pygame.mixer.init()

alarm_time = input("Enter the time of the alarm (HH:MM): ")

def check_alarm():
    current_time = datetime.datetime.now().strftime("%H:%M")
    if current_time == alarm_time:
        print("Alarm ringing! Press any key to stop.")
        try:
            sound_file = "alarm_sound.mp3"
            if os.path.exists(sound_file):
                pygame.mixer.music.load(sound_file)
                # Play indefinitely (-1 means loop forever)
                pygame.mixer.music.play(-1)

                # Keep the script running and check for events while music is playing
                alarm_stopped = False
                while pygame.mixer.music.get_busy() and not alarm_stopped:
                    # Process events from the pygame event queue
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            # Handle closing the window
                            pygame.quit()
                            exit() # Exit the script
                        if event.type == pygame.KEYDOWN:
                            # Handle any key press
                            pygame.mixer.music.stop()
                            print("Alarm stopped.")
                            alarm_stopped = True
                            break # Exit the event processing loop

                    # Small delay to prevent the loop from consuming too much CPU
                    time.sleep(0.05)

            else:
                print(f"Error: Alarm sound file '{sound_file}' not found in the current directory.")
                print("Please make sure 'alarm_sound.mp3' is in the same folder as the script.")

        except pygame.error as e:
            print(f"An error occurred while trying to play the sound: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Main loop to check the time
while True:
    check_alarm()
    # Calculate time until the start of the next minute
    now = datetime.datetime.now()
    seconds_remaining = 60 - now.second
    # If it's exactly the start of a minute (seconds_remaining is 60), wait 60 seconds.
    # Otherwise, wait the remaining seconds.
    sleep_duration = seconds_remaining if seconds_remaining > 0 else 60
    time.sleep(sleep_duration)





# Note: pygame.quit() is called if the window is closed, exiting the script.
# If the alarm is stopped by key press, the script goes back to checking the time.
