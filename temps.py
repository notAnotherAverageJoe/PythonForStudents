
class Logger:
    def login(self, message):
        print(f"Login: {message}")
    def logout(self, message):
        print(f"Logout: {message}")

class SystemAdmin():
    def login(self, message):
        print(f"Admin login: {message}")
        
user1 = Logger()
user1.login("Howdy")
admin1 = SystemAdmin()
admin1.login("Joe")
            
        





