# CTI-110
# P3HW2 - Salary
# Jason Hunt
# 10/30/2022
# Get (employee name, hours worked, pay rate, overtime hours)
# Cal (Regular hour pay, overtime pay, gross pay)
# Diplay (hours worked, pay rate, overtime, overtime pay, regular hour pay, gross pay)

employee_name = input("Enter employee's name: ")
hours_worked = float(input('Enter number of hours worked: '))
pay_rate = float(input("Enter employee's pay rate: "))

if hours_worked > 40:
    overtime = hours_worked - 40
    reg_hours = 40
else:
    overtime = 0
    reg_hours = hours_worked

reg_pay = (reg_hours * pay_rate)
overtime_pay = (pay_rate * 1.5) * overtime
gross_pay = reg_pay + overtime_pay

print('--------------------------------')
print('Employee name: ', employee_name)
print("")
print(f'{"Hours Worked":<15} {"Pay Rate":<10} {"Overtime":<10} {"Overtime Pay":<15} {"RegHour Pay":<15} {"Gross Pay":<15}')
print('------------------------------------------------------------------------------------------')
print(f'{hours_worked:<15} {pay_rate:<10} {overtime:<10} ${overtime_pay:<15.2f} ${reg_pay:<15.2f} ${gross_pay:<15.2f}')

