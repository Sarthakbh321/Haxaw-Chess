import chess


class Board():
    def __init__(self, fen=chess.STARTING_FEN):
        self.board = chess.Board(fen)
