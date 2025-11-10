# Brandon Claypool
# 11/09/2025
# P4HW1 - Score List and Grade Calculation
# Program collects a number of scores, validates input, removes the lowest score,
# calculates the average of remaining scores, and displays the corresponding letter grade.

"""
Pseudocode
1. Ask the user how many scores they want to enter
2. Create an empty list named scores
3. Use a for loop (with range) to repeat that many times:
    a. Ask user for a score.
    b. While the entered score is not between 0 and 100:
        - Display “INVALID Score entered!!!!”
        - Display “Score should be between 0 and 100”
        - Ask again for a valid score.
    c. Once valid, add score to the list.
4. After loop ends:
    a. Find and display the lowest score.
    b. Remove the lowest score from the list to make a modified list.
    c. Calculate the average of the modified list.
5. Determine letter grade based on the average:
        - 90–100 → A
        - 80–89  → B
        - 70–79  → C
        - 60–69  → D
        - Below 60 → F
6. Display all results in the same way provided by the png files
"""






# Step 1: Ask for number of scores
num_scores = int(input("How many scores do you want to enter? "))

# Step 2: Create empty list
scores = []

# Step 3: Collect valid scores using a loop
for i in range(1, num_scores + 1):
    score = float(input(f"Enter score #{i}: "))
    
    # Validation loop
    while score < 0 or score > 100:
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{i} again: "))
    
    scores.append(score)

# Step 4: Calculations
lowest = min(scores)
scores.remove(lowest)
average = sum(scores) / len(scores)

# Step 5: Determine letter grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# Step 6: Display formatted results
print("\n------------Results------------")
print(f"Lowest Score     : {lowest:.1f}")
print(f"Modified List    : {scores}")
print(f"Scores Average   : {average:.2f}")
print(f"Grade            : {grade}")
print("--------------------------------")
