
user_input = ""

first_iteration = True


while True:
    if first_iteration:
        
        user_input = input("What you gotta say? : ")
        first_iteration = False
    else:
        
        user_input = input("I got that! Anything else? : ")
        
    
    if user_input == "STOP":
        
        break
    
    