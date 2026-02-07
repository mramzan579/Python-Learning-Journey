items=["resistor","transistor","inductor","capacitor","transistor","capacitor","capacitor","resistor"]
unique_items=set(items)
dict_items={}
for item in items:
    if item in dict_items:
        dict_items[item]+=1
    else:
        dict_items[item]=1
print(f"Unique items: {unique_items}")
print(f"Item counts: {dict_items}")

#celsius to fahrenheite
celsius=float(input("Enter temperature in Celcius: "))
if celsius<-273.15:
    print("Invalid Temperature")
else:
    fahrenheite=(celsius*9/5)+32
    print(f"Temperature in fahranheite: {fahrenheite}")

integers=[2,3,4,6,3,8,0,46,53,76,45,4,6,9]
filtered_list=[]
for item in integers:
    if item > 10  and item % 2 ==0 :
        filtered_list.append(item)
print(filtered_list)

multiples=[]
for item in range(1,51):
    if item%3==0 and item%5==0:
        multiples.append(item)
print(multiples)

student_data={
    "Ali":80,
    "Ahmad":78,
    "Raza":65,
    "Faisal":59,
    "Faizan":60,
    "Rohan":51
}
for name,score in student_data.items():
    if score>=90:
        Grade="A+"
    elif score>=80:
        Grade="A"
    elif score>=70:
        Grade="B"
    elif score>=60:
        Grade="C"
    elif score<60:
        Grade="Fail"
    print(f"{name} : {score}")
