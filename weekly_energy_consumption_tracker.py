print("==Weekly Energy Consumption Tracker==")
#using simple conditions and basic knowledge of lists not functions and loops
input_from_user=input("Enter units consumed each day in a week separated by space:  ")
units=[int(m) for m in input_from_user.split()]
if len(units)!=7:
    print("Error: Please enter 7 values.")
else:
    #consumption tracking
    total_units=sum(units)
    maximum=max(units)
    minimum=min(units)
    average_units=total_units/len(units)
    unit_price=11.35
    cost=unit_price*total_units
    #displaying output
    print(f"Total units consumed in a week are: {total_units}")
    print(f"Maximum units consumed on one day are: {maximum}")
    print(f"Minimum units consumed on one day are: {minimum}")
    print(f"Average units on each day :{average_units}")
    print(f"Total cost for this week power consumption is: {cost} ")