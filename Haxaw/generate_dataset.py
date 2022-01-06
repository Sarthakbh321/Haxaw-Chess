import pandas
import chess.pgn


pgn = open("./data/data.pgn")

def generate():

    gameIndex = 0

    while(True):
        game = chess.pgn.read_game(pgn)

        if game is None:
            break
        
        print("Parsing game #%d" %gameIndex)
        board = game.board()
        print(board)
        gameIndex += 1

    print("Parsed all games")
        



if __name__ == "__main__":
    print("Generating dataset...")
    generate()
