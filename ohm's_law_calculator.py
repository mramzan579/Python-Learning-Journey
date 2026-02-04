print("Ohm's Law Calculator")
choice=int(input("What do you want to find choose one of the following by entering the number : 1. Voltage, 2. Current, 3. Resistance"))
if choice == 1:
    current_1=float(input("Enter the current in amperes"))
    resistance_1=float(input("Enter the resistance in ohms"))
    voltage_1=current_1*resistance_1
    print(f"The required voltage is: {voltage_1}")
elif choice == 2:
    voltage_2=float(input("Enter the voltage in volts"))
    resistance_2=float(input("Enter the resistance in ohms"))
    if resistance_2 == 0:
        print(f"The value of resistance should be a positive number.")
    else:
        current_2=voltage_2/resistance_2
        print(f"The required current is: {current_2}")
elif choice == 3:
    current_3=float(input("Enter the current in amperes"))
    voltage_3=float(input("Enter the voltage in volts"))
    if current_3 == 0:
        print("0 amperes current causes infinity error. Enter current value greater than zero")
    else:
        resistance_3=voltage_3/current_3
        print(f"The total resistance in circuit is: {resistance_3}")
else:
    print(f"choose the correct number")