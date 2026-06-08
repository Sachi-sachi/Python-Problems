#DUCK TYPING

class Animal:
    alive=True

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self): #speak method is repeated hence polymorphism is achieved
        print("Meow")

class Car:
   # def honk(self):
    #    print("Honk") #throws error because of no speak method

    def speak(self):
        print("Honk") # works because of duck typing, it doesn't care about the type of object, it cares about the method being called

animals=[Dog(),Cat(),Car()]

for a in animals:
    a.speak()

#Aggregation vs Composition

#Aggregation: Object can exist independently
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self, engine):
        self.engine = engine  # Engine passed from outside

engine = Engine()
car = Car(engine)
car.engine.start()

#Composition: Object cannot exist without the parent

class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # Created inside

car = Car()
car.engine.start()

#Static, Class & Magic Methods

#Static Method
class Math:
    @staticmethod
    def add(a, b):
        return a + b
    
print(Math.add(5, 3))

#Class Method

class Student:
    count = 0
    yo="Hello"

    def __init__(self):
        Student.count += 1
        Student.yo="Hi" 

    @classmethod
    def get_count(cls):
        return cls.count

s1 = Student()
s2 = Student()
print(Student.get_count())  # 2
print(Student.yo) 

#Magic/Dunder Method = __init_ , _str_ , _add_ etc constructors

#Nested Class

#class inner:
#   class outer:

class Outer:
    def __init__(self):
        print("Outer class object")

    def display(self):
        print("Outer class method")

    # Nested class
    class Inner:
        def __init__(self):
            print("Inner class object")

        def display(self):
            print("Inner class method")


#Outer class
outer_obj = Outer()
outer_obj.display()

# Inner class
inner_obj = Outer.Inner()
inner_obj.display()

#PURPOSE of nested class:
#Group related classes
#COde organization
#Encapsulation