
def add_one(number):
    """
    Takes a number, adds 1 to it, and assigns the result to the local variable 'number'.
    """
    
    number = number + 1
    
my_number = 42


print(f"Before method call: {my_number}")


add_one(my_number)


print(f"After method call: {my_number}")