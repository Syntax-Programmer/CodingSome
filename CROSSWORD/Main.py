"""
This is the main game entry file for the game.
This file contains the main gameloop and functions
that help initialize the module classes.

__AUTHOR__ = "Kriti Bhatnagar" and "Anand Maurya"
"""

import pygame

from sys import exit, path
from os import listdir
from os.path import join, isfile
from typing import Literal
from math import ceil
from WordHandler import Words


pygame.init()


SCREEN_SIZE = 1200, 800
window = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Crossword")


def basic_assets_loader(
    screen_size: tuple[int, int]
) -> dict[pygame.Surface, tuple[int, int]]:
    BG_IMAGE = join("Assets", "BgImage.png")
    bg_image = pygame.image.load(BG_IMAGE).convert()
    bg_image = pygame.transform.scale(bg_image, screen_size)

    BG_WORD_LIST_PATH = join("Assets", "BgWordList.png")
    BG_WORD_LIST_SIZE = screen_size[0], 200
    bg_word_list = pygame.image.load(BG_WORD_LIST_PATH).convert()
    bg_word_list = pygame.transform.scale(bg_word_list, BG_WORD_LIST_SIZE)

    assets_dict = {bg_image: (0, 0), bg_word_list: (0, 600)}
    return assets_dict


def get_grid_pos(
    block_size: tuple[int, int],
    grid_size: tuple[int, int],
    grid_offset: tuple[int, int] = (0, 0),
) -> list[tuple[int, int]]:
    """
    This gets all the pos that the grid squares need to go to.

    @param: block_size : tuple[int, int]
        The size of an individual block of the grid.
    @param: grid_size : tuple[int, int]
        The size of the complete grid.
    @param: grid_offset : tuple[int, int]
        The place where the grid has to be placed.
        This can be used to move the grid on the board.

    @returns: list[tuple[int, int]]
        The list of all the pos of the grid blocks.
    """
    return [
        (i * block_size[0] + grid_offset[0], j * block_size[1] + grid_offset[1])
        for i in range(ceil(grid_size[0] // block_size[0]))
        for j in range(ceil(grid_size[1] // block_size[0]))
    ]


def draw(
    screen: pygame.Surface,
    assets_data: dict[pygame.Surface, tuple[int, int]],
    grid_data: dict[tuple[int, int], list[tuple[int, int]]],
) -> None:
    GRAY = (75, 75, 75)
    for image, pos in assets_data.items():
        screen.blit(image, pos)
    for size, pos_list in grid_data.items():
        for pos in pos_list:
            rect = pygame.Rect(pos, size)
            # ? This draws the border of the grid from the rect.
            pygame.draw.rect(screen, GRAY, rect, 1)
    pygame.display.update()


def main(screen: pygame.Surface) -> None:
    """
    This is the main gameloop of the game.

    @param: screen : pygame.Surface
        The screen that hosts the game.
    """
    screen_size = screen.get_size()

    grid_size = 600, 600
    block_size = 50, 50
    grid_pos = get_grid_pos(block_size, grid_size)
    grid_data = {block_size: grid_pos}

    timer = pygame.time.Clock()
    fps = 60

    assets_data = basic_assets_loader(screen_size)

    running = True
    while running:
        timer.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        draw(screen, assets_data, grid_data)  # type: ignore
    pygame.quit()
    exit()


if __name__ == "__main__":
    main(window)
