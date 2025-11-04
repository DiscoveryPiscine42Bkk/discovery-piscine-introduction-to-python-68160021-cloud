
import sys


args = sys.argv[1:]


if len(args) != 2:
    print("none\n")
    sys.exit(0)

try:
    
    num1 = int(args[0])
    num2 = int(args[1])
    
    
    start = min(num1, num2)
    end = max(num1, num2)
    
    
    number_array = list(range(start, end + 1))
    
    
    print(number_array)
    
except ValueError:
    # Handle cases where the arguments are not valid integers
    print("Invalid numbers provided.\n")
    sys.exit(1)