# main class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        return f"I am {self.name}, protector of {self.city}, and I use {self.power}!"

    def save_the_day(self):
        return f"{self.name} uses {self.power} to save the day in {self.city}!"

# Subclass (Inheritance + Polymorphism Example)
class FlyingHero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

    def save_the_day(self):
        return f"{self.name} zooms through the sky at {self.flight_speed} km/h to save {self.city}!"

# Another Subclass
class TechHero(Superhero):
    def __init__(self, name, power, city, gadgets):
        super().__init__(name, power, city)
        self.gadgets = gadgets

    def save_the_day(self):
        return f"{self.name} uses high-tech gadgets like {', '.join(self.gadgets)} to protect {self.city}!"

#Example usage
hero1 = FlyingHero("SkyBolt", "Flight", "Metropolis", 500)
hero2 = TechHero("Circuit", "Intellect", "Neo City", ["Drone", "Holo-Shield"])

print(hero1.introduce())
print(hero1.save_the_day())

print(hero2.introduce())
print(hero2.save_the_day())

