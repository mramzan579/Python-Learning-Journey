# CHALLENGE 1: CRICKET ACADEMY ROSTER (COMPLETED & SOLVED)
class player:
    def __init__(self, name, role, runs=0):
        self.name=name
        self.role=role
        self.runs=runs

    def celebrate(self):
            print(f"{self.name} is celebrating thier century")

player1=player("King Babar", "Batsman", 100)
print(f"{player1.name} scored {player1.runs}")
player2=player("Shaheen Afridi", "Bowler", 5)
player3=player("Shadab Khan", "All Rounder", 50)
player2.celebrate()
player3.celebrate()

#CHALLENGE 2: BANK ACCOUNT MANAGER
class BankAccount:
     def __init__(self, account_holder, balance=0):
          self. account_holder=account_holder
          self.balance=balance
     def deposit(self, amount):
            self.balance+=amount
            print(f"Deposited: {amount}. New balance is: {self.balance}")
     def withdraw(self, amount):
           if amount>self.balance:
                print("Insufficient funds")
           else:
                self.balance-=amount
                print(f"Withdrawn: {amount}. New balance is: {self.balance}")
holder1=BankAccount("Alice", 1000)
holder2=BankAccount("Bob", 500)
holder1.deposit(500)
holder2.withdraw(600)

# CHALLENGE 3: THE SMARTPHONE AND APP TRACKER
class smartphone:
     def __init__(self, brnad, storage):
          self.brand=brnad
          self.storage=storage
          self.apps=[]
     def app(self, app_name):
          self.apps.append(app_name)
          print(f"Installed {app_name} on {self.brand} smartphone")
     def show_apps(self):
          print(f"Apps installed on {self.brand} smartphone: {self.apps}")
phone1=smartphone("Apple", 128)
phone2=smartphone("Samsung", 256)
phone1.app("Instagram")
phone1.app("WhatsApp")
phone2.app("Facebook")
phone1.show_apps()

class NumberSet:
     def __init__(self, val1, val2):
          self.val1=val1
          self.val2=val2
t=NumberSet(6,10)

# CHALLENGE 4: ANIMAL LIMBS CALCULATOR
class Animal():
    def __init__(self, arms, legs):
        self.arms=arms
        self.legs=legs
    def limbs(self):
        return self.arms+self.legs
spider=Animal(4,4)
spidlimbs=spider.limbs()

#CHALLENGE 5: PUBLIC VS PRIVATE PERSON ATTRIBUTES 
class person():
     def __init__(self, name):
          self.name=name
     def get_first_name(self):
          return self.name.split()[0]
     def get_last_name(self):
          return self.name.split()[-1]  
person1=person("John Doe")
print(person1.get_first_name())
print(person1.get_last_name())
print(person1.name)

class person():
     def __init__(self, name):
          self.__name=name
     def get_first_name(self):
          return self.__name.split()[0]
     def get_last_name(self):
          return self.__name.split()[-1]  
person1=person("John Doe")
print(person1._person__name)  # Accessing the private attribute using name mangling
print(person1.get_first_name())
print(person1.get_last_name())


