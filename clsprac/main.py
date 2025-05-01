from ice_cream import IceCreamStore as store
from customers import Customer as cust
import random as rand
import time


# just a small function to add spaces
def spaces():
    print("\n")

print("Welcome to the ice cream store simulator")
print("Time to create your store!")
# using the imported ice cream class
new_store = store.create_store()
stores_open = True
while stores_open:
    try:

        daily_operation = int(
            input(
                "1. Make ice cream🍨\n2. Take a break\n3. Serve Customers\n4. Store Stats\n5. Quit\n"
            )
        )
    except ValueError:
        print("\t\t\t\tIntegers only!")
        continue

    if daily_operation == 1:
        if new_store.hours > 0:
            print("You start creating ice cream!")
            print("This will cost you supplies and time\n that means money🍧")
            new_store.worked_hours()
            spaces()
            new_store.create_the_ice_cream()
            spaces()
        else:
            new_store.end_of_day()
       
            
    elif daily_operation == 2:
        if new_store.hours > 0:
            print("A relaxing break...")
            new_store.worked_hours()
            print(f"\t\tHours left in the day {new_store.hours}")
        else:
            new_store.end_of_day()
            
    elif daily_operation == 3:
        if new_store.hours > 0:
            new_store.worked_hours()
            all_customers = []
            number_of_customers = rand.randint(1, 10)
            for _ in range(number_of_customers):
                new_customers = cust.create_customer()
                all_customers.append(new_customers)
            for c in all_customers:
                print(f"Name: {c.name}, Mood: {c.mood}, Cash: {c.money}")
            while all_customers and new_store.inventory > 0:
                new_store.give_customers_cream(all_customers)
            print(f"\t\t\t\tNumber of Customers: {number_of_customers}🍦\n\n")
        else:
            new_store.end_of_day()

    elif daily_operation == 4:
        new_store.store_status()
        spaces()
    elif daily_operation == 5:
        stores_open = False
    else:
        break