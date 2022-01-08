import os
import pygame
import chess
from Haxaw.board import Board

pygame.init()

WIDTH = HEIGHT = 512
BOARD_DIMENSION = 8
SQ_SIZE = WIDTH//BOARD_DIMENSION
MAX_FPS = 15

BOARD_COLORS = [pygame.Color("white"), pygame.Color("gray")]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(pygame.Color("white"))
clock = pygame.time.Clock()

PIECE_IMAGES = {}
pieces_symbols = ["P", "R", "N", "B", "Q", "K"]

for symbol in pieces_symbols:
    # White pieces
    PIECE_IMAGES[symbol] = pygame.transform.scale(
        pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + "/images/w" + symbol + ".png"), (SQ_SIZE, SQ_SIZE)
    )
    
    # Black pieces
    PIECE_IMAGES[symbol.lower()] =  pygame.transform.scale(
        pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + "/images/b" + symbol + ".png"), (SQ_SIZE, SQ_SIZE)
    )



def main():
    gs = Board()
    
    current_sq_selected = None
    previous_clicks = []

    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                exit(0)
            elif(event.type == pygame.MOUSEBUTTONDOWN):
                location = pygame.mouse.get_pos()

                row = BOARD_DIMENSION - location[1]//SQ_SIZE - 1
                column = location[0]//SQ_SIZE
                
                index = row * BOARD_DIMENSION + column

                sq_selected = chess.SQUARES[index]
                
                if(sq_selected == current_sq_selected):
                    current_sq_selected = None
                    previous_clicks = []
                else:
                    current_sq_selected = sq_selected
                    previous_clicks.append(current_sq_selected)
                
                
                if(len(previous_clicks) == 2):
                    try:
                        move_to_make = gs.board.find_move(from_square=previous_clicks[0], to_square=previous_clicks[1])
                        gs.board.push(move_to_make)
                        try:
                            computer_moves = gs.get_best_moves()
                            gs.board.push(computer_moves[0][1])
                        except Exception as e:
                            print(e)
                    
                        current_sq_selected = None
                        previous_clicks = []

                    except ValueError:
                        current_sq_selected = sq_selected
                        previous_clicks = [current_sq_selected]

        render(screen, gs, current_sq_selected)
        
        outcome = gs.board.outcome()
        if(outcome != None):
            print(outcome.termination)
            print(outcome.result())
            exit(0)

        pygame.display.flip()
        clock.tick(MAX_FPS)


def render(screen, gs, selected_square):
    draw_board(screen)
    draw_square_highlights(screen, gs, selected_square)
    draw_pieces(screen, gs)


def draw_board(screen):
    for row in range(BOARD_DIMENSION):
        for col in range(BOARD_DIMENSION):
            y,x = SQ_SIZE * row, SQ_SIZE * col
            
            color = BOARD_COLORS[(row + col)%2]

            pygame.draw.rect(screen, color, pygame.Rect(x, y, SQ_SIZE, SQ_SIZE))


def draw_square_highlights(screen, gs, selected_square):
    if(selected_square == None):
        return

    moves = gs.board.generate_legal_moves(from_mask=chess.BB_SQUARES[selected_square])
    
    for move in moves:
        to_square = move.to_square
        
        row = BOARD_DIMENSION - to_square//8 - 1
        col = to_square%8
    
        x,y = col * SQ_SIZE, row * SQ_SIZE

        pygame.draw.rect(screen, pygame.Color("red"), pygame.Rect(x, y, SQ_SIZE, SQ_SIZE))

def draw_pieces(screen, gs):
    for row in range(BOARD_DIMENSION):
        for col in range(BOARD_DIMENSION):
            x,y = col * SQ_SIZE, (BOARD_DIMENSION - row - 1) * SQ_SIZE

            index = row * BOARD_DIMENSION + col

            piece = gs.board.piece_at(index)
            
            if(piece != None):
                image = PIECE_IMAGES[piece.symbol()]
                screen.blit(image, pygame.Rect(x, y, SQ_SIZE, SQ_SIZE))

if __name__ == "__main__":
    main()


"""
game_state = Board()
while(game_state.board.outcome() == None):
    moves = game_state.get_best_moves()

    val, move = moves[0]

    game_state.board.push(move)
    print(game_state.board)
    print("----------")

print(game_state.board.result())
"""
