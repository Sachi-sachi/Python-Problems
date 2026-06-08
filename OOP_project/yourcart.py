import tkinter as tk
import fooddelivery as fd

def your_cart(root):
    label = tk.Label(root, text="Your Cart", font=("Arial", 20))
    label.pack(pady=50)

    item1 = tk.Label(root, text="Item 1 - $10", font=("Arial", 14))
    item1.pack(pady=10)

    item2 = tk.Label(root, text="Item 2 - $15", font=("Arial", 14))
    item2.pack(pady=10)

    item3 = tk.Label(root, text="Item 3 - $20", font=("Arial", 14))
    item3.pack(pady=10)

    def back():
        for widget in root.winfo_children():
            widget.destroy()
        fd.options(root)

    backbutton = tk.Button(root, text="Back", font=("Arial", 14), width=20, command=back)
    backbutton.pack(pady=10)