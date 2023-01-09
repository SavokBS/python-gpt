import tkinter as tk
import random, string

# Create the window
window = tk.Tk()
window.title("Random Values")

# Create a label to display the random integer
int_label = tk.Label(window, text="0", font=("Helvetica", 32))
int_label.pack()

# Create a label to display the random hexadecimal string
hex_label = tk.Label(window, text="0", font=("Helvetica", 32))
hex_label.pack()

# Create a label to display the random string
string_label = tk.Label(window, text="0", font=("Helvetica", 32))
string_label.pack()

# Define a function to update the random values
def update_values():
    # Generate a random integer
    random_int = random.randint(0, 100)
    # Generate a random hexadecimal string
    random_hex = hex(random.randint(0, 100))
    # Generate a random string
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    # Update the integer label text
    int_label.config(text=str(random_int))
    # Update the hexadecimal label text
    hex_label.config(text=random_hex)
    # Update the string label text
    string_label.config(text=random_string)
    # Schedule the function to be called again in 1 millisecond
    window.after(1, update_values)

# Call the function for the first time
update_values()

# Run the Tkinter event loop
window.mainloop()


"""
This code will create a window with three labels: one that displays a random integer, another that displays a random hexadecimal string, and another that displays a random string. The values will be updated every millisecond.
"""
