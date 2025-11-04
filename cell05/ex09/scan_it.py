
import sys


args = sys.argv[1:]


if len(args) != 2:
    print("none\n")
    sys.exit(0)


keyword = args[0]
search_string = args[1]


occurrence_count = search_string.count(keyword)


if occurrence_count == 0:
    
    print("none\n")
else:
   
    print(f"{occurrence_count}\n")