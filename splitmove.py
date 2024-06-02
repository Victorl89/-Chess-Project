import re
board = [
    ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
    ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
    ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
    ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
    ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
    ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
    ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
    ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
]


def split_chess_move(move_str):
    # Regular expression to parse the move
    col_map = {
        "a": "0",
        "b": "1",
        "c": "2",
        "d": "3",
        "e": "4",
        "f": "5",
        "g": "6",
        "h": "7"
    }
    row_map = {
       "8": "0",
       "7": "1",
       "6": "2",
       "5": "3",
       "4": "4",
       "3": "5",
       "2": "6",
       "1": "7"
   }
    move_pattern = re.compile(
        r"([KQRBN])?([a-h])?x?([a-h][1-8])(=?[QRBN])?[+#]?")
    match = move_pattern.match(move_str)

    if match:
        piece = match.group(1)  # Piece (optional)
        source_file = match.group(2)  # Source file for captures (optional)
        capture = 'x' if 'x' in move_str else ''  # Capture indicator
        destination = match.group(3)  # Destination square
        promotion = match.group(4)  # Promotion (optional)
        # Check or mate (optional)
        check_or_mate = move_str[-1] if move_str[-1] in ['+', '#'] else ''

        # Split the destination into its components
        file, rank = col_map[destination[0]], row_map[destination[1]]

        # Construct the move array
        move = []
        if piece:
            move.append(piece)
        if source_file:
            move.append(source_file)
        if capture:
            move.append(capture)
        move.append(file)
        move.append(rank)
        if promotion:
            move.extend(['=', promotion[-1]])  # Promotion, e.g., "=Q"
        if check_or_mate:
            move.append(check_or_mate)
    else:
        move = list(move_str)

    return move

# συναρτηση που βρισκει σε ποιες θεσεις ειναι τα πιονια


def find_piece_positions(board, piece_name,next_move):
    rows = '87654321'
    cols = 'abcdefgh'
    positions = []
    move = list(next_move)
    target_piece = move[0]  # Το κομμάτι που μετακινείται, π.χ., 'R'
    target_column = move[1]  # Η στήλη του προορισμού, π.χ., 'e'
    target_row = int(move[2]) - 1  # Η γραμμή του προορισμού (μετατροπή σε δείκτη πίνακα)
    
    col_index = cols.index(target_column)  # Μετατροπή της στήλης σε δείκτη πίνακα
    row_index = 8 - int(move[2])  # Μετατροπή της γραμμής σε δείκτη πίνακα

    if target_piece == 'R':
        # Έλεγχος στη συγκεκριμένη στήλη
        for row in range(8):
            if board[row][col_index] == piece_name:
                positions.append(f"{cols[col_index]}{rows[row]}")
        
        # Έλεγχος στη συγκεκριμένη γραμμή
        for col in range(8):
            if board[row_index][col] == piece_name:
                positions.append(f"{cols[col]}{rows[row_index]}")
    elif target_piece == 'B':
        # Έλεγχος της κύριας διαγωνίου (από πάνω αριστερά προς κάτω δεξιά)
        for i in range(-7, 8):
            r = row_index + i
            c = col_index + i
            if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == piece_name:
                positions.append(f"{cols[c]}{rows[r]}")
        
        # Έλεγχος της άλλης διαγωνίου (από πάνω δεξιά προς κάτω αριστερά)
        for i in range(-7, 8):
            r = row_index + i
            c = col_index - i
            if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == piece_name:
                positions.append(f"{cols[c]}{rows[r]}")
    elif target_piece == 'N':
        # Όλες οι πιθανές κινήσεις του ίππου
        knight_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        
        for move in knight_moves:
            r = row_index + move[0]
            c = col_index + move[1]
            if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == piece_name:
                positions.append(f"{cols[c]}{rows[r]}")
    else :         
        for i in range(len(board)):
            for j in range(len(board[i])):
                    if board[i][j] == piece_name:
                        positions.append(f"{cols[j]}{rows[i]}")
        

    return positions


