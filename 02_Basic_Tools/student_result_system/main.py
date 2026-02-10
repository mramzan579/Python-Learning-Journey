# =========================
# Student Result System
# Muhammad Ramzan
# =========================
print(f"==Students Result System by Muhammad Ramzan==")
# Dictionary storing student names as keys and a list of marks as values
students_data={
    "Ali":[67,87,90,54],
    "Ahmad Raza":[76,9,89,79],
    "Faisal":[65,87,90,86],
    "Rohan":[65,76,57,99],
    "Faizan":[67,87,59,79]
}
#iterating through dictionary for geting marks
for name,marks in students_data.items():
    total=sum(marks)
    avg=total/len(marks)
    percentage=(total/(100*len(marks)))*100#Taking percentage of marks
    #setting conditions for final grading
    if percentage>=90:
        grade="A+"
    elif percentage>=80:
        grade="A"
    elif percentage>=70:
        grade="B"
    elif percentage>=60:
        grade="C"
    else:
        grade="Fail"
    #display of final result
    print(f"Name: {name}\nMarks : {total}\nPercentage: {percentage:.2f}\nGrade: {grade}\nAverage Marks : {avg:.2f}")
