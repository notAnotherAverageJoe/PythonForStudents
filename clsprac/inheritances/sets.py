class Animal:
    def __init__(self, name, species):
        self._name = name
        self._species = species

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def species(self):
        return self._species

    @species.setter
    def species(self, value):
        if not value:
            raise ValueError("Species cannot be empty")
        self._species = value

    def make_sound(self):
        return "Some generic animal sound"

    def info(self):
        return f"{self.name} is a {self.species}."


class Bird(Animal):
    def __init__(self, name, species, can_fly=True):
        super().__init__(name, species)
        self._can_fly = can_fly

    @property
    def can_fly(self):
        return self._can_fly

    @can_fly.setter
    def can_fly(self, value):
        if not isinstance(value, bool):
            raise ValueError("can_fly must be a boolean")
        self._can_fly = value

    def make_sound(self):
        return "Chirp chirp!"

    def fly(self):
        return f"{self.name} is flying!" if self.can_fly else f"{self.name} can't fly."


parrot = Bird("Polly", "Parrot")
print(parrot.info())       # Polly is a Parrot.
print(parrot.make_sound()) # Chirp chirp!
print(parrot.fly())        # Polly is flying!

penguin = Bird("Pingu", "Penguin", can_fly=False)
print(penguin.fly())       # Pingu can't fly.

penguin.name = "Pengy"
print(penguin.name)        # Pengy
