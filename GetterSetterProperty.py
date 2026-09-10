import datetime

class User:
    def __init__(self, name, dob, email):
        self.name = name
        self.dob = dob
        self._email = email
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self._email = new_email
        else:
            print("Unreal email!!")
            
user = User("Angelo", "20-03-2009", "nshutijoseph34@gmai.com")
user.email = "nshuti"
print(user.email)