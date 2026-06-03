from dataclasses import dataclass

@dataclass (init=True, repr=True, eq=True, order=True, frozen=False)
class Person:
    name: str
    age: int

'''''''''''''''''''''''''''''''''
#it is written as 

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
'''''''''''''''''''''''''''''''''

#p1 = Person("Sachi") error as age is missing
p2 = Person("Sachi", 25)
p3 = Person(age=25, name="Sachi")
p4 = Person("John", 30)
p5 = Person("John", 35)

#print(p1==p2) #error
print(p2==p3) #True
print(p2==p4) #False
print(p4==p5) #False
#print(p2.age<p4.age) #True if order=False no error as u r comparing age not the whole object
print(p2<p4)

p5.age = 40 #error as frozen=True
print(p5)
