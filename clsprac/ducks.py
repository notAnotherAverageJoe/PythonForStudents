
class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm pretending to be a duck!")

def make_it_quack(living_being):
    living_being.quack()  

make_it_quack(Duck())
make_it_quack(Person())
# Quack!
# I'm pretending to be a duck!


# form of polymorphism