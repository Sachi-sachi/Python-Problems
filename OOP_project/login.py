import tkinter as tk
import fooddelivery as fd


def login_page(root):
    label = tk.Label(root, text="Login to Your Account", font=("Arial", 20))
    label.pack(pady=50)

    username_label = tk.Label(root, text="Username:", font=("Arial", 14))
    username_label.pack(pady=5)
    username_entry = tk.Entry(root, font=("Arial", 14), width=30)
    username_entry.pack(pady=5)

    password_label = tk.Label(root, text="Password:", font=("Arial", 14))
    password_label.pack(pady=5)
    password_entry = tk.Entry(root, font=("Arial", 14), width=30, show="*")
    password_entry.pack(pady=5)

    #Function within function to validate login credentials
    def validate_login():
        username = username_entry.get()
        password = password_entry.get()


        if username == "user" and password == "pass":
            # Clear login UI
            for widget in root.winfo_children():
                widget.destroy()

            #success message
            success_label = tk.Label(root, text="Login Successful!", font=("Arial", 16), fg="green")
            success_label.pack(pady=10)
            #logout button
            
            def logout():
                 # clear all widgets
                for widget in root.winfo_children(): #root.winfo_children(): This function returns a list of all widgets inside the root window
                     widget.destroy()
                     # reload login page
                login_page(root)

            logout_button = tk.Button(root, text="Logout", font=("Arial", 14), width=20, command= logout)
            logout_button.pack(pady=10)
            # Show main menu
            fd.options(root)

        else:
            error_label = tk.Label(root, text="Invalid username or password. Please try again.", font=("Arial", 12), fg="red")
            error_label.pack(pady=10)

    #make the login button call the validate_login function when clicked
    #command parameter is used to specify the function to be called when the button is clicked.
    login_button = tk.Button(root, text="Login", font=("Arial", 14), width=20, command=validate_login)
    login_button.pack(pady=20)
