
def find_the_redheads(family_dict):
    """
    Takes a dictionary {name: hair_color} and uses the filter function 
    to return a list of first names of individuals with "red" hair.
    """
    
    redhead_items = filter(lambda item: item[1] == "red", family_dict.items())
    
    
    redhead_names = [item[0] for item in redhead_items]
    
    return redhead_names


dupont_family = {
    "jaisai": "red",
    "mine": "blond",
    "pitta": "brunette",
    "earn": "red",
    "ryu": "red"
}


print(find_the_redheads(dupont_family))