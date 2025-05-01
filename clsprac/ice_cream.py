import time
store_open = True
class IceCreamStore:
    def __init__(self, store_name, hours, cash_on_hand=0, inventory=0):
        self.store_name = store_name
        self.hours = hours
        self.cash_on_hand = cash_on_hand
        self.inventory = inventory

    def store_open(self):
        working_hours = int(input("How many hours will you work today? 'max 18 hours' : "))
        self.hours = working_hours
        print(f"Store will be open for {self.hours} hours today")
        
    def store_status(self):
        print("\n\t\t-----------🍨🍧🍦🍨🍧🍦------------")
        print(f"\t\tName: {self.store_name}\n\t\tHours left: {self.hours}\n\t\tCash: {self.cash_on_hand}\n\t\tInventory: {self.inventory}")
        print("\t\t-----------🍨🍧🍦🍨🍧🍦------------")
        
    def spend_funds(self):
        choice = int(input("1. Shop upgrades\n2. Back to work!"))
        if choice == 1:
            print("Upgrade shop coming soon")
            pass
        
        
    def __str__(self):
        return f"{self.store_name} (Open {self.hours}h, Cash: ${self.cash_on_hand})"
    
    # method to feed customers
    def give_customers_cream(self, noc):
        if self.inventory > 0:
            for _ in range(len(noc)):
                noc.pop(0)
                self.inventory -=1
                self.cash_on_hand +=10
        else:
            print("Not enough inventory!")
    # method to create ice cream affecting cash and inventory
    def create_the_ice_cream(self):
        self.inventory += 10
        self.cash_on_hand -= 10
        print(f"Current cash: {self.cash_on_hand}")
        print(f"Current Inventory: {self.inventory}")
        
    def worked_hours(self):
        if self.hours > 0:
            self.hours -= 1
            print("An hour has passed...")
        
    def end_of_day(self):
        print("\nEnd of day report: \n")
        print("============================")
        self.store_status()
        print("============================")
        print("\n\t\t\t....Time to rest...")
        time.sleep(3)
        self.store_open()
    
    # takes the class as an argument and changes an attribute on the 
    # class level, meaning if bankrupt is called, all stores are closed
    @classmethod
    def bankrupt(cls):
        store_open = False
        print(f"All stores are now closed due to bankruptcy.")
        
    @classmethod
    def upgrade_store(cls):
        pass
        
        #Does not rely on any instance of the class
    @staticmethod
    def create_store():
        s_name = input("Enter the store name: ")
        s_hours = int(input("How many hours will you work today? (max 18 hours): "))
        new_store = IceCreamStore(s_name, s_hours)
        return new_store


