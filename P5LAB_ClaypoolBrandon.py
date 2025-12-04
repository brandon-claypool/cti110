# Brandon Claypool
# 12/3/2025
# P5LAB
# Using user-defined functions

import random

def disperse_change(change):

    # Converting the value to an integer
    change = round(change* 100)
    print(f"Change owed as integer: ${change}")

    # Determine how many dollars are needed
    num_dollars = change // 100
    change = change - (num_dollars * 100)

    # Determine how many quarters are needed
    num_quarters = change // 25
    change = change - (num_quarters * 25)

    # Determine how many dimes are needed
    num_dimes = change // 10
    change = change - (num_dimes * 10)

    # Determine how many nickels are needed
    num_nickels = change // 5
    change = change - (num_nickels * 5)

    # Determine how many pennies are needed
    num_pennies = change


    # Display coins needed
    if num_dollars > 0:
        if num_dollars == 1:
            print(f"{num_dollars} dollar")
        else:
            print(f"{num_dollars} dollars")

    if num_quarters > 0:
        if num_quarters == 1:
            print(f"{num_quarters} quarter  ")
        else:
            print(f"{num_quarters} quarters  ")

    if num_dimes > 0:
        if num_dimes == 1:
            print(f"{num_dimes} dime  ")
        else:
            print(f"{num_dimes} dimes  ")

    if num_nickels > 0:
        if num_nickels == 1:
            print(f"{num_nickels} nickel ")
        else:
            print(f"{num_nickels} nickels  ")

    if num_pennies > 0:
        if num_pennies == 1:
            print(f"{num_pennies} penny  ")
        else:
            print(f"{num_pennies} pennies  ")    



def main():
    # Logic goes here

    # Generate the amount owed
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe: ${amount_owed:.2f}")

    # Create variable to represent money put into machine
    money_in = float(input("How much cash will you put in the self-checkout? "))

    # Calculate change owed to customer
    change = money_in - amount_owed
    print(f"Change owed: ${change:.2f}")

    # Call the disperse_change function
    disperse_change(change)

# Call the main function
main()