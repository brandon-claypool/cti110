# Brandon Claypool
# 10/12/2025
# P2HW2
# Python program helps a user plan for a trip

# Pseudocode
# First, tell the user the purposes of the program
# Next, have the user input all the necessary information
# Display a summary of the travel expenses
# Output the remaining balance after expenses

# First, tell the user the purpose of the program
print("This program calculates and displays travel expenses")

# Next, have the user input all the necessary information
budget = int(input("\nEnter Budget: "))
destination = input("\nEnter your travel destination: ")
gas_money = int(input("\nHow much do you think you will spend on gas? "))
hotel_money = int(input("\nApproximately, how much will you need for accommodation/hotel? "))
food_money = int(input("\nLast, how much do you need for food? "))

# Display a summary of the travel expenses
print("\n------------Travel Expenses------------")
print("Location:", destination)
print("Initial Budget:",budget)
print("\nFuel:",gas_money)
print("Accommodation:",hotel_money)
print("Food:",food_money)

# Output the remaining balance after expenses
remaining_balance = budget - gas_money - hotel_money - food_money

print("\nRemaining Balance:",remaining_balance)