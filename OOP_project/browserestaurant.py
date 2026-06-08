import tkinter as tk
import fooddelivery as fd

def browse_restaurants(root):
    label = tk.Label(root, text="Browse Restaurants", font=("Arial", 20))
    label.pack(pady=50)

    restaurant1 = tk.Label(root, text="Restaurant 1", font=("Arial", 14))
    restaurant1.pack(pady=10)

    restaurant2 = tk.Label(root, text="Restaurant 2", font=("Arial", 14))
    restaurant2.pack(pady=10)

    restaurant3 = tk.Label(root, text="Restaurant 3", font=("Arial", 14))
    restaurant3.pack(pady=10)

    def back():
        for widget in root.winfo_children():
            widget.destroy()
        fd.options(root)

    backbutton = tk.Button(root, text="Back", font=("Arial", 14), width=20, command=back)
    backbutton.pack(pady=10)