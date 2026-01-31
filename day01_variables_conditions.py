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