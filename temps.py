
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

    





