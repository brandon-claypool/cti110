# Brandon Claypool
# P4LAB2
# This program displays a multiplication table using both while and for loops.

# Outer loop controls if the program repeats (sentinel value = "no")
run_again = "yes"

while run_again.lower() == "yes":
    # Ask user for an integer
    num = int(input("Enter an integer: "))

    # Validate input
    if num < 0:
        print("Cannot accept negative values.")
    else:
        print(f"\nMultiplication table for {num}:\n")
        # Use a for loop to generate table 1–12
        for i in range(1, 13):
            print(f"{num} x {i} = {num * i}")

    # Ask if user wants to run again
    print()  # blank line for readability
    run_again = input("Do you wish to run the program again? (yes/no): ")

print("\nProgram ended.")
