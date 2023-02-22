from student_package.student_module import Student

Student.school_name = "JC"
Student.school_address = "Mysuru"

stud_1 = Student(1001, "jack", "jack@gmail.com", 45.2)
stud_2 = Student(1002, "peter", "peter@gmail.com", 85.2)
stud_3 = Student(1003, "mark", "mark@gmail.com", 56.5)

print(stud_1.student_id)
print(stud_3.print_student_name)

print(Student.get_school_details())
print(stud_1.print_student_name)

print(stud_2.get_student_name)