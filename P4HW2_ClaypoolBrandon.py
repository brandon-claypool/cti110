# Brandon Claypool
# 11/09/2025
# P4HW2 - Salary Calculator with Multiple Employees
# This program calculates the gross pay for multiple employees. It asks the user
# for each employee's name, hours worked, and pay rate, calculates overtime and 
# regular pay, and displays totals for all employees entered.

"""
Pseudocode:
1. Initialize total counters for overtime pay, regular pay, and gross pay
2. Ask user for employee's name (use sentinel “Done” to stop)
3. While employee name is not “Done”:
      a. Ask for hours worked (float)
      b. Ask for pay rate (float)
      c. If hours > 40:
            overtime_hours = hours - 40
            overtime_pay = overtime_hours * (pay_rate * 1.5)
            regular_pay = 40 * pay_rate
         Else:
            overtime_hours = 0
            overtime_pay = 0
            regular_pay = hours * pay_rate
      d. gross_pay = regular_pay + overtime_pay
      e. Display formatted results for that employee
      f. Add overtime_pay, regular_pay, and gross_pay to totals
      g. Increment employee counter
      h. Ask for next employee name
4. After loop ends, display:
      - total number of employees
      - total overtime paid
      - total regular pay
      - total gross pay
"""

# Initialize totals
total_employees = 0
total_overtime = 0
total_regular = 0
total_gross = 0

# Input loop
employee_name = input("Enter employee's name or 'Done' to terminate: ")

while employee_name != "Done":
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

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

    # Display results for this employee
    print()
    print(f"Employee name:   {employee_name}")
    print()
    print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'OverTime':<10}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<12}")
    print("-" * 72)
    print(f"{hours_worked:<15.1f}{pay_rate:<12.2f}{overtime_hours:<10.1f}${overtime_pay:<14.2f}${regular_pay:<14.2f}${gross_pay:<12.2f}")
    print()

    # Update totals
    total_employees += 1
    total_overtime += overtime_pay
    total_regular += regular_pay
    total_gross += gross_pay

    # Prompt for next employee
    employee_name = input("Enter employee's name or 'Done' to terminate: ")

# Display summary totals
print()
print(f"Total number of employees entered: {total_employees}")
print(f"Total amount paid for overtime: ${total_overtime:.2f}")
print(f"Total amount paid for regular hours: ${total_regular:.2f}")
print(f"Total amount paid in gross: ${total_gross:.2f}")
