import random as rand
racer_id = 0

class AllRacers():
    def __init__(self, id, distance=0):
        self.id = id
        self.distance = distance
     
    @staticmethod
    def create_racers():
       return AllRacers(racer_id)
      
    def drive(self):
        movement = rand.randint(1,10)
        self.distance += movement

racers = []
random_racers = rand.randint(1,8)

for i in range(random_racers):
    racers.append(AllRacers.create_racers())
    racer_id += 1
    
for racer in racers:
    print(f"#: {racer.id}")
    

race_started = False
while(not race_started):
    choice = input("Start Race?\n").lower()
    if choice =='y':
        race_started = True
        print("Race has begun!")
        winner_found = False
        while not winner_found:
            for racer in racers:
                racer.drive()
                print(f"Racer #{racer.id} is at {racer.distance} units.")
                if racer.distance >= 100:
                    print(f"\n🏁 Winner: Racer #{racer.id} 🏁")
                    winner_found = True
                    break
        
    else:
        print("Waiting to start the race...\n")
        continue
