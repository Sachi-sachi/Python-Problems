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

    def add_to_cart(item):
    def remove_from_cart(item):
    def place_order():
    def track_order(order_id):
    def make_payment():

class DeliveryAgent(User): #Child or derived class
    def __init__(self, current_location, availability_status):
        self.current_location = current_location
        self.availability_status = availability_status

    def accept_order(order):
        
    def pick_order(order):
    def deliver_order(order):
    def update_status():

class Admin(User): #Child or derived class

    def add_restaurant():
        
    def remove_restaurant():
    def view_all_orders():
    def manage_users():


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