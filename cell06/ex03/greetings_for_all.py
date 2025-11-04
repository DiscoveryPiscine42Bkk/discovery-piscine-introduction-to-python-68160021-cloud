
def greetings(name="noble stranger"):
    """
    Displays a welcome message using the provided name. 
    If the argument is not a string, it displays an error.
    """
    
    if isinstance(name, str):
        print(f"Hello, {name}.\n")
    else:
        
        print("Error! It was not a name.\n")


greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)