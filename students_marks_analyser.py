print("Student Marks Analyser")

#Enter marks manually for each subject
s_1=int(input("Enter marks of your first subject"))
s_2=int(input("Enter marks of your second subject"))
s_3=int(input("Enter marks of your third subject"))
s_4=int(input("Enter marks of your fourth subject"))
s_5=int(input("Enter marks of your fifth subject"))

#validate marks in range [0-100]
if any (m < 0 or m > 100 for m in [s_1,s_2,s_3,s_4,s_5]):
    print("Error: Marks must be between 0 and 100")
else:
    #store marks in a list
    all_subjects_marks=[s_1,s_2,s_3,s_4,s_5]
    subject_nums=len(all_subjects_marks)
    total=sum(all_subjects_marks)
    percentage=(total/(subject_nums*100))*100
    # Determine grade
    if percentage>=90:
        Grade="A"
    elif percentage>=80:
        Grade="B"
    elif percentage>=70:
        Grade="C"
    elif percentage>=60:
        Grade="D"
    else:
        Grade="Fail"
    # Display result
    print("==Result==")
    print(f"Total marks: {total}/500")
    print(f"Percentage : {percentage}")
    print(f"Grade: {Grade}")