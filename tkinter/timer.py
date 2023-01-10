import tkinter as tk
import time
import datetime

# Get the start time
start_time = time.time()

# Create the window
window = tk.Tk()
window.title("Time Passed")

# Create a label to display the time
label = tk.Label(window, text="0", font=("Helvetica", 32))
label.pack()

# Define a function to update the time display
def update_time():
    # Calculate the elapsed time
    elapsed_time = time.time() - start_time
    # Format the elapsed time as a hexadecimal string
    elapsed_time = int(elapsed_time)
    # Update the label text
    label.config(text=str(elapsed_time) + " sec")
    # Schedule the function to be called again in 1 second
    window.after(1000, update_time)

# Call the function for the first time
update_time()

# Run the Tkinter event loop
window.mainloop()

"""
This code will create a window with a label that displays the elapsed time. The elapsed time will be updated every second.
"""
