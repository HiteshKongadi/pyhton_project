class Employee:
    company_name = None  # Static variable or class variable
    company_location = None  # Static variable or class variable

    # constructor - pre-requisite
    def __init__(self):
        self.emp_id = None  # non static variables
        self.emp_name = None  # non static variables
        self.emp_salary = None  # non static variables
        self.emp_performance = None  # non static variables

    @staticmethod  # static method
    def print_author_name():
        print("Author name : Hitesh Kongadi")

    def display_employee_records(self):  # non static method
        print(50 * "-")
        print("Empoyee ID:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Employee Salary:", self.emp_salary)
        print("Employee Performance:", self.emp_performance)
        print("Company Name :", Employee.company_name)
        print("Company Location :", Employee.company_location)
        print(50 * "-")

    def salary_calculation(self, bonus):
        updated_salary = self.emp_salary + (self.emp_salary * (bonus / 100))
        return updated_salary

    def calculate_bonus(self):
        if self.emp_performance == "A":
            print(self.salary_calculation(10))
            print(self.emp_name)
            print("10 % bonus")

        elif self.emp_performance == "B":
            print(self.salary_calculation(5))
            print(self.emp_name)
            print("5 % bonus")

        elif self.emp_performance == "C":
            print(self.salary_calculation(2))
            print(self.emp_name)
            print("2 % bonus")

        else:
            print(self.emp_name)
            print("No Bonus")
