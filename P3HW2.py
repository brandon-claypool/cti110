# Brandon Claypool
# 10/26/2025
# P3HW2 - Salary Calculator
# This program calculates and displays an employee's regular pay, overtime pay,
# and gross pay based on hours worked and pay rate. If the employee works more than
# 40 hours, overtime pay is calculated at 1.5 times the regular rate.

"""
Pseudocode:
1. Ask user for employee's name and store in a variable
2. Ask user for hours worked and store as float
3. Ask user for pay rate and store as float
4. If hours worked > 40:
     - Calculate overtime hours = hours worked - 40
     - Calculate overtime pay = overtime hours * (pay rate * 1.5)
     - Regular pay = 40 * pay rate
   Else:
     - Overtime hours = 0
     - Overtime pay = 0
     - Regular pay = hours worked * pay rate
5. Calculate gross pay = regular pay + overtime pay
6. Display all values in aligned columns (see assignment formatting)
"""

# Get user input
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Calculate pay
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = 40 * pay_rate
else:
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = hours_worked * pay_rate
    

gross_pay = regular_pay + overtime_pay

# Output results
print("----------------------------------------")
print(f"Employee name:  {employee_name}")
print()
print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'OverTime':<10}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<12}")
print("-" * 72)
print(f"{hours_worked:<15.1f}{pay_rate:<12.1f}{overtime_hours:<10.1f}${overtime_pay:<14.2f}${regular_pay:<14.2f}${gross_pay:<12.2f}")
