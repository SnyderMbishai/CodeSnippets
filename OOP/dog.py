"""
OOP(Object-Oriented programming) demonstration using Dog
OOP concepts: 

    Inheritance -> Child attributes and methods passed down from the parent class 
    Abstraction -> hiding implementation details of the system from a user
    Polymophism -> TODO
    encapsulation -> restricting access TODO -> data hiding

    others:
    Coupling ->
    Cohesion ->
    Association ->
    Aggregation->
    Composition->

Attributes:
    Instance attributes
    Class attributes
"""

class Dog:
    # example of a class attribute
    species = "Canis familiaris"

    # instance attributes as below
    def __init__(self, age, name, breed, owner):
        self.age = age
        self.name = name
        self.breed = breed
        self.owner = owner

    # Instance method
    def __str__(self):
        return f"{self.name} is {self.age} years old and belongs to {self.species} species"

    # Instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

# Child class inheriting Dog() class above(parent class)
class BullDog(Dog):
    # polymophism
    def speak(self, sound="Arf"):
        # use super() to access the parent class
        return super().speak(sound)


if __name__=="__main__":    
    # Class object instance
    my_dog = Dog(age=4, name="spirit", breed="bulldog", owner="Mbishai")
    print(my_dog)
    print(my_dog.speak("hallo hallo"))
    # child class instance
    my_bulldog = BullDog(age=3, name="Rex", breed="bulldog", owner="Eve")
    print(my_bulldog)
    print(my_bulldog.speak())



