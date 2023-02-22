from  demo4_employee.employee_module import Employee

Employee.company_name = "einfochips"
Employee.company_location = "Bengaluru"

print(Employee.company_name)
print(Employee.company_location)

emp1 = Employee()
emp2 = Employee()
emp3 = Employee()

emp1.emp_id = 889
emp1.emp_name = "Marco"
emp1.emp_salary = 6000.45
emp1.emp_performance = "B"

emp2.emp_id = 890
emp2.emp_name = "Hitesh"
emp2.emp_salary = 5000.89
emp2.emp_performance = "A"

emp3.emp_id = 891
emp3.emp_name = "Polo"
emp3.emp_salary = 7800.96
emp3.emp_performance = "D"

emp3.emp_id = 892
emp3.emp_name = "Patrick"
emp3.emp_salary = 89547.65
emp3.emp_performance = "D"

print(emp2.emp_id)
print(emp2.emp_name)
print(emp2.emp_salary)
print(emp2.emp_performance)

print(emp1.emp_id)
print(emp1.emp_name)
print(emp1.emp_salary)
print(emp1.emp_performance)

print(emp3.emp_id)
print(emp3.emp_name)
print(emp3.emp_salary)
print(emp3.emp_performance)

Employee.print_author_name()
emp1.display_employee_records()

emp3.calculate_bonus()

