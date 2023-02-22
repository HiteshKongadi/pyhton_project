def salary_calculation(bonus):
    updated_salary = emp_salary + (emp_salary * (bonus / 100))
    return updated_salary

print(salary_calculation(10))