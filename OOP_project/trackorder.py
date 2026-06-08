import tkinter as tk
import fooddelivery as fd

def track_order(root):
    label = tk.Label(root, text="Track Your Order", font=("Arial", 20))
    label.pack(pady=50)

    order_status = tk.Label(root, text="Your order is being prepared!", font=("Arial", 14))
    order_status.pack(pady=10)

    estimated_time = tk.Label(root, text="Estimated delivery time: 30 minutes", font=("Arial", 14))
    estimated_time.pack(pady=10)

    def back():
        for widget in root.winfo_children():
            widget.destroy()
        fd.options(root)

    backbutton = tk.Button(root, text="Back", font=("Arial", 14), width=20, command=back)
    backbutton.pack(pady=10)