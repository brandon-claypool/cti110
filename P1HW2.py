# Brandon Claypool
# 09/24/25
# P1HW2
# Python program helps a user plan for a trip

# Tell the user the purpose of the program
print("This program calculates and displays travel expenses")

# Get travel information from the user
budget = int(input("\nEnter Budget: "))
destination = input("\nEnter your travel destination: ")
gas_money = int(input("\nHow much do you think you will spend on gas? "))
hotel_money = int(input("\nApproximately, how much will you need for accommodation/hotel? "))
food_money = int(input("\nLast, how much do you need for food? "))
122
# Display results
print("\n------------Travel Expenses------------")
print("Location:", destination)
print("Initial Budget:",budget)
print("\nFuel:",gas_money)
print("Accommodation:",hotel_money)
print("Food:",food_money)

remaining_balance = budget - gas_money - hotel_money - food_money

print("\nRemaining Balance:",remaining_balance)