# CTI-110
# P2HW2 - List
# Jason Hunt
#10/12/2022
#Get module grades (1-6)
#Calculate the sum of grades
#Calculate the grades average
#Display lowest grade, highest grade, sum of grades and the grade average

module1 = float(input('Enter grade for Module 1: '))
module2 = float(input('Enter grade for Module 2: '))
module3 = float(input('Enter grade for Module 3: '))
module4 = float(input('Enter grade for Module 4: '))
module5 = float(input('Enter grade for Module 5: '))
module6 = float(input('Enter grade for Module 6: '))
sum_of_grades = module1 + module2 + module3 + module4 + module5 + module6
average = (module1 + module2 + module3 + module4 + module5 + module6) / 6
grade_list = [module1, module2, module3, module4, module5, module6]

print('\n------------Results------------')
print(f"{'Lowest Grade:' :<20}", f"{min(grade_list) :<20}")
print(f"{'Highest Grade:' :<20}",f"{max(grade_list) :<20}")
print(f"{'Sum of Grades:' :<20}", f"{float(sum_of_grades) :<20}")
print(f"{'Average:' :<20}", f"{f'{average:.2f}' :<20}")
print('-------------------------------')
