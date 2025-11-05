def checkmate(board_rows):
    
    board = [list(row) for row in board_rows]
    board_size = len(board)
    

    king_pos = None
    for r in range(board_size):
        for c in range(board_size):
            if board[r][c] == 'K':
                king_pos = (r, c)
                break
        if king_pos:
            break

    if not king_pos:
        
        print("Error: King not found")
        return False
    
    kr, kc = king_pos

    
    def check_direction(start_r, start_c, dr, dc, piece_types):
        
        r, c = start_r + dr, start_c + dc
        while 0 <= r < board_size and 0 <= c < board_size:
            piece = board[r][c]
            if piece in piece_types:
                
                return True
            if piece != '.':
                
                return False
            r, c = r + dr, c + dc
        return False

    
    for dc in [-1, 1]:
        r, c = kr - 1, kc + dc
        if 0 <= r < board_size and 0 <= c < board_size and board[r][c] == 'P':
            print("Success")
            return True
            
    
    for dc in [-1, 1]:
        r, c = kr + 1, kc + dc
        if 0 <= r < board_size and 0 <= c < board_size and board[r][c] == 'P':
            print("Success")
            return True


    
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if check_direction(kr, kc, dr, dc, ['R', 'Q']):
            print("Success")
            return True

    
    for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        if check_direction(kr, kc, dr, dc, ['B', 'Q']):
            print("Success")
            return True

    
    print("Fail")
    return False

