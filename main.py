class Animals :
    def sound(self):
        print("Animals make sound")

class Dog(Animals) :
    def sound(self):
        print("The dog barks")

class Cat(Animals) :
    def sound(self):
        print("A cat meows")
    
class Lion(Animals) :
    def sound(self):
        print("A lion roars")

animals = [Dog(),Cat(),Lion(),Animals()]
for a in animals:
    a.sound()