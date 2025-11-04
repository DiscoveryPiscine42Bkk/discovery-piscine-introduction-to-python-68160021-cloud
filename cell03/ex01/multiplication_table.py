
try:
    
    table_number = int(input("Enter a number\n"))
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit(1)


for i in range(10):
    result = i * table_number
    
    print(f"{i} x {table_number} = {result}")