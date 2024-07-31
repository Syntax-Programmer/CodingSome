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
from math import ceil


pygame.init()


screen = pygame.display.set_caption("Platformer Game")
SCREEN_SIZE = 1500, 800
screen = pygame.display.set_mode(SCREEN_SIZE)


def parse_filename(
    filename: str,
) -> tuple[str, Literal["Right", "Left", "None"], tuple[int, int]]:
    """
    This takes in a filename and extracts data from it.

    @param: filename : str
        The filename of an image in the format (name direction size).

    @returns: tuple[str, Literal["R", "L", "N"], tuple[int, int]]
        The extracted data from the filename.
    """
    filename = filename.removesuffix(".png")
    filename = filename.strip(" ")
    name, direction, size = filename.split(" ", 2)
    size = size[1:-1]
    size = size.split("x")
    size = tuple(map(int, size))
    return name, direction, size  # type: ignore


def flip_images_x(image_list: list[pygame.Surface]) -> list[pygame.Surface]:
    """
    This flips all the images in a list in the x direction.

    @param: image_list : list[pygame.Surface]
        The list of the images to flip.

    @returns: list[pygame.Surface]
        The list of the flipped images.
    """
    return [pygame.transform.flip(image, True, False) for image in image_list]


def decode_sprite_sheets_x(
    sprite_dir_path: str, scaled_size: tuple[int, int]
) -> dict[str, list[pygame.Surface]]:
    """
    This takes all the sprite sheets in a directory and splits in x direction.

    @param: sprite_dir_path : str
        The path of the directory that contains the sprite sheets.
    @param: scaled_size : tuple[int, int]
        The required size of the images.

    @returns: dict[str, list[pygame.Surface]]
        The name of the sprite sheet mapped to its split images.
    """
    sprite_sheet_data = {
        parse_filename(name): name
        for name in listdir(sprite_dir_path)
        if isfile(join(sprite_dir_path, name))
    }
    all_sprites = {}
    for (name, direction, frame_size), original_name in sprite_sheet_data.items():
        sprite_sheet = pygame.image.load(
            join(sprite_dir_path, original_name)
        ).convert_alpha()
        sprites = []
        for image_index in range(sprite_sheet.get_width() // frame_size[0]):
            rect = pygame.Rect((image_index * frame_size[0], 0), frame_size)
            image = pygame.Surface(frame_size, pygame.SRCALPHA, 32)
            image.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale(image, scaled_size))
        if direction != "N":
            opposite_direction = "R" if direction == "L" else "L"
            all_sprites[f"{name}_{direction}"] = sprites
            all_sprites[f"{name}_{opposite_direction}"] = flip_images_x(sprites)
        else:
            all_sprites[name] = sprites
    return all_sprites


def get_bg_image(
    image_color: Literal["Blue", "Brown", "Gray", "Green", "Pink", "Purple", "Yellow"],
    bg_image_data: dict[str, pygame.Surface],
) -> pygame.Surface:
    """
    This returns a background image of the given color.

    @param: image_color : Literal["Blue", "Brown", "Gray", "Green", "Pink", "Purple", "Yellow"]
        The color of the bg tiles.
    @param: bg_image_data : dict[str, pygame.Surface]
        The color of the image mapped to its image tile.

    @returns: pygame.Surface
        The bg tile of the specified color.
    """
    return bg_image_data[image_color]


def get_bg_pos(
    screen_size: tuple[int, int], bg_image_size: tuple[int, int]
) -> list[tuple[int, int]]:
    """
    This gives all the positions the bg tile need to go to tile the full screen.

    @param: screen_size : tuple[int, int]
        The size of the screen hosting the game.
    @param: bg_image_size : tuple[int, int]
        The size of the bg tile image.

    @returns: list[tuple[int, int]]
        The list of coordinates of the bg tiles to go.
    """
    return [
        (i * bg_image_size[0], j * bg_image_size[1])
        for i in range(ceil(screen_size[0] / bg_image_size[0]))
        for j in range(ceil(screen_size[1] / bg_image_size[1]))
    ]


def draw(
    screen: pygame.Surface, bg_image: pygame.Surface, bg_pos: list[tuple[int, int]]
) -> None:
    BLACK = (0, 0, 0)
    screen.fill(BLACK)
    for pos in bg_pos:
        screen.blit(bg_image, pos)
    pygame.display.update()


def main(screen: pygame.Surface) -> None:
    """
    The main gameloop that executes all the logic of the game.

    @param: screen : pygame.Surface
        The screen that hosts the game.
    """
    screen_size = screen.get_size()

    timer = pygame.time.Clock()
    fps = 60

    BG_IMAGES_PATH = join("Assets", "Background")
    BG_IMAGES = {
        color.removesuffix(".png"): pygame.image.load(
            join(BG_IMAGES_PATH, color)
        ).convert_alpha()
        for color in listdir(BG_IMAGES_PATH)
    }

    # TODO: Make the bg color load according to the level data.
    bg_image = get_bg_image("Blue", BG_IMAGES)
    bg_pos = get_bg_pos(screen_size, bg_image.get_size())

    running = True
    while running:
        timer.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        draw(screen, bg_image, bg_pos)
    pygame.quit()
    exit()


if __name__ == "__main__":
    main(screen)
