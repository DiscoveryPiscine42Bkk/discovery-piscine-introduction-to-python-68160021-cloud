
def array_of_names(name_dict):
    """
    Takes a dictionary of {first_name: last_name} and builds an array 
    (list) of full names, with the first letter of each name capitalized.
    """
    full_names_array = []
    
    
    for first_name, last_name in name_dict.items():
        
        formatted_first = first_name.capitalize()
        formatted_last = last_name.capitalize()
        
        
        full_name = f"{formatted_first} {formatted_last}"
        
        
        full_names_array.append(full_name)
        
    return full_names_array


persons = {
    "jaisai": "cat",
    "mine": "cat",
    "pitta": "cat",
    "earn": "cat"
}


print(array_of_names(persons))