#WAP which accepts marks of four subjects and display total marks,percentage and grade.
#hint:more than 70%->distinction,more than 60%->first,more than 40%->pass,lesss than40%->fail
total_marks=400

total_grade=4.0
mark_of_first_student=int(input("enter the mark of first student: "))
mark_of_second_student=int(input("enter the mark of second student: "))
mark_of_third_student=int(input("enter the mark of third student: "))
mark_of_fourth_student=int(input("enter the mark of fourth student: "))
total_mark=float(mark_of_first_student+mark_of_second_student+mark_of_third_student+mark_of_fourth_student)
total_percentage=(total_mark/total_marks) * 100
if total_percentage >=70:
    print("distinction")
elif total_percentage >= 60:
    print("first division")
elif total_percentage >= 40:
    print("pass")
else:
    print("fail")