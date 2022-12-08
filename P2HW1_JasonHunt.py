# This program calculates the display travel expenses
# 10/8/2022
# CTI-110 P2HW1 - Travel
# Jason Hunt
# Get from user(Budget, Travel_destination, fuel, food)
# Program calculates the remaining balance
# Display (Budget, Travel_destination, fuel, food, remaining balance

Budget =float(input('Enter Budget: '))
Travel_destination = input('\nEnter your travel destination: ')
Fuel = float(input('\nHow much do you think you will spend on gas? '))
Accomodation = float(input('\nApproximately, how much will you need for accomodation/hotel? '))
Food = float(input('\nLast, how much do you need for food? '))
Remaining_bal = Budget - (Fuel + Accomodation + Food)

print('\n------------Travel Expenses-------------')
print(f"{'Location:' : <20}", f"{Travel_destination : <20}")
print(f"{'Initial Budget:' :<20}", f"{'$'+str(float(Budget)) : <20}")
print(f"{'Fuel:':<20}", f"{'$'+str(float(Fuel)) :<20}")
print(f"{'Accomodation:' : <20}", f"{'$'+str(float(Accomodation)) : <20}")
print(f"{'Food:' : <20}", f"{'$'+str(float(Food)) : <20}")
print('-----------------------------------------\n')

print(f"{'Remaining Balance:' : <20}", f"{'$'+str(float(Remaining_bal)) : <20}")

