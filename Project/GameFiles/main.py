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

path.append("GameFiles\\Objects")
from Objects import Neutral


pygame.init()


screen = pygame.display.set_caption("Platformer Game")
SCREEN_SIZE = 1500, 800
screen = pygame.display.set_mode(SCREEN_SIZE)


def parse_image_filename(
    filename: str,
) -> tuple[str, Literal["R", "L", "N"], tuple[int, int]]:
    # This is so we can have all the data we need right on our hands when decoding sprite sheets.
    # This helps us save time on getting all the data we need.
    filename = filename.removesuffix(".png")
    filename = filename.strip(" ")
    data_parts = filename.split(" ", 2)
    if (
        len(data_parts) != 3
        or data_parts[1] not in ["R", "L", "N"]
        or data_parts[2][0] != "("
        or data_parts[2][-1] != ")"
    ):
        raise ValueError(
            f"The data in the filename should be in the format \
                (image_name image_direction(Literal['R', 'L', 'N']) (image_size))\
                    not of {filename}."
        )
    name, direction, size = data_parts
    size = size[1:-1]
    size = size.split("x")
    if len(size) != 2:
        raise ValueError("The size field in the filename must have 2 entries.")
    try:
        size = tuple(map(int, size))
    except ValueError:
        raise ValueError(
            "The entries in the size field of the filename must be integers."
        )
    return name, direction, size  # type: ignore


def flip_images_x(image_list: list[pygame.Surface]) -> list[pygame.Surface]:
    return [pygame.transform.flip(image, True, False) for image in image_list]


def decode_sprite_sheets_x(
    sprite_sheets_dir_path: str, scaling_size: tuple[int, int]
) -> dict[str, list[pygame.Surface]]:
    sprite_sheet_data = {
        parse_image_filename(name): name
        for name in listdir(sprite_sheets_dir_path)
        if isfile(join(sprite_sheets_dir_path, name))
    }
    all_sprites = {}
    for (name, direction, frame_size), original_name in sprite_sheet_data.items():
        sprite_sheet = pygame.image.load(
            join(sprite_sheets_dir_path, original_name)
        ).convert_alpha()
        sprites = []
        for image_index in range(sprite_sheet.get_width() // frame_size[0]):
            rect = pygame.Rect((image_index * frame_size[0], 0), frame_size)
            image = pygame.Surface(frame_size, pygame.SRCALPHA, 32)
            image.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale(image, scaling_size))
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
    return bg_image_data[image_color]


def get_bg_tile_pos(
    screen_size: tuple[int, int], bg_image_size: tuple[int, int]
) -> list[tuple[int, int]]:
    # This gives all the pos the bg tile need to be placed to tile the screen. Just in case you don't get english.
    return [
        (i * bg_image_size[0], j * bg_image_size[1])
        for i in range(ceil(screen_size[0] / bg_image_size[0]))
        for j in range(ceil(screen_size[1] / bg_image_size[1]))
    ]


def draw(
    screen: pygame.Surface,
    bg_image: pygame.Surface,
    bg_pos: list[tuple[int, int]],
    player_object: Neutral.Player,
) -> None:
    BLACK = (0, 0, 0)
    screen.fill(BLACK)
    for pos in bg_pos:
        screen.blit(bg_image, pos)
    player_object.draw(screen)
    pygame.display.update()


def main(screen: pygame.Surface) -> None:
    GRAVITY = 9.8

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
    #! CHANGE THIS TO DYNAMICALLY LOAD AND DETERMINE VALUES.
    #! THIS IS FOR TESTING PURPOSES ONLY.
    #! THIS CODE WORKS FLAWLESSLY.
    player = Neutral.Player(
        (300, 300), decode_sprite_sheets_x("Assets\\Characters\\VirtualGuy", (48, 48))
    )
    # TODO: Make the bg color load according to the level data.
    bg_image = get_bg_image("Blue", BG_IMAGES)
    bg_pos = get_bg_tile_pos(screen_size, bg_image.get_size())

    running = True
    while running:
        timer.tick(fps)
        current_fps = timer.get_fps()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                #! CHANGE THIS TO DYNAMICALLY LOAD AND DETERMINE VALUES.
                #! THIS IS FOR TESTING PURPOSES ONLY.
                #! THIS CODE WORKS FLAWLESSLY.
                if event.key == pygame.K_SPACE:
                    player.jumping(-100)
        draw(screen, bg_image, bg_pos, player)
        #! CHANGE THIS TO DYNAMICALLY LOAD AND DETERMINE VALUES.
        #! THIS IS FOR TESTING PURPOSES ONLY.
        #! THIS CODE WORKS FLAWLESSLY.
        Neutral.player_handler(player, GRAVITY, current_fps, moving_vel=70)
    pygame.quit()
    exit()


if __name__ == "__main__":
    main(screen)
