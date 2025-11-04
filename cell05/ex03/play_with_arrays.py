


original_array = [2, 8, 9, 48, 8, 22, -12, 2]


unique_results_set = set()


for number in original_array:
    
    if number > 5:
        
        processed_number = number + 2
        
        
        unique_results_set.add(processed_number)


print(original_array)


print(unique_results_set)