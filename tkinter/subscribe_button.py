import tkinter as tk

def on_click():
  # Toggle the button text and color
  global subscribed
  if subscribed:
    button.configure(text="Subscribe", bg='red')
  else:
    button.configure(text="Subscribed!", bg='gray')
  subscribed = not subscribed

# Create the main window
root = tk.Tk()

# Create the button
button = tk.Button(root, text="Subscribe", bg='red', command=on_click)
button.pack()

# Set the initial state of the button
subscribed = False

# Run the tkinter event loop
root.mainloop()

"""
This code will create a window with a button that says "Subscribe" and is red in color. When the button is clicked, the text will change to "Subscribed!" and the button will become gray. If the button is clicked again, the text will change back to "Subscribe" and the button will become red.
"""
