import numpy as np

from typing import Final, Literal

ROWS: Final = 6
COLUMNS: Final = 7
TITLE: Final = "Connect 4"

Player = Literal[1, 2]


def is_valid_location(board: np.ndarray, col: int) -> bool:
    return col in range(COLUMNS) and board[ROWS - 1][col] == 0


def drop_piece(board: np.ndarray, col: int, piece: int) -> None:
    for row in range(ROWS):
        if board[row][col] == 0:
            board[row][col] = piece
            return


def is_winning_move(board: np.ndarray, piece: int) -> bool:
    for row in range(ROWS - 3):
        for col in range(COLUMNS):
            if (
                board[row][col] == piece
                and board[row + 1][col] == piece
                and board[row + 2][col] == piece
                and board[row + 3][col] == piece
            ):
                return True

    for col in range(COLUMNS - 3):
        for row in range(ROWS):
            if (
                board[row][col] == piece
                and board[row][col + 1] == piece
                and board[row][col + 2] == piece
                and board[row][col + 3] == piece
            ):
                return True

    for row in range(ROWS - 3):
        for col in range(COLUMNS - 3):
            if (
                board[row][col] == piece
                and board[row + 1][col + 1] == piece
                and board[row + 2][col + 2] == piece
                and board[row + 3][col + 3] == piece
            ):
                return True

    for row in range(3, ROWS):
        for col in range(COLUMNS - 3):
            if (
                board[row][col] == piece
                and board[row - 1][col + 1] == piece
                and board[row - 2][col + 2] == piece
                and board[row - 3][col + 3] == piece
            ):
                return True

    return False


def print_board(board: np.ndarray) -> None:
    print(np.flip(board, 0))