def positions_of_pawn(current_board, move, color):
    move = split_chess_move(move)
    col_map = {
        "0": "a",
        "1": "b",
        "2": "c",
        "3": "d",
        "4": "e",
        "5": "f",
        "6": "g",
        "7": "h"
    }
    row_map = {
       "0": "8",
       "1": "7",
       "2": "6",
       "3": "5",
       "4": "4",
       "5": "3",
       "6": "2",
       "7": "1"
   }

    # Analyzing the move
    is_capture = 'x' in move
    is_promotion = '=' in move
    is_check_or_mate = any(ch in move for ch in ['+', '#'])

    # capture
    if is_capture:

        move_type = 'capture'
        #Knight
        if move[0] == 'N':
            next_move = move[0]+col_map[move[2]]+row_map[move[3]]
            if color == 0:
                position = (find_piece_positions(current_board, 'wN', next_move))
                previous_move = ", ".join(position)
                print(previous_move)

            if color == 1:
                position = (find_piece_positions(current_board, 'bN', next_move))
                previous_move = ", ".join(position)
                print(previous_move)

                
        #Rook
        elif move[0] == 'R':
            # Rook
            next_move = move[0]+col_map[move[2]]+row_map[move[3]]
            if color == 0:
                position = (find_piece_positions(current_board, 'wR',next_move))
                previous_move = ", ".join(position)
                print(previous_move)

            if color == 1:
                position = (find_piece_positions(current_board, 'bR',next_move))
                previous_move = ", ".join(position)
                print(previous_move)

                
        #Bishop
        elif move[0] == 'B':
            
            next_move = move[0]+col_map[move[2]]+row_map[move[3]]
            if color == 0:
                position = (find_piece_positions(current_board, 'wB', next_move))
                previous_move = ", ".join(position)
                print(previous_move)
                

            if color == 1:
                position = (find_piece_positions(current_board, 'bB', next_move))
                previous_move = ", ".join(position)
                print(previous_move)
            print(next_move)
                
        #Queen
        elif move[0] == 'Q':
            # Queen
            next_move = move[0]+col_map[move[2]]+row_map[move[3]]
            if color == 0:
                position = (find_piece_positions(current_board, 'wQ', next_move))
                previous_move = ", ".join(position)
                print(previous_move)
                

            if color == 1:
                position = (find_piece_positions(current_board, 'bQ', next_move))
                previous_move = ", ".join(position)
                print(previous_move)
            print(next_move)
                
        #King
        elif move[0] == 'K':
            # King
            next_move = move[0]+col_map[move[2]]+row_map[move[3]]
            if color == 0:
                position = (find_piece_positions(current_board, 'wK', next_move))
                previous_move = ", ".join(position)
                print(previous_move)
                

            if color == 1:
                position = (find_piece_positions(current_board, 'bK', next_move))
                previous_move = ", ".join(position)
                print(previous_move)
            print(next_move)
               
        #pawn
        else:
            # pawn
            if color == 0:
                previous_move = move[0] + row_map[str(int(move[3])+1)]
                next_move = col_map[move[2]]+row_map[move[3]]
                print(previous_move)
                print(next_move)

                


            if color == 1:
                previous_move = move[0] + row_map[str(int(move[3])-1)]
                next_move = col_map[move[2]]+row_map[move[3]]
                print(previous_move)
                print(next_move)


    # promotion
    elif is_promotion:
        move_type = 'promotion'
        if color == 0:
            previous_move = col_map[move[0]]+row_map[str(int(move[1])+1)]
        else:
            previous_move = col_map[move[0]]+row_map[str(int(move[1])-1)]
        next_move = move[3]+col_map[move[0]]+row_map[move[1]]
        print(previous_move)
        print(next_move)

    # check or mate
    elif is_check_or_mate:
        move_type = 'check_or_mate'
        #Knight
        if move[0] == 'N':
            next_move = move[0]+col_map[move[1]]+row_map[move[2]]
            if color == 0:
                position = (find_piece_positions(current_board, 'wN', next_move))
                previous_move = ", ".join(position)
                print(previous_move)

            if color == 1:
                position = (find_piece_positions(current_board, 'bN', next_move))
                previous_move = ", ".join(position)
                print(previous_move)

                
        #Rook
        elif move[0] == 'R':
            # Rook
            next_move = move[0]+col_map[move[1]]+row_map[move[2]]
            if color == 0:
                position = (find_piece_positions(current_board, 'wR',next_move))
                previous_move = ", ".join(position)
                print(previous_move)

            if color == 1:
                position = (find_piece_positions(current_board, 'bR',next_move))
                previous_move = ", ".join(position)
                print(previous_move)

                
        #Bishop
        elif move[0] == 'B':
            
            next_move = move[0]+col_map[move[1]]+row_map[move[2]]
            if color == 0:
                position = (find_piece_positions(current_board, 'wB', next_move))
                previous_move = ", ".join(position)
                print(previous_move)
                print(position)
                

            if color == 1:
                position = (find_piece_positions(current_board, 'bB', next_move))
                previous_move = ", ".join(position)
                print(previous_move)
            print(next_move)
                
        #Queen
        elif move[0] == 'Q':
            # Queen
            next_move = move[0]+col_map[move[1]]+row_map[move[2]]
            if color == 0:
                position = (find_piece_positions(current_board, 'wQ', next_move))
                previous_move = ", ".join(position)
                print(previous_move)
                

            if color == 1:
                position = (find_piece_positions(current_board, 'bQ', next_move))
                previous_move = ", ".join(position)
                print(previous_move)
            print(next_move)
                
        #King
        elif move[0] == 'K':
            # King
            next_move = move[0]+col_map[move[1]]+row_map[move[2]]
            if color == 0:
                position = (find_piece_positions(current_board, 'wK', next_move))
                previous_move = ", ".join(position)
                print(previous_move)
                

            if color == 1:
                position = (find_piece_positions(current_board, 'bK', next_move))
                previous_move = ", ".join(position)
                print(previous_move)
            print(next_move)
               
        #pawn
        else:
            # pawn
            if color == 0:
                previous_move = move[0] + row_map[str(int(move[2])+1)]
                next_move = col_map[move[1]]+row_map[move[2]]
                print(previous_move)
                print(next_move)

                


            if color == 1:
                previous_move = move[0] + row_map[str(int(move[2])-1)]
                next_move = col_map[move[1]]+row_map[move[2]]
                print(previous_move)
                print(next_move)

    # standard
    else:
        move_type = 'standard'
        # knight
        if move[0] == 'N':
            next_move = move[0]+col_map[move[1]]+row_map[move[2]]
            if color == 0:
                position = (find_piece_positions(current_board, 'wN',next_move))
                previous_move = ", ".join(position)
                print(previous_move)

            if color == 1:
                position = (find_piece_positions(current_board, 'bN',next_move))
                previous_move = ", ".join(position)
                print(previous_move)

            
            print(next_move)
        # bishop
        elif move[0] == 'B':
            next_move = move[0]+col_map[move[1]]+row_map[move[2]]
            if color == 0:
                position = (find_piece_positions(current_board, 'wB',next_move))
                previous_move = ", ".join(position)
                print(previous_move)

            if color == 1:
                position = (find_piece_positions(current_board, 'bB',next_move))
                previous_move = ", ".join(position)
                print(previous_move)

            
            print(next_move)
        ## rook
        elif move[0] == 'R':
            
            next_move = move[0]+col_map[move[1]]+row_map[move[2]]
            if color == 0:
                # list with location of 2 panws
        
                position = (find_piece_positions(current_board, 'wR',next_move))
                previous_move = ", ".join(position)
                print(previous_move)

            if color == 1:
                
                position = (find_piece_positions(current_board, 'bR',next_move))
                previous_move = ", ".join(position)
                print(previous_move)
            
            print(next_move)
        # queen
        elif move[0] == 'Q':
            next_move = move[0]+col_map[move[1]]+row_map[move[2]]
            if color == 0:
                position = (find_piece_positions(current_board, 'wQ', next_move))
                previous_move = ", ".join(position)
                print(previous_move)

            else:
                position = (find_piece_positions(current_board, 'bQ', next_move))
                previous_move = ", ".join(position)
                print(previous_move)
            
            print(next_move)
        # king
        elif move[0] == 'K':
            next_move = move[0]+col_map[move[1]]+row_map[move[2]]
            if color == 0:
                position = (find_piece_positions(current_board, 'wK', next_move))
                previous_move = ", ".join(position)
                
                print(previous_move)
                print(next_move)
            else:
                position = (find_piece_positions(current_board, 'bK', next_move))
                previous_move = ", ".join(position)
            
                print(previous_move)
                print(next_move)
        # pawns
        else:
            
            if color == 0:  # white
               
                if current_board[(int(move[1])+1)][int(move[0])] == '  ':
                    previous_move = col_map[move[0]]+row_map[str(int(move[1])+2)]

                else:
                    previous_move = col_map[move[0]]+row_map[str(int(move[1])+2)]
                    
                    previous_move = col_map[move[0]]+row_map[str(int(move[1])+1)]
            else:  # black
                if move[0]+str(int(move[1])+1) == '  ':
                    previous_move = col_map[move[0]]+str(int(move[1])+2)

                else:
                    previous_move = col_map[move[0]]+str(int(move[1])+1)

            next_move = col_map[move[0]]+row_map[move[1]]
            print(previous_move)
            print(next_move)
    return move_type, move


# Example usage:
moves = [ "Qh5+", "Bh5", "Bh7", "Bh8"]
for m in moves:
    move_type, move_components = positions_of_pawn(board, m, 0)
    print(f"Move: {m} -> Type: {move_type}, Components: {move_components}")

moves_black = ["Ba6"]
for m in moves_black:
    move_type, move_components = positions_of_pawn(board, m, 1)
    print(f"Move: {m} -> Type: {move_type}, Components: {move_components}")
