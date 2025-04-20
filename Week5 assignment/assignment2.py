class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚢"

# Animal Example
class Animal:
    def move(self):
        pass

class Dog(Animal):
    def move(self):
        return "Running 🐕"

class Bird(Animal):
    def move(self):
        return "Flying 🐦"

class Fish(Animal):
    def move(self):
        return "Swimming 🐟"



vehicles = [Car(), Plane(), Boat()]
animals = [Dog(), Bird(), Fish()]

print("Vehicle Movements:")
for v in vehicles:
    print(v.move())

print("\nAnimal Movements:")
for a in animals:
    print(a.move())
