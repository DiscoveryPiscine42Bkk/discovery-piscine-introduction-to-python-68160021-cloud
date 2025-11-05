from checkmate import checkmate

def example1_fail():
    board = (
        "....",
        ".P..",
        ".B..",
        "...K"
    )
   
    print("--- Example 1 (Fail) ---")
    checkmate(board)

def example2_success():
    board = (
        "B...",
        "....",
        "....",
        "...K"
    )
    
    print("--- Example 2 (Success) ---")
    checkmate(board)


def example3_success():
    board = (
        "....",
        "R.K.",
        "....",
        "...."
    )
    
    print("--- Example 3 (Success) ---")
    checkmate(board) 


def example4_success():
    
    board = (
        "....",
        "....",
        "..K.",
        ".P.."
    )
    
    print("--- Example 4 (Success - Pawn) ---")
    checkmate(board) 


def example5_fail():
    board = (
        "B...",
        ".R..", 
        "....",
        "...K"
    )
    
    print("--- Example 5 (Fail - Blocked) ---")
    checkmate(board) 

if __name__ == "__main__":
    example1_fail()
    example2_success()
    example3_success()
    example4_success()
    example5_fail()