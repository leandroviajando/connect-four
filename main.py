import numpy as np
import pygame

from src.game import COLUMNS, ROWS, Player, drop_piece, is_winning_move, print_board
from src.graphics import (
    column,
    draw_board,
    draw_hovering_piece,
    draw_winning_message,
    open_window,
)

if __name__ == "__main__":
    board = np.zeros((ROWS, COLUMNS))
    game_over = False
    turn = 0
    window = open_window()

    print_board(board)
    draw_board(window, board)

    while not game_over:
        player: Player = 1 if turn % 2 == 0 else 2

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEMOTION:
                draw_hovering_piece(window, event, player)

            if event.type == pygame.MOUSEBUTTONDOWN:
                drop_piece(board, column(event), player)

                print_board(board)
                draw_board(window, board)

                if is_winning_move(board, player):
                    winning_message = f"Congrats player {player}!"

                    print(winning_message)
                    draw_winning_message(window, winning_message, player)

                    game_over = True
                else:
                    turn += 1
