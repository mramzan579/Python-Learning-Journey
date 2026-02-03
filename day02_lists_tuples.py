marks=[54,87,98,90,45]
print(marks)
marks[0]=55
print(marks)
#list slicing
student_data=["M Ramzan","Semester-II","GPA=3.7", "age=18"]
print(student_data[0:3])
print(student_data[-4:-2])
student_data[0]="Muhammad Ramzan"
print(student_data)
#list update
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
