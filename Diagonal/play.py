import pygame
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


def main():
    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                exit(0)
        
        render(screen)
        pygame.display.flip()
        clock.tick(MAX_FPS)


def render(screen):
    draw_board(screen)


def draw_board(screen):
    for row in range(BOARD_DIMENSION):
        for col in range(BOARD_DIMENSION):
            y,x = SQ_SIZE * row, SQ_SIZE * col
            
            color = BOARD_COLORS[(row + col)%2]

            pygame.draw.rect(screen, color, pygame.Rect(x, y, SQ_SIZE, SQ_SIZE))




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
