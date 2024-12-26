import chess

def PGN_TO_FEN(PGN):

    board = chess.Board()
    
    PGN = PGN.replace("\n", " ")
    PGN = PGN.replace("\r", " ")

    move_list = PGN.split(" ")
    move_list = move_list[:-1]

    move_tuples = []

    FEN_LIST = [board.fen() + "\n"]

    for idx, move in enumerate(move_list):

        if move.split(".")[0].isdigit():

            moves = [move.split(".")[1], move_list[idx + 1]]
            move_tuples.append(moves)
  
    for pair in move_tuples:

        for move in pair:

            if move != '':

                board.push_san(move)
                FEN_LIST.append(board.fen() + "\n")

    with open("src/fen.txt", "w") as file:
        file.writelines(FEN_LIST)

    return move_tuples
