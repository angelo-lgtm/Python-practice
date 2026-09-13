from datetime import datetime

class User:
    def __init__(self, name: str, dob: str, email: str):
        self.name = name
        self.dob = dob
        self._email = email
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, new_email: str):
        if "@" in new_email:
            self._email = new_email
            print(f"Email formatted at {datetime.now()}")
        else:
            print("Unreal email!!")
            
class Employee:
    #Static attribute 
    e_count = 0
    
    def __init__(self, user: User, department: str):
            self.user = user
            self.department = department
            #Use of static attribute within a class
            Employee.e_count+=1
            
    def description(self):
            print(f"Name of Employee: {self.user.name}\nEmail: {self.user.email}\n")

class BankAccount:
    balance = 0
    
    def __init__(self, employee: Employee):
        self.employee = employee
        Bank.total_accounts()
    
    #Private method created by prefixing the name of method by 2 underscores
    def __log_transaction(self, type: str, amount: int):
        if type == "withdraw":
            self.balance -= amount
        else:
            self.balance += amount
    
    #Procted method created by prefixing the name of method by 1 underscore        
    def _is_valid_amount(self, amount: int):
        return amount > 0
    
    def deposit(self, amount: int):
        if self._is_valid_amount(amount):
            self.__log_transaction("deposit", amount)
            print(f"The amount of {amount} has been deposited into {self.employee.user.name}'s account.")
        else:
            print("Transactino failed!")
            
    def withdraw(self, amount: int):
        if self._is_valid_amount(amount) and amount <= self.balance:
            self.__log_transaction("withdraw", amount)
            print(f"The amount of {amount} has been withdrawn from {self.employee.user.name}'s account.")
        else:
            print("Transaction failed!")

class Bank:
    accounts = 0
    
    #Creation of a static method using the below annotation
    @staticmethod
    def total_accounts():
        Bank.accounts += 1
        
    def show_accounts():
        print(f"The total number of accounts: {Bank.accounts}")
            
user = User("Angelo", "20-03-2009", "joseph34@gmai.com")

user2 = User("Divin", "16-06-2007", "divin@gmail.com")

employee = Employee(user, "IT")
employee.description()

employee2 = Employee(user2, "HR")
employee2.description()

print(f"Total number of employees: {Employee.e_count}")

account = BankAccount(employee)
account.deposit(2000000)

account2 = BankAccount(employee2)
account2.deposit(5000000)

Bank.show_accounts()