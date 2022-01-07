import pygame
from Haxaw.board import Board

game_state = Board()

print(game_state.get_best_moves()[:5])
