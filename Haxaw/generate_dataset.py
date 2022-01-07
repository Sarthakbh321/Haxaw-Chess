import pandas as pd
import chess.pgn
from board import Board
import numpy as np


pgn = open("./data/data.pgn")
evaluation = pd.read_csv("./data/stockfish.csv")

def generate(limit):
    training_features, training_labels = [], []
    gameIndex = 0
    positions_parsed = 0

    while(True):

        if(positions_parsed > limit):
            break

        game = chess.pgn.read_game(pgn)
        
        move_scores = evaluation["MoveScores"][gameIndex]
        move_scores = move_scores.split()

        if game is None:
            break
        
        gs = Board()

        for move_index, move in enumerate(game.mainline_moves()):
            
            try:
                centipawn_valuation = move_scores[move_index]
                centipawn_valuation = int(centipawn_valuation)
            except Exception:
                centipawn_valuation = 0

            gs.board.push(move)
            encoded = gs.convert_to_representation()
            
            training_features.append(encoded)
            training_labels.append(centipawn_valuation)
            positions_parsed += 1

        gameIndex += 1
        print("Parsed: %d games and %d positions" % (gameIndex, positions_parsed))
                

    print("Parsed all games")
    training_features = np.array(training_features)
    training_labels = np.array(training_labels)

    return training_features, training_labels
        



if __name__ == "__main__":
    print("Generating dataset...")
    X, Y = generate(100000)
    
    np.savez("dataset/dataset_50k.npz", X, Y)

