# CHALLENGE 7: Safe File Reading with try-except

import csv


try:
   with open("factory.txt","r") as file:
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Log file is missing! Creating a backup plan...")
    with open('example.txt', 'w') as file:
        file.write("This is a backup log file.")
finally:
   print("Program executed successfully without crashing!")
print("Program executed successfully without crashing!")

import csv
with open("inventry.csv", "w", newline='') as f:
   data=csv.writer(f)
   data.writerow(['Item', 'Quantity', 'Status'])
   data.writerow(['Microchips', '500', 'In Stock'])
   data.writerow(['Sensors', '12', 'Low Stocks'])
try:
      with open("inventry.csv", "r") as f:
         csv_reader=csv.reader(f)
         for row in csv_reader:
            print(row)
except FileNotFoundError:
      print("Inventory file is missing! Please check the system.")