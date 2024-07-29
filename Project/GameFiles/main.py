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


def decode_image_filename(
    filename: str,
) -> tuple[str, Literal["R", "L", "N"], tuple[int, int]]:
    # TODO: Parse each of the >1700 images so that it matches the filename parser requirements.
    # TODO: Get Therapy.
    pass


def flip_images_x(image_list: list[pygame.Surface]) -> list[pygame.Surface]:
    return [pygame.transform.flip(image, True, False) for image in image_list]


def flip_images_y(image_list: list[pygame.Surface]) -> list[pygame.Surface]:
    return [pygame.transform.flip(image, False, True) for image in image_list]


def decode_sprite_sheets(
    sprite_dir_path: str, scaled_size: tuple[int, int]
) -> dict[str, list[pygame.Surface]]:
    pass


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
