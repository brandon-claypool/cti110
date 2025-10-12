# Brandon Claypool
# 10/12/2025
# P2HW1
# Edit & enhance the P1HW2 travel-budget program to display nicely formatted results.

print("This program calculates and displays travel expenses")

# Inputs as floats
budget       = float(input("\nEnter Budget: "))
destination  = input("\nEnter your travel destination: ")
gas_money    = float(input("\nHow much do you think you will spend on gas? "))
hotel_money  = float(input("\nApproximately, how much will you need for accommodation/hotel? "))
food_money   = float(input("\nLast, how much do you need for food? "))

remaining_balance = budget - gas_money - hotel_money - food_money

def money(x) -> str:  # defines a helper that formats a number as a dollar string
    return f"${x:.2f}" # returns a new string with '$' and 2 decimals

COL1 = 20   # label column width
COL2 = 20   # value column width
TOTAL = COL1 + COL2

title = "Travel Expenses"
print(f"\n{'-'*12}{title:^{TOTAL-24}}{'-'*12}")     # Title line with 12 dashes on each side
print(f"{'Location:':<{COL1}}{destination:<{COL2}}")    # Location line with 2 columns, pull from user input
print(f"{'Initial Budget:':<{COL1}}{money(budget):<{COL2}}")     # Initial budget line with 2 columns
print(f"{'Fuel:':<{COL1}}{money(gas_money):<{COL2}}")   # Fuel line with 2 columns
print(f"{'Accommodation:':<{COL1}}{money(hotel_money):<{COL2}}")    # Accommodations line with 2 columns
print(f"{'Food:':<{COL1}}{money(food_money):<{COL2}}")  # Food line with 2 columns
print("-" * TOTAL)  # brackets the travel expenses brief with dashes using the TOTAL value established above and used in the title line

print(f"\nRemaining Balance: {money(remaining_balance)}") # Remaining balance line
