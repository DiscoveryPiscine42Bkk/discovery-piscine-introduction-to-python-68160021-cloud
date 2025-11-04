
import sys


args = sys.argv[1:]


if len(args) != 1:
    
    print("none\n")
else:
    
    input_string = args[0]
    lowercased_string = input_string.lower()
    print(f"{lowercased_string}\n")