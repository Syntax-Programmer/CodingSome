"""
This is the main game entry point of the game.
This handles the gameloop and the initializer functions.

__AUTHOR__ = Anand Maurya
"""

import pygame

from sys import exit, path
from os import listdir
from os.path import join, isfile
from typing import Literal


pygame.init()


screen = pygame.display.set_caption("GameGame")
SCREEN_SIZE = 1200, 800
screen = pygame.display.set_mode(SCREEN_SIZE)


def draw(screen: pygame.Surface) -> None:
    BLACK = (0, 0, 0)
    screen.fill(BLACK)
    pygame.display.update()


def main(screen: pygame.Surface) -> None:
    """
    The main gameloop that executes all the logic of the game.

    @param: screen : pygame.Surface
        The screen that hosts the game.
    """
    timer = pygame.time.Clock()
    fps = 60

    running = True
    while running:
        timer.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        draw(screen)
    pygame.quit()
    exit()


if __name__ == "__main__":
    main(screen)
