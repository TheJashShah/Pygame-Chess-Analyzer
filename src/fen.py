from piece import Piece

def parse_fen(FEN):

    FEN = FEN.split(' ')[0]

    WHITE = ["K", "P", "B", "N", "R", "Q"]
    BLACK = ["k", "p", "b", "n", "r", "q"]

    piece_list = [[None] * 8 for _ in range(8)]
    row = 0
    col = 0

    for char in FEN:
        
        if char in BLACK:
            piece_list[row][col] = Piece(0, 0, BLACK.index(char), 0)
            col += 1

        elif char in WHITE:
            piece_list[row][col] = Piece(0, 0, WHITE.index(char), 1)
            col += 1

        elif char == "/":
            row += 1
            col = 0
            
        elif char.isdigit():
            col += int(char)

    return piece_list
