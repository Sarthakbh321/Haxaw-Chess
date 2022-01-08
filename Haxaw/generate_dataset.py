import os
import pandas as pd
import chess.pgn
from Haxaw.board import Board
import numpy as np


pgn = open(os.path.dirname(os.path.realpath(__file__)) +  "/data/data.pgn")
evaluation = pd.read_csv(os.path.dirname(os.path.realpath(__file__)) + "/data/stockfish.csv")

result_dict = {"1-0": 1, "1/2-1/2": 0, "0-1": -1}


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
            result = result_dict[game.headers["Result"]]

            gs.board.push(move)
            encoded = gs.convert_to_representation()
            
            training_features.append(encoded)
            training_labels.append(result)
            positions_parsed += 1

        gameIndex += 1
        print("Parsed: %d games and %d positions" % (gameIndex, positions_parsed))
                

    print("Parsed all games")
    training_features = np.array(training_features)
    training_labels = np.array(training_labels)

    return training_features, training_labels
        



if __name__ == "__main__":
    print("Generating dataset...")
    X, Y = generate(1e5)
    
    np.savez(os.path.dirname(os.path.realpath(__file__)) + "/dataset/result_based_dataset_1M.npz", X, Y)

