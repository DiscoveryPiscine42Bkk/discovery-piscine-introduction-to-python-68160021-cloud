
try:
    num1 = int(input("Enter the first number:\n"))
    num2 = int(input("Enter the second number:\n"))
except ValueError:
    print("Invalid input. Please enter integers.")
    exit(1)


result = num1 * num2

if result < 0:
    sign_message = "The result is negative."
elif result > 0:
    sign_message = "The result is positive."
else:  
    sign_message = "The result is positive and negative."


print(f"{num1} x {num2} = {result}")


print(sign_message)