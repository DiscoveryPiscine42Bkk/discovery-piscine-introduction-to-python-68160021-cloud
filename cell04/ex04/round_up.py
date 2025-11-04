
import math


try:
    
    number = float(input("Give me a number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit(1)


rounded_up_number = int(math.ceil(number))


print(rounded_up_number)