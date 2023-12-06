# A class is a blueprint of an object
# Objects are instances of a class

class person:
    name = "Joe"
    age = 34
    gender = "male"

    def walk(self):
        print("walking")

p = person()
p.walk()

print(p.name)