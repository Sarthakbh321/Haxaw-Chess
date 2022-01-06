import pandas as pd
import chess.pgn
from board import Board

pgn = open("./data/data.pgn")

def generate():

    gameIndex = 0

    while(True):
        game = chess.pgn.read_game(pgn)

        if game is None:
            break
        
        print("Parsing game #%d" % gameIndex)
        gs = Board()

        for move in game.mainline_moves():
            gs.board.push(move)
            print(move ,game.headers["Result"])
            print(gs.board)

        gameIndex += 1
        exit(0)

    print("Parsed all games")
        



if __name__ == "__main__":
    print("Generating dataset...")
    generate()
