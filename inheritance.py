# P arent class
class Animal:
    def speak(self):
        print("Animal is speaking")

# Child class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
class Cat(Animal):
    def meow(self):
        print("The cat is meowing")

d = Dog()
d.speak()
c = Cat
c.meow()

