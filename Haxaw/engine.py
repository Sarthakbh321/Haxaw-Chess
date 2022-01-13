import os
import chess
import numpy as np
from tensorflow import keras

"""
Bootstrap decorator. Allows for recursion without actually using recursion. (Not used currently)
"""
from types import GeneratorType
def bootstrap(func, stack=[]):
    def wrapped_function(*args, **kwargs):
        if stack:
            return func(*args, **kwargs)
        else:
            call = func(*args, **kwargs)
            while True:
                if type(call) is GeneratorType:
                    stack.append(call)
                    call = next(call)
                else:
                    stack.pop()
                    if not stack:
                        break
                    call = stack[-1].send(call)
            return call
 
    return wrapped_function



class Engine():
    def __init__(self):
        curr_dir = os.path.dirname(os.path.realpath(__file__))
        self.model = keras.models.load_model(curr_dir + "/neural_weights")
        self.states_parsed = 0

    def evaluate(self, board):
        brd = board.convert_to_representation()
        brd = np.array([brd])
        prediction = self.model.predict(brd)

        return prediction[0]
    

    def black_minimax(self, gs, alpha, beta, depth=2):
        self.states_parsed += 1
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
                value = max(value, self.black_minimax(gs, alpha, beta, depth-1))
                gs.board.pop()

                if(value >= beta):
                    break

                alpha = max(alpha, value)
               
            return value

        else:
            value = float("inf")

            for move in gs.board.legal_moves:
                gs.board.push(move)
                value = min(value, self.black_minimax(gs, alpha, beta, depth-1))
                gs.board.pop()

                if(value <= alpha):
                    break

                beta = min(beta, value)
            
            return value

           
