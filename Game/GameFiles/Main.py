"""
This is the main game file that executes the game and has
all the initializer functions, json data fetchers and data implementers.
"""

import pygame
import json

from sys import path, exit
from os import listdir
from os.path import join, isfile
from math import ceil
from typing import Literal


pygame.init()


pygame.display.set_caption("Game")
SCREEN_SIZE = 1200, 800
screen = pygame.display.set_mode(SCREEN_SIZE)


def draw(screen: pygame.Surface) -> None:
    WHITE = (255, 255, 255)
    screen.fill(WHITE)
    pygame.display.update()


def main(screen: pygame.Surface) -> None:
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
