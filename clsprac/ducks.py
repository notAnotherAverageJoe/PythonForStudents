
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

class Logger:
    def login(self, message):
        print(f"User Login: {message}")
    def logout(self, message):
        print(f"Logout: {message}")

class SystemAdmin():
    def login(self, message):
        print(f"Admin login: {message}")
        
def all_login(emps):
    emps.login("Sytem access.")
all_login(Logger())
all_login(SystemAdmin())

    
