
def famous_births(figures_dict):
    """
    Sorts the dictionary of historical figures by their date_of_birth and 
    displays each entry with a welcome message.
    """
    
    sorted_figures = sorted(
        figures_dict.items(), 
        key=lambda item: item[1]["date_of_birth"]
    )
    
    
    for key, data in sorted_figures:
        name = data["name"]
        dob = data["date_of_birth"]
        
        
        print(f"{name} is a great scientist born in {dob}.")


women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}


famous_births(women_scientists)