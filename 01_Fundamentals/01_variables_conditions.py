measured_voltage=12.4
measured_current=0.8
power_watts=measured_current*measured_voltage
if power_watts>10.0:
    print("Warning: Heat Dissipation High")
else:
    print("Efficiency Nominal")
 
hours=9
minutes=34
seconds_in_this_hour=minutes*60
remaining_seconds=3600-seconds_in_this_hour
print(f"Remaining time: {remaining_seconds}s")
#applying conditions for current situation
current_amps=2.5
max_limit=2.0
if (current_amps>max_limit):
    print("BREAKER TRIPPED!")
else:
    print("Load Safe")
switch_pos="down"
if (switch_pos=="up"):
    print("Light is ON")
else:
    print("Light is OF")   
temp_samples=[25.2,25.4,25.9,26.3,27.7,23.3] 
temp_average=sum(temp_samples)/len(temp_samples)
print(f"The average temprature is : {temp_average}C")
top_row=["Q","W","E","R","T"]
top_row[3]="FAULTY"
print(top_row)
#Ohm's Law calculator
voltage = float(input("Input the value of volatge   "))
resistance = int(input("Input the value of Resistance   "))
if resistance > 0:
    current = voltage / resistance
    print(f"The current is: {current}")
elif resistance == 0 :
    print("The infinity error. The value of resistance should not be zero.")
else:
    print("The value of resistance should not be negative.")
variable_a=True
variable_b=False
if variable_a & variable_b == True :
    print("Signal High")
else:
    print("Signal Low")

values=[10,20,30]
values.append(40)
print(values)
#described home LED state
led_state="pulse"
if led_state=="pulsing":
    print("PWM Active")
elif led_state=="on":
    print("Active")
else:
    print("State unknown")

pins=["GPI01","GPI02","GPI03","ADC0"]
pins[3]="ADC10"
print(pins)

input_v=210
if input_v>100&input_v<220:
    print("Adapter Safe")
else:
    print("Input Surge: Fuse Blown")
#Battery Health Monitor
battery_voltage=12
if battery_voltage>=12.6:
    print("The battery is Full.")
elif battery_voltage>12.0 & battery_voltage<12.5:
    print("The health situation Good.")