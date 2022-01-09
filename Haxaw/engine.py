import os
import chess
import numpy as np
from tensorflow import keras


class Engine():
    def __init__(self):
        curr_dir = os.path.dirname(os.path.realpath(__file__))
        self.model = keras.models.load_model(curr_dir + "/neural_weights")

    def evaluate(self, board):
        brd = board.convert_to_representation()
        brd = np.array([brd])
        prediction = self.model.predict(brd)

        return prediction[0]
    

    def black_minimax(self, gs, depth=2):
        outcome = gs.board.outcome()
        if(outcome != None):
            if(outcome.result() == "1/2-1/2"): return 0
            elif(outcome.result() == "1-0"): return 100000
            else: return -100000

        if(depth == 0):
            return gs.get_pieces_valuation()

        current_player = gs.board.turn
        if(current_player == chess.WHITE):
            value = -float("inf")

            for move in gs.board.legal_moves:
                gs.board.push(move)
                value = max(value, self.black_minimax(gs, depth-1))
                gs.board.pop()
               
            return value

        else:
            value = float("inf")

            for move in gs.board.legal_moves:
                gs.board.push(move)
                value = min(value, self.black_minimax(gs, depth-1))
                gs.board.pop()
            
            return value

           
