
cords ={(0,0): "Main", (1,1):"Second", (2,2):"Third", (1,2):"Fourth", (1,0):"Fifth"}

for k,v in cords.items():
    if k == (1,1):
        print(f"Take the {cords[(1,1)]}, path!")
    elif k == (2,2):
        print(f"{cords[(2,2)]}, path is closed.")
    else:
        print(f"Wrong path")
    
    


# print("" == False)

# print(bool("") == bool(False))  