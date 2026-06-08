from abc import ABC, abstractmethod #abstraction

#Classes and Objects concept
class User: #Parent or base class
    def __init__(self, user_id, name, phone, address, password):
        self.user_id = user_id
        self.name = name
        #encapsulation: private attributes
        self.__phone = phone
        self.__address = address
        self.__password = password

    def login(self, user_id, password):
        if self.user_id == user_id and password == self.__password:
            print(f"{self.name} logged in successfully.")
            return True
        else:
            print("Invalid credentials. Please try again.")
            return False

    def logout(self):
        print(f"{self.name} logged out successfully.")

    def update_profile(self, phone=None, address=None):
        if phone:
            self.__phone = phone
        if address:
            self.__address = address
        print(f"{self.name}'s profile updated successfully.")

    #getter methods for private attributes
    def get_phone(self):
        return self.__phone

    def get_address(self):
        return self.__address

#inheritance where customer is childclass and inherits from User who is parent class
class Customer(User): #Child or derived class
    def __init__(self, cart, order_history):
        self.cart = cart
        self.order_history = order_history

    def browse_restaurants():
        print("Browsing restaurants...")

    def add_to_cart(item):
        print(f"Added {item} to cart.")

    def remove_from_cart(item):
        print(f"Removed {item} from cart.")

    def place_order():
        print("Order placed successfully.")

    def track_order(order_id):
        print(f"Tracking order {order_id}...")

    def make_payment():
        print("Processing payment...")

class DeliveryAgent(User): #Child or derived class
    def __init__(self, current_location, availability_status):
        self.current_location = current_location
        self.availability_status = availability_status

    def accept_order(order):      
        print(f"Delivery agent accepted order {order}.")

    def pick_order(order):
        print(f"Delivery agent picked up order {order}.")

    def deliver_order(order):
        print(f"Delivery agent delivered order {order}.")

    def update_status():
        print("Updating delivery agent status...")

class Admin(User): #Child or derived class

    def add_restaurant():
        print("Adding restaurant...")
        
    def remove_restaurant():
        print("Removing restaurant...")

    def view_all_orders():
        print("Viewing all orders...")

    def manage_users():
        print("Managing users...")


class Payment(ABC): #Abstract class for payment
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount): #polymorphism as same method name in abstract class and child classes
        print(f"Processing credit card payment of amount: {amount}")

class UPIPayment(Payment):
    def process_payment(self, amount): #polymorphism as same method name in abstract class and child classes
        print(f"Processing UPI payment of amount: {amount}")

class CashOnDelivery(Payment):
    def process_payment(self, amount): #polymorphism as same method name in abstract class and child classes
        print(f"Please pay {amount} rupees to delivery agent upon receiving your order.")

def main():
    print("---- User Registration ----")
    
    user_id = int(input("Enter User ID: "))
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    address = input("Enter Address: ")
    password = input("Create Password: ")

    user = User(user_id, name, phone, address, password)

    print("\n---- Login ----")
    login_id = int(input("Enter User ID: "))
    login_pass = input("Enter Password: ")

    if user.login(login_id, login_pass):
        print("\n---- Update Profile ----")
        new_phone = input("Enter new phone (or press Enter to skip): ")
        new_address = input("Enter new address (or press Enter to skip): ")

        user.update_profile(
            phone=new_phone if new_phone else None,
            address=new_address if new_address else None
        )

        print("\n---- Payment ----")
        print("1. Credit Card\n2. UPI\n3. Cash On Delivery")
        choice = int(input("Choose payment method: "))
        amount = float(input("Enter amount: "))
        
        match choice:
            case 1:
                payment = CreditCardPayment()
            case 2:
                payment = UPIPayment()
            case 3:
                payment = CashOnDelivery()

        payment.process_payment(amount)

        user.logout()


if __name__ == "__main__":
    main()
