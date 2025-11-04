
import sys



def shrink(input_string):
    """
    Displays the first eight characters of the input string using slices.
    Applies to strings with length > 8.
    """
    
    shrunk_string = input_string[0:8]
    print(shrunk_string)

def enlarge(input_string):
    """
    Appends 'Z' characters to make the total length eight, then displays the result.
    Applies to strings with length < 8.
    """
    current_length = len(input_string)
    
    
    z_count = 8 - current_length
    
    
    enlarged_string = input_string + ('Z' * z_count)
    print(enlarged_string)



parameters = sys.argv[1:]
num_parameters = len(parameters)


if num_parameters < 1:
    print("none\n")
    sys.exit(0)


for param in parameters:
    param_length = len(param)
    
    if param_length > 8:
        
        shrink(param)
    elif param_length < 8:
        
        enlarge(param)
    else:
        
        print(param)