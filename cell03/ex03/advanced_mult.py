
import sys


if len(sys.argv) > 1:
    print("none")
    sys.exit(0)


table_num = 0


while table_num <= 10:
    
    output_line = f"Table de {table_num}:"
    
    
    multiplier = 0
    
    
    while multiplier <= 10:
        
        result = table_num * multiplier
        
        
        output_line += f" {result}"
        
        
        multiplier += 1
    
    
    print(output_line)
    
    
    table_num += 1