class Turret:
    def __init__(self, name, ammo=100, level=1):
        self.name = name
        self.ammo = ammo
        self.level = level

    @staticmethod
    def create():
        turret_name = input("Enter turret name: ")
        print(f"Turret {turret_name} has been created")
        new_turret = Turret(turret_name)
        all_turrets.append(new_turret)

all_turrets = []

def main():
    while True:
        choice = input("1. Create Turret\n2. View all turrets\n3. Quit\n")
        if choice == "1":
            Turret.create()
        elif choice == "2":
            view_turrets()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

def view_turrets():
    if not all_turrets:
        print("No active turrets\n")
        return
    for turret in all_turrets:
        print(f"Turret Name: {turret.name}, Ammo: {turret.ammo}, Level: {turret.level}")

main()
