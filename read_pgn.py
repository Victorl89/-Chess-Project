
import re
def read_pgn_file(pgn_text):
    #with open(filepath, 'r') as file:
      #  pgn_text = file.read()

    moves = []
    in_moves_section = False
    moves_text = ""

    for line in pgn_text.splitlines():
        # Check if we're in the moves section and sets the flag to True.
        if not in_moves_section and line.startswith("1."):
            in_moves_section = True

        if in_moves_section:
            moves_text += ' ' + line.strip()

    # Removing comments and result tags
    moves_text = moves_text.split('{')[0].split('[')[0].strip()
    moves_text = moves_text.replace("\n", " ").replace("\r", " ")
    moves_text = ' '.join(moves_text.split())  # Normalize whitespace

    # Split moves by identifying move numbers
  
    move_pattern = re.compile(r'\d+\.(\.\.)?\s*')
    moves = move_pattern.split(moves_text)

    # Remove empty strings and digits
    clean_moves = [move for move in moves if move and not move.isdigit() and '.' not in move]
    
    # Further split each move pair into individual moves
    final_moves = []
    for move in clean_moves:
        final_moves.extend(move.strip().split())
    #ισως εχει προβλημα με κινησεις οπως 'axb5

    return final_moves
