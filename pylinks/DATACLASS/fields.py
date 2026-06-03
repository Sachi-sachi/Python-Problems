from dataclasses import dataclass, field


#how default can cause problems when using mutable types like lists or dictionaries. If you set a default value for a field to be a mutable type, that default value will be shared across all instances of the dataclass.

@dataclass
class Person:
    name: str
    #hobbies: list = [] # This is a mutable default value, which can lead to unexpected behavior
    hobbies: list = field(default_factory=list)  # This is the correct way to set a default value for a mutable type

p1 = Person(name="Alice")
p2 = Person(name="Bob")

p1.hobbies.append("reading")
print(p2.hobbies)  # This will print ['reading'] due to the mutable default value
p2.hobbies.append("sports")
print(p1.hobbies)  # This will print ['reading', 'sports'] due to the mutable default value
print(p2.hobbies)

#postinit 

@dataclass
class Person:
    name: str
    age: int
    is_adult: bool = field(init=False)

    def __post_init__(self):
        self.is_adult = self.age >= 18
p1 = Person(name="Alice", age=25)
print(p1.is_adult)  # This will print True because Alice is an adult