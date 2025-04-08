# Taking input for the day of the week and converting it to lowercase
day_of_week = input("Enter day_of_week: ").lower()
print("day_of_week is", day_of_week)

# Checking if the day is Saturday or Sunday
if day_of_week == "saturday" or day_of_week == "sunday":
    print("We learn DevOps.")  # If it's a weekend, print this message
else:
    print("We do office work.")  # If it's a weekday, print this message

# Taking two numbers as input from the user
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

# Asking the user to choose an arithmetic operation
choice = input("Choose operation (+, -, *, /, %): ")

# Performing the operation based on user choice
if choice == "+":  # Addition
    sum_of_num = num1 + num2
    print("Sum is", sum_of_num)

elif choice == "-":  # Subtraction
    sub_of_num = num1 - num2
    print("Subtraction is", sub_of_num)

elif choice == "*":  # Multiplication
    mul_of_num = num1 * num2
    print("Multiplication is", mul_of_num)

elif choice == "/":  # Division
    if num2 != 0:  # Checking for division by zero
        div_of_num = num1 / num2
        print("Division is", div_of_num)
    else:
        print("Error: Division by zero is not allowed.")

elif choice == "%":  # Modulus (Remainder)
    if num2 != 0:
        mod_of_num = num1 % num2
        print("Remainder is", mod_of_num)
    else:
        print("Error: Modulus by zero is not allowed.")

else:  
    print("Invalid operator")  # If the user enters an unsupported operator
