import tkinter as tk

import browserestaurant as br
import yourcart as yc
import trackorder as to

def options(root):
    label = tk.Label(root, text="Welcome to the Food Delivery App!", font=("Arial", 20))
    label.pack(pady=50)

    def browse_restaurants():
        # Clear main menu UI
        for widget in root.winfo_children():
            widget.destroy()
        # Show browse restaurants page
        br.browse_restaurants(root)

    def your_cart():
        for widget in root.winfo_children():
            widget.destroy()
        yc.your_cart(root)

    def track_order():
        for widget in root.winfo_children():
            widget.destroy()
        to.track_order(root)
    
    button1 = tk.Button(root, text="Browse Restaurants", font=("Arial", 14), width=20, command=browse_restaurants)
    button1.pack(pady=10)

    button2 = tk.Button(root, text="Your Cart", font=("Arial", 14), width=20, command=your_cart)
    button2.pack(pady=10)

    button3 = tk.Button(root, text="Track Order", font=("Arial", 14), width=20, command=track_order)
    button3.pack(pady=10)
