import pyfiglet

text_art = pyfiglet.figlet_format("Magico Apps\nCorporate Talent & Payroll Management System")
print(text_art)


def calculate_bonus(base_salary, performance_rating):
    if performance_rating == 5:
        bonus = base_salary * (20/100)
    elif performance_rating == 3 or performance_rating == 4:
        bonus = base_salary * (10/100)
    elif performance_rating < 3 and performance_rating > 0:
        bonus = 0
    return bonus



def calculate_tax(gross_salary):
    if gross_salary > 7000:
        tax_deduction = gross_salary * (15/100)
    elif gross_salary >= 3000 and gross_salary <= 7000:
        tax_deduction = gross_salary * (10/100)
    elif gross_salary < 3000 and gross_salary >= 0:
        tax_deduction = 0
    return tax_deduction



def print_output(bonus,employee_name,department,base_salary,gross_salary,tax_amount,net_salary):
    print(f"""
\n\n
==============================================================================================
Employee Name: {employee_name}
Department: {department}
Base Salary: {base_salary:.2f} EGP
Bonus: {bonus:.2f} EGP
Tax Deduction: {tax_amount:.2f} EGP
Net Salary: {net_salary:.2f} EGP
==============================================================================================
""")



def main_hr_app():

    print("\n==============================================================================================")
    employee_name = input("Enter your name: ")
    department = input("Enter your Department: ")
    base_salary = float(input("Enter the Base Salary: "))
    performance_rating = int(input("Enter the Performance Rating between (1-5): "))
    print("==============================================================================================\n")
    
    if base_salary >= 0:
        valid_base_salary = base_salary
    else:
        print("The Base Salary shouldn't be negative!")
        return 1

    if performance_rating >= 1 and performance_rating <= 5:
        valid_performance_rating = int(performance_rating)
    else:
        print("Performance Rating should be in range (1-5).\n")
        return 1

    bonus = calculate_bonus(valid_base_salary, valid_performance_rating)
    gross_salary = valid_base_salary + bonus
    gross_salary = float(gross_salary)
    tax_deduction = calculate_tax(gross_salary)
    net_salary = gross_salary - tax_deduction

    print_output(bonus,employee_name,department,valid_base_salary,gross_salary,tax_deduction,net_salary)







main_hr_app()