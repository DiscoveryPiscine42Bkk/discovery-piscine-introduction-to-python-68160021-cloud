


try:
    number = int(input())
except ValueError:
    
    print("Invalid input. Please enter an integer.")
    exit(1)

if number < 0:
    print("This number is negative.")
elif number > 0:
    print("This number is positive.")
else:  
    print("This number is both positive and negative.")