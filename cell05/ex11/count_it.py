
import sys


parameters = sys.argv[1:]
num_parameters = len(parameters)


if num_parameters == 0:
    print("none\n")
    sys.exit(0)


print(f"parameters: {num_parameters}\n")


for param in parameters:
    length = len(param)
    print(f"{param}: {length}\n")