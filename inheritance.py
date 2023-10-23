
# Parent class
class Animal:
    def speak(self):
        print("Animal is Speaking")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

class Cat(Animal):
    def meow(self):
        print("Cat is meowing")

d = Dog()
d.speak()