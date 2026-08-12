# Challenge 1: Bank Account System (Encapsulation)

class BankAccount:
    def __init__(self, account_holder, account_balance):
        self.account_holder = account_holder
        # Private attribute (Negative balance protection)
        self.__balance = account_balance if account_balance >= 0 else 0

    # Getter method to read private balance
    def get_balance(self):
        return self.__balance

    # Setter / Mutator with validation
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New Balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # Mutator with validation
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New Balance: {self.__balance}")
        else:
            print("Invalid or insufficient funds.")


# --- Testing Encapsulation ---
bank_account = BankAccount("John Doe", 1000)

# Correct way using Getter:
print(f"Initial Balance: {bank_account.get_balance()}")

bank_account.deposit(500)
bank_account.withdraw(200)

# Direct access test (Will throw AttributeError as expected):
# print(bank_account.__balance)

class User_manager:
    def __init__(self, username, password):
        self.username = username
        self.__password = None  # Private attribute
        self.set_password(password)
    def get_password(self):
        return self.__password
    def set_password(self, new_password):
        if len(new_password) >= 8:
            self.__password = new_password
            print("Password updated successfully.")
        else:
            print("Password must be at least 8 characters long.")
    def verify_password(self, password):
        if password == self.__password:
            print("Password verified!")
            return True
        else:
            print("Incorrect password.")
            return False
first=User_manager("ali", "securePass123")
print(first.get_password())  # Accessing private attribute via getter
print(first.verify_password("securePass123"))  # Verifying password

# Challenge 3: Patient Monitoring System (Encapsulation)
class patient:
    def __init__(self, name, temprature):
        self.name=name
        self.temprature=temprature
    @property
    def temprature(self):
        return self.__temprature
    @temprature.setter
    def temprature(self, value):
        if 35 <= value <= 42:
            self.__temprature = value
        else:
            raise ValueError("Temperature must be between 35 and 42 degrees Celsius.")
temp1=patient("ali", 37)
print(f"{temp1.name}'s temperature is: {temp1.temprature}°C")
print(temp1.temprature)  # Accessing private attribute via property
temp1.temprature = 38  # Using the setter method
print(f"{temp1.name}'s updated temperature is: {temp1.temprature}°C")

#challenge 4: E-Commerce Product price management (Encapsulation)
class product:
    def __init__(self, name, price, discount=0):
        self.name=name
        self.price=price
        self.discount=discount
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, value):
        if value >= 0:
            self.__price = value
        else:
            raise ValueError("Price cannot be negative.")
    @property
    def discount(self):
        return self.__discount
    @discount.setter
    def discount(self, value):
        if 0 <= value <= 100:
            self.__discount = value
        else:
            raise ValueError("Discount must be between 0 and 100.")
    @property
    def final_price(self):
        return self.__price * (1 - self.__discount / 100)
pr1=product("shampoo", 234, 10)
print(f"{pr1.name}'s final price is: ${pr1.final_price:.2f}")

#Last challenge: API Key Management (Encapsulation)
class APIKeyManager:
    def __init__(self, api_key, request_count=0, max_limits=5):
        self.__api_key = api_key  # Private attribute
        self.__request_count = request_count  # Private attribute
        self.__max_limits = max_limits  # Private attribute
    def make_request(self, provided_key):
        if provided_key != self.__api_key:
            print("Invalid API Key!")
        else:
            if self.__request_count < self.__max_limits:
                self.__request_count += 1
                print(f"Request successful! Total requests made: {self.__request_count}")
            else:
                print("API request limit reached. Please wait or upgrade your plan.")
    @property
    def remaining_requests(self):
        return self.__max_limits - self.__request_count
api=APIKeyManager("my_secret_api_key")
api1=APIKeyManager("wrong_key")
api1.make_request("wrong_key")  
api1.make_request("wrong_key")
api1.make_request("wrong_key")
api1.make_request("wrong_key")
api1.make_request("wrong_key")
api1.make_request("wrong_key")
api1.make_request("wrong_key")
api.make_request("my_secret_api_key")  # Valid request
print(f"Remaining requests: {api.remaining_requests}")
print(f"Remaining requests: {api1.remaining_requests}")