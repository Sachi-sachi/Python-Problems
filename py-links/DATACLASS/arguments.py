#Positional: 

def greet(name, age):
    print(name, age)

#greet("Sachi", 25)
#greet(25.56, "Sachi", 7)

#Keyword:

def greet(name, age):
    print(name, age)
#greet(name="Sachi", age=25)
#greet(age=25, "Sachi")

#Default:

def greet(name, age=18):
    print(name, age)

greet("Sachi")        # age = 18
greet("Sachi", 25)    # age = 25

#Variable-length: (*args)

def sum_all(*args):
    print(sum(args))

sum_all(10, 20, 30)

#Variable-length: (**kwargs)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Sachi", age=25, city="New York")

#Keyword-only:

def greet(name, *, age):
    print(name, age)

greet("Sachi", age=25)  # Valid
#greet("Sachi", 25)      # Invalid, age must be specified as a keyword argument
greet(name="Sachi", age=25)  # Valid