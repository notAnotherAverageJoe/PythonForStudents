class Puppet:
    def __init__(self, name, spooky_lvl, age, energy=10):
        self.name = name
        self.spooky_lvl = spooky_lvl
        self.age = age
        self.energy = energy
    def greet(self):
        print(f"hello, my name is {self.name}, I am {self.age}, years old...")
    def move(self):
        print(f"{self.name} shuffles across the room..creepy....")
        self.energy_usage()
    def move_right_arm(self):
        print(f"{self.name} moves their right arm")
        self.energy_usage()
    def move_left_arm(self):
        if self.energy >0:
            print(f"{self.name} moves their left arm")
        else:
            self.energy_usage()
    def energy_usage(self):
        if self.energy <= 0:
            print("Remains still and silent...must be out of energy")
        else:
            self.energy -= 1
            print(f"Energy spent moving. Remaining energy level: {self.energy}")
        
        
        


first_puppet = Puppet("Steve", 3, 241)
first_puppet.greet()
first_puppet.move()
first_puppet.move_right_arm()
first_puppet.move_left_arm()
