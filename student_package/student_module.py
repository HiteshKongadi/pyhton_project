class Student:
    school_name = None
    school_address = None

    def __init__(self, student_id, student_name, studentmailid, student_percentage):
        self.student_id = student_id
        self.student_name = student_name
        self.studentmailid = studentmailid
        self.student_percentage = student_percentage

    @property
    def get_student_name(self):
        return self.student_name

    @property
    def print_student_name(self):
        return "Hi " + self.student_name + " your percentage is", self.student_percentage

    @staticmethod
    def get_school_details():
        return Student.school_name + " is located at "+ Student.school_address

    def print_grade(self):
        if 100 >= self.student_percentage >= 90:
            print("Grade is A", self.student_percentage)

        elif 89 >= self.student_percentage >= 80:
            print("Grade is B", self.student_percentage)

        elif 79 >= self.student_percentage >= 60:
            print("Grade is c", self.student_percentage)

        else:
            print("Fail")
