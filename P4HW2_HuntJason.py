# CTI-110
# P4HW2-Salary Calculator
# Jason Hunt
# 11/15/2022
# Get users employee names, hours worked, and pay rate 
# Calculate overtime, overtime pay, regular pay, gross pay, how many employee names entered, total overtime payed, total regular hours payed, and total gross payed
# Display hours worked, pay rate overtime, overtime pay, regular hour pay, and gross pay
# When user enters "None"
# Display
employee_list=[]
total_overtime = 0
total_reg_hours = 0
total_gross_pay = 0


while(True):
    print("Enter employee's name or \"None\" to terminate:", end=' ')
    employee_name = input()
    
    if employee_name != 'None':
        hours_worked = float(input("How many hours did " + employee_name + " work? "))
        pay_rate = float(input("What is " + employee_name + "'s pay rate? "))
        employee_list.append(employee_name)

        if hours_worked > 40:
            overtime = hours_worked - 40
        else:
            overtime = 0

        overtime_pay = (1.5 * pay_rate)  * overtime
        reg_hour = hours_worked - overtime
        reg_hour_pay = reg_hour * pay_rate
        gross_pay = overtime_pay + reg_hour_pay

        total_overtime += overtime_pay
        total_reg_hours += reg_hour_pay
        total_gross_pay += gross_pay
        
        print("\n")
        print('Employee name: ', employee_name)
        print("\n")
        print(f'{"Hours Worked": <15} {"Pay Rate": <10} {"Overtime": <10} {"Overtime Pay": <15} {"RegHour Pay": <15} {"Gross Pay": <15}')
        print("------------------------------------------------------------------------------------------")
        print(f'{hours_worked: <15} {pay_rate: <10} {overtime: <10} ${overtime_pay: <15.2f} ${reg_hour_pay: <15.2f} ${gross_pay: <15.2f}')
        print("\n")
              
    
    else:
        break

print("\n")    
print("Total number of employees entered: ", len(employee_list))
print("Total amount payed for overtime: " + f'${total_overtime:<.2f}')
print("Total amount payed for regular hours: " + f'${total_reg_hours:.2f}')
print("Total amount payed in gross: " + f'${total_gross_pay:.2f}')
        
