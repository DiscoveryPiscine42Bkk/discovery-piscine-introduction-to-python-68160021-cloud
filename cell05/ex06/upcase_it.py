
import sys


args = sys.argv[1:]


if len(args) != 1:
    
    print("none\n")
else:
    
    input_string = args[0]
    uppercased_string = input_string.upper()
    print(f"{uppercased_string}\n")