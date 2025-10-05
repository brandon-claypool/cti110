# Brandon Claypool
# 10/05/25
# P2LAB2 - Dictionary MPG Calculator
# This program uses a dictionary to store vehicle MPG values.
# It asks the user to select a vehicle and enter miles to calculate
# how many gallons of gas are needed for that trip.

# --- Create dictionary of vehicles and MPG values ---
vehicle_mpg = {
    'Camaro': 18.21,
    'Prius': 52.36,
    'Model S': 110,
    'Silverado': 26
}

# --- Get dictionary keys and display them ---
keys = vehicle_mpg.keys()
print(keys)

# --- Prompt user for vehicle choice ---
vehicle = input("\nEnter a vehicle to see it's mpg: ")

# --- Display selected vehicle's mpg ---
mpg = vehicle_mpg[vehicle]
print(f"\nThe {vehicle} gets {mpg} mpg.")

# --- Prompt user for miles to drive ---
miles = float(input(f"\nHow many miles will you drive the {vehicle}? "))

# --- Calculate gallons needed ---
gallons_needed = miles / mpg

# --- Display final result rounded to 2 decimals ---
print(f"\n{gallons_needed:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles:.1f} miles.")
