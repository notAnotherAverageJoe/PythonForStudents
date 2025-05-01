class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm pretending to be a duck!")

def make_it_quack(thing):
    thing.quack()  # It doesn't matter *what* thing is, as long as it has a quack() method

make_it_quack(Duck())     # ✅ Quack!
make_it_quack(Person())   # ✅ I'm pretending to be a duck!
