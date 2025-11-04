
try:
    number = int(input("pleast enter a number: "))

    if number == 0:
        print("this number is equal to zero.")
    else:
        print("This number is diffferent from zero.")

except ValueError:
    print("invalid input. Please enter an integer ")
