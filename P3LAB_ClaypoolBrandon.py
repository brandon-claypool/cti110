# Brandon Claypool
# 10/19/2025
# P3LAB - Making Change (using branches)
# Program that reads a money amount and prints the most efficient number of
# Dollars, Quarters, Dimes, Nickels, and Pennies to make change. Program does not print any coins that are 0
# and use singular/plural forms correctly and prints "No change" for 0.00.

amount = float(input("Enter the amount of money as a float: $"))

# Convert integer to cents - the addition of 0.5 is to alleviate rounding issues. 
# After trying several iterations, I was getting various incorrect output, for example, $0.29 was only printing '1 Quarter, 3 Pennies'
# Adding 0.5 after multiplying by 100 was able to offset rounding errors.
cents = int(amount * 100 + 0.5)

# Use // and subtraction to convert the input from cents to dollars, quarters, dimes, nickels and pennies
dollars = cents // 100
cents = cents - dollars * 100

quarters = cents // 25
cents = cents - quarters * 25

dimes = cents // 10
cents = cents - dimes * 10

nickels = cents // 5
cents = cents - nickels * 5

pennies = cents  # remainder 0..4

total = dollars + quarters + dimes + nickels + pennies



if total == 0:
    print("No change")

# Branches for dollars through pennies. Each denomination has a branch for if its singular, and then an else if statement to handle plural
else:
    if dollars == 1:
        print("1 Dollar")
    elif dollars > 1:
        print(dollars, "Dollars")

    if quarters == 1:
        print("1 Quarter")
    elif quarters > 1:
        print(quarters, "Quarters")

    if dimes == 1:
        print("1 Dime")
    elif dimes > 1:
        print(dimes, "Dimes")

    if nickels == 1:
        print("1 Nickel")
    elif nickels > 1:
        print(nickels, "Nickels")

    if pennies == 1:
        print("1 Penny")
    elif pennies > 1:
        print(pennies, "Pennies")