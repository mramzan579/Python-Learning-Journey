#== Exercise 1: Count unique electronic items ==
items = ["resistor","transistor","inductor","capacitor","transistor","capacitor","capacitor","resistor"]
unique_items = set(items)  # store unique items
dict_items = {}  # dictionary to count each item's occurrences

for item in items:
    if item in dict_items:
        dict_items[item] += 1  # increase count if already exists
    else:
        dict_items[item] = 1  # initialize count

print("=== Exercise 1 ===")
print(f"Unique items: {unique_items}")
print(f"Item counts: {dict_items}")
print()

# == Exercise 2: Celsius to Fahrenheit ==
celsius = float(input("Enter temperature in Celsius: "))
if celsius < -273.15:
    print("Invalid Temperature")
else:
    fahrenheit = (celsius * 9 / 5) + 32  # formula conversion
    print(f"Temperature in Fahrenheit: {fahrenheit}")
print()

# == Exercise 3: Filter integers ==
integers = [2,3,4,6,3,8,0,46,53,76,45,4,6,9]
filtered_list = []

for item in integers:
    if item > 10 and item % 2 == 0:  # keep only numbers >10 and even
        filtered_list.append(item)

print("=== Exercise 3 ===")
print(f"Filtered integers: {filtered_list}")
print()

# == Exercise 4: Multiples of 3 and 5 ==
multiples = []

for item in range(1, 51):
    if item % 3 == 0 and item % 5 == 0:  # divisible by both 3 and 5
        multiples.append(item)

print("=== Exercise 4 ===")
print(f"Multiples of 3 and 5 between 1-50: {multiples}")
print()

# == Exercise 5: Student grading ==
student_data = {
    "Ali": 80,
    "Ahmad": 78,
    "Raza": 65,
    "Faisal": 59,
    "Faizan": 60,
    "Rohan": 51
}

grades = {}  # store name -> grade mapping

for name, score in student_data.items():
    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    else:
        grade = "Fail"

    grades[name] = grade  # store grade in dictionary

print("=== Exercise 5 ===")
for name in grades:
    print(f"{name} : {student_data[name]} : {grades[name]}")
print()

# == Exercise 6: Simple Banking System ==
balance = 1000
user_demand = input("Balance, Withdraw or Deposit: ").lower()

if user_demand == "balance":
    print(f"Your balance is: {balance}")

elif user_demand == "withdraw":
    demand = int(input("Enter the amount you want to withdraw: "))  # convert input to integer
    if demand <= balance:
        balance -= demand  # update balance after withdrawal
        print(f"You have withdrawn {demand} and now your current balance is {balance}")
    else:
        print("You don't have enough balance.")

elif user_demand == "deposit":
    amount = int(input("Enter the amount you want to deposit: "))
    balance += amount  # update balance after deposit
    print(f"Your new balance is: {balance}")

else:
    print("System Error! Try Again")


# Exercise 6 – Separate Even and Odd Numbers

random_numbers = [3,5,6,9,0,2,65,73,567,345]

evens = []
odds = []

# loop through numbers and classify
for item in random_numbers:
    if item % 2 == 0:
        evens.append(item)
    else:
        odds.append(item)

print("Even numbers:", evens)
print("Odd numbers:", odds)



# Exercise 7 – Inventory Lookup System


inventory = {"apple": 50, "banana": 20, "orange": 30}

user_input = input("What fruit do you want to eat: ")

# check if fruit exists in inventory
if user_input in inventory:
    print(f"The quantity of {user_input}: {inventory[user_input]}")
else:
    print("Fruit out of stock")



# Exercise 8 – Vowel Counter

vwl_check = input("Write any word or sentence: ")

vowels = "aeiouAEIOU"
count = 0

# count vowels using loop
for ch in vwl_check:
    if ch in vowels:
        count += 1

print(f"Total vowels: {count}")



# Exercise 9 – Multiplication Table Generator

num = int(input("Enter number for table: "))

# generate table from 1 to 10
for i in range(1, 11):
    table = num * i
    print(table)


