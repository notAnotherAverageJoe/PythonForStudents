



class Logger:
    def login(self, message):
        print(f"Login: {message}")
    def logout(self, message):
        print(f"Logout: {message}")
logger = Logger()
logger.login("Howdy!")
class System:
    def __init__(self, mode):
        self.mode = mode
        self.logs = Logger()
    def power_on(self):
        if self.mode == 1:
            print("Powering on")
            self.logs.login("Welcome back!")
        elif self.mode == 2:
            print("Power saving mode")
        elif self.mode == 3:
            print("Power off")
            self.logs.logout("See you tomorrow!")
        else:
            print("Invalid system operation")
computer1 = System(1)
computer1.power_on()
computer2 = System(2)
computer2.power_on()
computer3 = System(3)
computer3.power_on()

            
        




