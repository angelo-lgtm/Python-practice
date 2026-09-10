class Dog:
	def __init__(self, name, breed, owner):
			self.name = name
			self.breed = breed
			self.owner = owner
	
	def bark(self):
			print("Whoof whoof")
			
class Owner:
	def __init__(self, name, address, contact_number):
			self.name = name
			self._address = address
			self. phone_number = contact_number
   
	def get_address(self):
			return self._address

	def set_address(self, address):
			self._address = address
		
owner = Owner("Chris", "123 St.Peter Square", "998-9384-03")	
dog = Dog("Max", "Bulldog", owner)
print(dog.name)
dog.bark()
print(dog.breed)

#This way is not recommended in Python development instead we have to use getters and setters to do this operation.
print(owner._address) 