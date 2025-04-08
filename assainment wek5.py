# Question1
print("Activity1: Design Your Own Class!")
class Superhero:
    def __init__(self, name, power, weakness):
        self.name = name
        self.power = power
        self.__weakness = weakness  # Encapsulated attribute

    def display_info(self):
        return f"""
        Superhero Details:
        ------------------
        Name: {self.name}
        Power: {self.power}
        """

    def reveal_weakness(self):
        return f"{self.name}'s weakness is {self.__weakness}"


class FlyingSuperhero(Superhero):
    def __init__(self, name, power, weakness, flight_speed):
        super().__init__(name, power, weakness)
        self.flight_speed = flight_speed

    def display_info(self):
        return f"""
        Superhero Details:
        ------------------
        Name: {self.name}
        Power: {self.power}
        Flight Speed: {self.flight_speed} km/h
        """


# Example usage
hero1 = Superhero("Ironman", "Technology", "Ego")
hero2 = FlyingSuperhero("Superman", "Super Strength", "Kryptonite", 1000)

print(hero1.display_info())
print(hero1.reveal_weakness())
print(hero2.display_info())



#Activity 2: Polymorphism Challenge
print("Polymorphism Challenge:")                                           
class Animal:
    def move(self):
        return "The animal moves in its own way."


class Dog(Animal):
    def move(self):
        return "The dog runs on four legs."


class Bird(Animal):
    def move(self):
        return "The bird flies in the sky."


class Vehicle:
    def move(self):
        return "The vehicle moves on wheels."


class Car(Vehicle):
    def move(self):
        return "The car drives on the road."


class Plane(Vehicle):
    def move(self):
        return "The plane flies in the air."


# Example usage
entities = [Dog(), Bird(), Car(), Plane()]

for entity in entities:
    print(entity.move())