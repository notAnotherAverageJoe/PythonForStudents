import random as rand

all_names = ["James","Emily","Bill","Mark","Steve","Sarah","Mason","Joe","Jolly","Holly","Lily","Marge"]

class Customer:
    def __init__(self, name, mood, money=10):
        self.name = name
        self.mood = mood
        self.money = money
        
    @staticmethod
    def create_customer():
        customer_name = rand.choice(all_names)
        customer_mood = rand.choice(["happy","sad","meh"])
        # we don't need money because it is already defaulted to 10
        # we could change it if we wanted to in the future.
        new_customer = Customer(customer_name, customer_mood)
        return new_customer
    
        
        
        
        