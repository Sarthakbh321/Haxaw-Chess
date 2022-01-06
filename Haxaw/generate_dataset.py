import pandas as pd
import chess.pgn
from board import Board

pgn = open("./data/data.pgn")
evaluation = pd.read_csv("./data/stockfish.csv")

def generate():

    gameIndex = 0

    while(True):
        game = chess.pgn.read_game(pgn)
        
        move_scores = evaluation["MoveScores"][gameIndex]
        move_scores = list(map(int, move_scores.split()))

        if game is None:
            break
        
        print("Parsing game #%d" % gameIndex)
        gs = Board()

        for move_index, move in enumerate(game.mainline_moves()):
            centipawn_valuation = move_scores[move_index]
            gs.board.push(move)
            print(move ,game.headers["Result"], centipawn_valuation)
            print(gs.board)

        gameIndex += 1
        exit(0)

    print("Parsed all games")
        



if __name__ == "__main__":
    print("Generating dataset...")
    generate()
