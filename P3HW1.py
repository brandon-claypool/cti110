# Brandon Claypool
# 10/26/2025
# P3HW1 - Debugging and Completing a Program
# This program asks the user for 6 module grades, stores them in a list,
# calculates the lowest, highest, sum, and average of those grades,
# and then displays the numeric summary and the letter grade for the average.

# Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# determine lowest, highest , sum and average for grades
low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)

# determine letter grade for average
if avg >= 90:
    letter = 'A'
elif avg >= 80:
    letter = 'B'
elif avg >= 70:
    letter = 'C'
elif avg >= 60:
    letter = 'D'
else:
    letter = 'F'

# display results (match the example style)
print("\n------------Results------------")
print(f"Lowest Grade:   {low:.1f}")
print(f"Highest Grade:  {high:.1f}")
print(f"Sum of Grades:  {total:.1f}")
print(f"Average:        {avg:.2f}")
print("---------------------------------")
print(f"\nYour grade is: {letter}")