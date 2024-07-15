# 

# Step 1: Prompt the user to input two numbers
number1 = 8
number2 = 4

# Step 2: Perform the addition operation
addition = number1 + number2

# Step 3: Perform the subtraction operation
subtraction = number1 - number2

# Step 4: Perform the multiplication operation
multiplication = number1 * number2

# Step 5: Perform the division operation
if number2 != 0:
    division = number1 / number2
else:
    division = "undefined (cannot divide by zero)"

# Step 6: Print the results of each operation with descriptive messages
print(f"\nResults:")
print(f"{number1} + {number2} = {addition}")
print(f"{number1} - {number2} = {subtraction}")
print(f"{number1} * {number2} = {multiplication}")
print(f"{number1} / {number2} = {division}")
