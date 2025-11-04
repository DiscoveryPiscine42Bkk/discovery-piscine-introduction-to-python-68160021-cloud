
import sys

if len(sys.argv) != 2:
    
    print("none\n")
    sys.exit(0)


required_parameter = sys.argv[1]


user_word = input("What was the parameter? ")


if user_word == required_parameter:
    print("Good job!")
else:
    
    print("Nope, sorry...\n")