
import sys


args = sys.argv[1:]

if len(args) != 1:
    print("none\n")
    sys.exit(0)

input_string = args[0]
output_chars = ""
z_count = 0


for char in input_string:
    if char == 'z':
        output_chars += "z"
        z_count += 1


if z_count == 0:
    
    print("none\n")
else:
    
    print(f"{output_chars}\n")