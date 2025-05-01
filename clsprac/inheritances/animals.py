# Animal class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "Some generic animal sound"

    def info(self):
        return f"{self.name} is a {self.species}."


# Bird class that inherits from Animal
class Bird(Animal):
    def __init__(self, name, species, can_fly=True):
        super().__init__(name, species)
        self.can_fly = can_fly

    def make_sound(self):
        return "Chirp chirp!"

    def fly(self):
        if self.can_fly:
            return f"{self.name} is flying!"
        else:
            return f"{self.name} can't fly."

# Example usage
parrot = Bird("Polly", "Parrot")
penguin = Bird("Pingu", "Penguin", can_fly=False)

print(parrot.info())      # Polly is a Parrot.
print(parrot.make_sound())# Chirp chirp!
print(parrot.fly())       # Polly is flying!

print(penguin.info())     # Pingu is a Penguin.
print(penguin.make_sound())# Chirp chirp!
print(penguin.fly())      # Pingu can't fly.
