marks=[54,87,98,90,45]
print(marks)
marks[0]=55
print(marks)
#list slicing
student_data=["M Ramzan","Semester-II","GGPA=3.7", "age=18"]
print(student_data[0:3])
print(student_data[-4:-2])
student_data[0]="Muhammad Ramzan"
print(student_data)
#list methods
electric_components=["Resistance=5ohms","current=0.5amp","voltage=2.5volts"]
electric_components[1]="current=0.54amp"
print(electric_components)
electric_components.append("capacitance=5micro farad")
print(electric_components)
electric_components.pop()
print(electric_components)
electric_components.remove("Resistance=5ohms")
print(electric_components)
electric_components.append("Power=1.35watts")
print(electric_components)

#The signal buffer(append&pop)
buffer = [22.1, 23.5, 21.8]
buffer.append(25.0)
#applying condition if len of list increases from 3 then to pop the last number index 0
if len(buffer)>3:
    buffer.pop(0) #removes the first reading
    print(buffer)

#The Logic Level Gate (In-Place Update)
pins = [True, True, False, True]    
pins[2]=True
print(f"Pin 3 is corrected in list :{pins}")
#Data selection / slicing / filtering pipeline
data_received=[20,30,40,50,60]
data_after_filteration=[data_received[1],data_received[2],data_received[3]]
print(data_after_filteration)

packet = ["HEADER", 0xAF, 0x12, 0x55, "CRC_OK"]
payload= packet [1:-1]
print(payload)
#The Component Inventory (Delete & Remove)
components_inventory=["Resistor","Inductor","Capacitor","Transistor","LED","ICs"]
components_inventory.remove("Inductor")
components_inventory.pop()
print(components_inventory)

#The Diagnostic Report (List Methods & Conditions)
report_list=["E01","E04" , "E404"]
if "E04" in report_list:
    print("Critical: Voltage Sag detected (E04)")
    print(len(report_list))
#Tabs Currently opened in my browser
tabs=["LinkedIn","Youtube","Hostinger","Wikipedia"]
work_tabs=tabs[0:3]
tabs[2]="GitHub"
print(f"All tabs opened in browser are :{tabs} and working tabs are : {work_tabs}")

#taking input from user and saving in a list
fav_movie_1=input("Enter names of your first fav movie  ")
fav_movie_2=input("Enter names of your second fav movie  ")
fav_movie_3=input("Enter names of your third fav movie  ")
movies=[fav_movie_1,fav_movie_2,fav_movie_3]
print(movies)

