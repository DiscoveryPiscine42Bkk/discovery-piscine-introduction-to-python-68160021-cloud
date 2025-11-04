
try:
    
    user_input = input("Enter a number less than 25\n")
    
    start_number = int(user_input)
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit(1)


if start_number > 25:
    print("Error\n")
else:
    
    for number in range(start_number, 26):
        print(f"Inside the loop, my variable is {number}")