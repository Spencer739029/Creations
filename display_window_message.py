import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("My Message Window")
window.geometry("300x150")  # Set window size (width x height)

# Add a custom message label
message = tk.Label(window, text="I love Summer \n so much!!! :)", font=("Arial", 20))
message.pack(pady=30)  # Add some padding around the label

# Start the GUI event loop
window.mainloop()

# Delete previous window to display new message
