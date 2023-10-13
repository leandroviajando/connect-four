import math
import pathlib
from typing import Final

import numpy as np
import pygame

from src.game import COLUMNS, ROWS, TITLE, Player

PROJECT_ROOT_PATH: Final = pathlib.Path(__file__).parent.parent
WINNING_IMAGE_PATH: Final = PROJECT_ROOT_PATH / "assets" / "winner.png"

SLOT: Final = 100
WIDTH: Final = COLUMNS * SLOT
HEIGHT: Final = (ROWS + 1) * SLOT
SIZE: Final = (WIDTH, HEIGHT)

RED: Final = (255, 0, 0)
GREEN: Final = (0, 255, 0)
BLUE: Final = (0, 0, 255)
GREY: Final = (128, 128, 128)
OFFSET: Final = 100
RADIUS: Final = int(SLOT / 2 - 5)


def open_window() -> pygame.Surface:
    pygame.init()

    window = pygame.display.set_mode(SIZE)
    pygame.display.set_caption(TITLE)

    return window


def column(event: pygame.event.Event) -> int:
    posx = event.pos[0]

    return math.floor(posx / SLOT)


def draw_board(window: pygame.Surface, board: np.ndarray) -> None:
    pygame.draw.rect(window, GREY, (0, 0, WIDTH, SLOT))
    board = board[::-1, :]

    for col in range(COLUMNS):
        for row in range(ROWS):
            rect = (col * SLOT, row * SLOT + OFFSET, SLOT, SLOT)
            pygame.draw.rect(window, BLUE, rect)

            slot = (int(col * SLOT + SLOT / 2), int(row * SLOT + OFFSET + SLOT / 2))
            pygame.draw.circle(window, GREY, slot, RADIUS)

            if board[row][col] == 1:
                pygame.draw.circle(window, RED, slot, RADIUS)
            elif board[row][col] == 2:
                pygame.draw.circle(window, GREEN, slot, RADIUS)

    pygame.display.update()


def draw_hovering_piece(
    window: pygame.Surface, event: pygame.event.Event, player: Player
) -> None:
    pygame.draw.rect(window, GREY, (0, 0, WIDTH, SLOT))
    posx = event.pos[0]
    piece = (posx, int(SLOT / 2))

    if player == 1:
        pygame.draw.circle(window, RED, piece, RADIUS)
    elif player == 2:
        pygame.draw.circle(window, GREEN, piece, RADIUS)

    pygame.display.update()


def draw_winning_message(
    window: pygame.Surface,
    winning_message: str,
    player: Player,
) -> None:
    font = pygame.font.SysFont("Comic Sans MS", size=33, bold=True)
    image = pygame.image.load(WINNING_IMAGE_PATH)
    label = font.render(winning_message, True, RED if player == 1 else GREEN)

    window.blit(image, (120, 220))
    window.blit(label, (170, 350))

    pygame.display.update()
    pygame.time.wait(3000)
