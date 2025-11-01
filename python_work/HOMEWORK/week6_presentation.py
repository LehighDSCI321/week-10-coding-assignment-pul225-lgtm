# superclass with common attributes
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def breathe(self):
        print(f"{self.name} is breathing.")

# inheriting from Animal
class Dog(Animal):
    # Inherits __init__ and breathe() automatically
    def bark(self):  # New method unique to Dog
        print(f"{self.name} says woof!")

# overriding a method
class Cat(Animal):
    def breathe(self):  # Override breathe() for Cat
        print(f"{self.name} purrs while breathing.")

animal = Animal('elephant', 3)
animal.breathe()

dog = Dog('dd', 4)
dog.bark()
dog.breathe()

cat = Cat('cc', 5)
cat.breathe()
