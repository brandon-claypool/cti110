# Brandon Claypool
# 10/26/2025
# P2HW1
# Edit & enhance the P1HW2 travel-budget program to display nicely formatted results.

print("This program calculates and displays travel expenses")

# Inputs as floats
budget       = float(input("\nEnter Budget: "))
destination  = input("\nEnter your travel destination: ")
gas_money    = float(input("\nHow much do you think you will spend on gas? "))
hotel_money  = float(input("\nApproximately, how much will you need for accommodation/hotel? "))
food_money   = float(input("\nLast, how much do you need for food? "))

# Calculate remaining balance
remaining_balance = budget - gas_money - hotel_money - food_money

# Display formatted output
print("\n------------Travel Expenses------------")
print(f"{'Location:':20}{destination}")
print(f"{'Initial Budget:':20}${budget:.2f}")
print(f"{'Fuel:':20}${gas_money:.2f}")
print(f"{'Accommodation:':20}${hotel_money:.2f}")
print(f"{'Food:':20}${food_money:.2f}")
print("----------------------------------------")
print(f"{'Remaining Balance:':20}${remaining_balance:.2f}")
