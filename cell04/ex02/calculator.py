
try:
    
    num1 = float(input("Give me the first number: "))
    
    num2 = float(input("Give me the second number: "))
except ValueError:
    print("Invalid input. Please enter valid numbers.")
    exit(1)


print("Thank you!")


addition = num1 + num2
print(f"{num1} + {num2} = {addition}")


subtraction = num1 - num2
print(f"{num1} - {num2} = {subtraction}")


if num2 != 0:
    division = num1 / num2
    
    if division == int(division):
        print(f"{int(num1)} / {int(num2)} = {int(division)}")
    else:
        print(f"{num1} / {num2} = {division}")
else:
    print(f"{num1} / {num2} = Cannot divide by zero")


multiplication = num1 * num2
print(f"{num1} * {num2} = {multiplication}")