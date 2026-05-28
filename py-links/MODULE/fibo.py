def greet():
    print("Hello from fibo!")

print("Value of __name__ inside fibo.py:", __name__)


def test_func():
   print("Testing function in fibo.py")
   greet()

def test2():
    print("Testing function 2 in main.py")

print("Yo,", test_func())

if __name__ == "__main__":
    print("This runs only when fibo.py is executed directly")
    