import pygame
from Haxaw.board import Board

game_state = Board()

while(game_state.board.outcome() == None):
    moves = game_state.get_best_moves()

    val, move = moves[0]

    game_state.board.push(move)
    print(game_state.board)
    print("----------")

print(game_state.board.result())

