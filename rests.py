menu = {"taco": 2.99, "burger": 5.99, "pizza": 7.99}
# for key, value in menu.items():
#     print(f"{key}: ${value}")
# item = input("Enter your menu selection: ").lower()
# if item in menu:
#     print(f"{item.title()} costs ${menu[item]:.2f}")
# else:
#     print("sorry we 86'ed it")
# print(f"TEST -> {menu['burger']}")


currently_open = "open" # non empty strings are true
check = 0
while currently_open:
    orders = input("Menu options:\nTacos\nBurgers\nPizza\nQ to quit\n").lower()
    if orders == 'q':
        currently_open = ""
    elif orders in menu:
        print(f"{orders.title()}: {menu[orders]:.2f}")
        check += menu[orders]
        print(f"Bill: {check:.2f}")
    else:
        print("Invalid, try again")
        
  
    
        