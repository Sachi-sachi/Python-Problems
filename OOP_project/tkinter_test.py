import tkinter as tk

# Create main window
root = tk.Tk()
root.title("My First Tkinter App")
root.geometry("300x200")

# Function for button click
def say_hello():
    label.config(text="Hello, World!")

# Create a label
label = tk.Label(root, text="Click the button", font=("Arial", 12))
label.pack(pady=20)

# Create a button
button = tk.Button(root, text="Click Me", command=say_hello)
button.pack()

# Start the GUI loop
root.mainloop()


'''''''''''''''''''''
🔍 Explanation (step-by-step)

tk.Tk() → Creates the main window
root.title() → Sets window title
root.geometry() → Sets window size
Label → Displays text
Button → Clickable button
command=say_hello → Runs function on click
pack() → Places widgets in the window
mainloop() → Keeps app running
'''''''''''''''''''''