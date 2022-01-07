import os
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
        
