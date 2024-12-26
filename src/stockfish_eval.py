ENGINE_PATH = r"C:\Users\Jash\Downloads\stockfish-windows-x86-64-avx2\stockfish\stockfish-windows-x86-64-avx2.exe"
# REPLACE WITH YOUR STOCKFISH ENGINE PATH.

from stockfish import Stockfish

engine = Stockfish(path=ENGINE_PATH)

def get_stats(fen):

    engine.set_fen_position(fen)

    # best_move = engine.get_best_move()
    eval = engine.get_evaluation()

    if eval['type'] == 'cp':
        eval_score = eval['value'] / 100

    elif eval['type'] == 'mate':
        print(f"Mate in {eval['value']} moves.")

    moves = engine.get_top_moves()

    return moves, eval_score

    
