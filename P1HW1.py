# Brandon Claypool
# 09/24/25
# P1HW1
# Python program that collects integers from the user
# to complete calculations such addition, subtraction, and exponents
# then displays the results.

# Calculating Exponenets
print("-----Calculating Exponenets----\n")

# Get base and exponent from the user
base = int(input("Enter an integer as the base value: "))
exp = int(input("Enter an integer as the exponent: "))

# Compute the exponent
exp_result = base ** exp

print(f"\n{base} raised to the power of {exp} is {exp_result} !!\n")

# Addition and Subtraction
print("-----Addition and Subtraction----\n")

start = int(input("Enter a starting integer: "))
add = int(input("Enter an integer to add: "))
subtract = int(input("Enter an integer to subtract: "))

total = start + add - subtract

print(f"\n{start} + {add} - {subtract} is equal to {total}")