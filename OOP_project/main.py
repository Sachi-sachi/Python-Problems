#program starts here
import tkinter as tk
import loadingpage as lp
import login
import fooddelivery as fd

root = tk.Tk()
root.title("Food Delivery App")
root.geometry("1200x600")

# Show loading page and keep reference
loading_widget = lp.loading(root)

# Function to switch screens
def show_main_page():
    loading_widget.destroy()  # remove loading UI
    login.login_page(root)          # show main menu
    

# Call after 2 seconds (2000 ms)
root.after(2000, show_main_page)

root.mainloop()
