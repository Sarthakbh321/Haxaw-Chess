import chess
import numpy as np
from Haxaw.engine import Engine


class Board():
    def __init__(self, fen=chess.STARTING_FEN):
        self.board = chess.Board(fen)
        self.engine = None

    def convert_to_representation(self):
        
        encoding_dict = {"K": 1, "k": 5, "Q": 9, "q": 10, "R": 11, "r": 12, \
                         "B": 13, "b": 14, "N": 15, "n": 16, "P": 17, "p": 18}


        board_state = np.zeros(65, dtype=np.uint8)

        for i in range(64):
            piece = self.board.piece_at(i)

            if(piece != None):
                p_symbol = piece.symbol()
                board_state[i] = encoding_dict[p_symbol]

                if(p_symbol == "K" or p_symbol == "k"):
                    if(self.board.has_kingside_castling_rights(piece.color) and self.board.has_queenside_castling_rights(piece.color)):
                        board_state[i] += 3
                    elif(self.board.has_kingside_castling_rights(piece.color)):
                        board_state[i] += 1
                    elif(self.board.has_queenside_castling_rights(piece.color)):
                        board_state[i] += 2

        if(self.board.ep_square != None):
            board_state[self.board.ep_square] = 19
        
        # Current board state is after the move has been made. So the player will be opposite of current turn
        if(not self.board.turn == chess.WHITE):
            board_state[64] = 0
        else:
            board_state[64] = 1
            
        return board_state

    def get_best_moves(self):
        if(self.engine == None):
            self.engine = Engine()
        
        self.engine.states_parsed = 0
        evals = []
        for move in self.board.legal_moves:
            self.board.push(move)
            evaluation = self.engine.evaluate(self)
            piece_valuation = self.engine.black_minimax(self, -float("inf"), float("inf")) 
            total_evaluation = 0.7 * evaluation + piece_valuation 

            evals.append((total_evaluation, move, piece_valuation))

            self.board.pop()
        evals.sort(key=lambda x: x[0], reverse=self.board.turn)
        
        print("States evaluated: ", self.engine.states_parsed)
        return evals

    def get_pieces_valuation(self):
        values = {"p": 1, "n": 3, "b": 3, "r": 5, "q": 9, "k": 10000}
        

        current_value = 0
        piece_map = self.board.piece_map()
        for i in piece_map:
            piece = piece_map[i]
            square = chess.SQUARES[i]
            opponent = self.board.turn

            if(piece != None):
                symbol = piece.symbol().lower()

                if(piece.color == chess.BLACK):
                    current_value -= values[symbol]
                else:
                    current_value += values[symbol]
                
                '''
                # if this is your piece and can be taken by the opponent, adjust the valuation
                if(piece.color != opponent and self.board.is_attacked_by(opponent, square)):
                    if(piece.color == chess.BLACK):
                        current_value += values[symbol]
                    else:
                        current_value -= values[symbol]
                '''

        return current_value

   

