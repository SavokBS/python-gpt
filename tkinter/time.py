import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    clock_label.configure(text=current_time)
    clock_label.after(1000, update_time)

root = tk.Tk()
clock_label = tk.Label(root, font=("calibri", 40, "bold"),
                       background = "purple", foreground = "white")
clock_label.pack(fill=tk.BOTH, expand=1)
update_time()
root.mainloop()


"""
This code creates a new window using tkinter and a Label widget that displays the current time in the format "HH:MM:SS". The update_time function is called every second to update the time displayed in the window. The time.strftime function is used to format the current time as a string.
"""
