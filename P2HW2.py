# Brandon Claypool
# 10/12/2025
# P2HW2 - List Basics (Grades)
# Program asks for six module grades, stores them in a list, and then
# displays the lowest grade, highest grade, sum of grades, and the average
# (average shown with two decimal places) in a formatted results section.
"""
Pseudocode
1) Prompt the user for six grades, one for each module. Ensure the values account
for decimals
"Enter grade for Module 1: " etc.
2) Store the input grade values in a list
module grades = [m1, m2, m3, .....]
3) Calculate the lowest grade, highest grade, sum of grades, and the grades's
average
lowest grade using min(module_grades)
highest grade using max(module_grades)
total of grades using sum(module_grades)
average using total divided by the length of the list (len(module_grades))
5) Print a blank line, then the header line: "------------Results------------".
6) Print four lines:
Lowest Grade: <lowest with 1 decimal>
Highest Grade: <highest with 1 decimal>
Sum of Grades: <total with 1 decimal>
Average: <average with 2 decimals>
(Numbers right-aligned to a common column for neatness.)
7) Print the closing line of dashes.
"""
# 1) Inputs
m1 = float(input("Enter grade for Module 1: "))
m2 = float(input("Enter grade for Module 2: "))
m3 = float(input("Enter grade for Module 3: "))
m4 = float(input("Enter grade for Module 4: "))
m5 = float(input("Enter grade for Module 5: "))
m6 = float(input("Enter grade for Module 6: "))
# 2) Store in a list
module_grades = [m1, m2, m3, m4, m5, m6]
# 3) Calculations
lowest = min(module_grades)
highest = max(module_grades)
total = sum(module_grades)
average = total / len(module_grades)
# 4) Output (formatted to match sample)
print("\n------------Results------------")
print(f"Lowest Grade: {lowest:.1f}")
print(f"Highest Grade: {highest:.1f}")
print(f"Sum of Grades: {total:.1f}")
print(f"Average: {average:.2f}")
print("----------------------------------------------")
