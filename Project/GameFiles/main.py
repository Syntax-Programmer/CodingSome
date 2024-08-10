"""
This is the main game entry point of the game.
This handles the gameloop and the initializer functions.

__AUTHOR__ = Anand Maurya
"""

import pygame
import json

from sys import exit, path
from os import listdir
from os.path import join, isfile
from typing import Literal
from math import ceil

path.append("GameFiles\\Objects")
from Objects import Neutral
from Objects import Hostile
from Objects import Passive
from Objects import Common


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


def decode_terrain_image() -> dict[str, pygame.Surface]:
    # This is the terrain name mapped to its rect data.
    terrain_data = {
        "GreenGrass": (96, 0, 48, 48),
        "GreenDirt": (144, 0, 32, 32),
        "BrownGrass": (96, 64, 48, 48),
        "BrownDirt": (144, 64, 32, 32),
        "PinkGrass": (96, 128, 48, 48),
        "PinkDirt": (144, 128, 32, 32),
        "LargeBrick": (272, 128, 48, 48),
        "MediumBrick": (320, 128, 32, 32),
        "CopperMedium": (208, 16, 32, 32),
        "CopperSmall": (192, 16, 16, 16),
        "CopperLong": (192, 0, 48, 16),
        "CopperTall": (240, 0, 16, 48),
        "IronMedium": (208, 80, 32, 32),
        "IronSmall": (192, 80, 16, 16),
        "IronLong": (192, 64, 48, 16),
        "IronTall": (240, 64, 16, 48),
        "OrangeMetalMedium": (208, 144, 32, 32),
        "OrangeMetalSmall": (192, 144, 16, 16),
        "OrangeMetalLong": (192, 128, 48, 16),
        "OrangeMetalTall": (240, 128, 16, 48),
        "GoldMedium": (288, 144, 32, 32),
        "GoldSmall": (272, 144, 16, 16),
        "GoldLong": (272, 128, 48, 16),
        "GoldTall": (320, 128, 16, 48),
        "ThinGold": (272, 0, 48, 8),
        "ThinCopper": (272, 16, 48, 8),
        "ThinIron": (272, 32, 48, 8),
        "RockHorizontal1": (0, 0, 48, 8),
        "RockHorizontal2": (0, 40, 48, 8),
        "RockVertical1": (0, 8, 8, 32),
        "RockVertical2": (40, 8, 8, 32),
        "RockEdgeTopLeft": (58, 8, 8, 8),
        "RockEdgeTopRight": (64, 8, 8, 8),
        "RockEdgeBottomLeft": (58, 16, 8, 8),
        "RockEdgeBottomRight": (64, 16, 8, 8),
        "WoodHorizontal1": (0, 64, 48, 8),
        "WoodHorizontal2": (0, 104, 48, 8),
        "WoodVertical1": (0, 72, 8, 32),
        "WoodVertical2": (40, 72, 8, 32),
        "WoodEdgeTopLeft": (58, 72, 8, 8),
        "WoodEdgeTopRight": (64, 72, 8, 8),
        "WoodEdgeBottomLeft": (58, 80, 8, 8),
        "WoodEdgeBottomRight": (64, 80, 8, 8),
        "CabbageHorizontal1": (0, 128, 48, 8),
        "CabbageHorizontal2": (0, 168, 48, 8),
        "CabbageVertical1": (0, 136, 8, 32),
        "CabbageVertical2": (40, 136, 8, 32),
        "CabbageEdgeTopLeft": (58, 136, 8, 8),
        "CabbageEdgeTopRight": (64, 136, 8, 8),
        "CabbageEdgeBottomLeft": (58, 144, 8, 8),
        "CabbageEdgeBottomRight": (64, 144, 8, 8),
    }
    terrain_sprites = {}
    TERRAIN_IMAGE_PATH = join("Assets", "Terrain", "Terrain.png")
    terrain_image = pygame.image.load(TERRAIN_IMAGE_PATH).convert_alpha()
    for terrain_name, rect_data in terrain_data.items():
        rect = pygame.Rect(rect_data)
        image = pygame.Surface(rect_data[2:], pygame.SRCALPHA, 32)
        image.blit(terrain_image, (0, 0), rect)
        terrain_sprites[terrain_name] = image
    return terrain_sprites


def parse_level_json(level_count: int) -> dict:
    levels_path = join("GameFiles", "Levels", f"level{level_count}.json")
    level_data = {}
    try:
        with open(levels_path) as level_file:
            level_data = json.load(level_file)
    except FileNotFoundError:
        raise FileNotFoundError(
            f"The specified path: {levels_path} to the level json does not exist."
        )
    return level_data


def level_json_data_user(
    level_json_data: dict, terrain_handler: Passive.TerrainHandler
) -> Literal["Blue", "Brown", "Gray", "Green", "Pink", "Purple", "Yellow"]:
    try:
        terrain_handler.add_terrain_blocks(level_json_data["terrains"])
        return level_json_data["bg_color"]
    except KeyError:
        raise KeyError(
            "The level json data is either wrong or does not have the required fields."
        )


def parse_config_json() -> tuple[float, float, float, Neutral.Player]:
    config_file_path = join("GameFiles", "config.json")
    config_data = {}
    try:
        with open(config_file_path) as config_file:
            config_data = json.load(config_file)
    except FileNotFoundError:
        raise FileNotFoundError("The config file is not in the GameFiles directory")
    player_assets_path = join("Assets", "Characters", config_data["player"]["type"])
    player_assets = decode_sprite_sheets_x(
        player_assets_path, config_data["player"]["size"]
    )
    player = Neutral.Player(config_data["player"]["initial_pos"], player_assets)
    return (
        config_data["gravity"],
        config_data["player"]["initial_run_speed"],
        config_data["player"]["initial_jump_speed"],
        player,
    )


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
    terrain_handler: Passive.TerrainHandler,
) -> None:
    BLACK = (0, 0, 0)
    screen.fill(BLACK)
    for pos in bg_pos:
        screen.blit(bg_image, pos)
    terrain_handler.draw(screen)
    player_object.draw(screen)
    pygame.display.update()


def main(screen: pygame.Surface) -> None:
    screen_size = screen.get_size()

    timer = pygame.time.Clock()
    fps = 60
    level_count = 1

    BG_IMAGES_PATH = join("Assets", "Background")
    BG_IMAGES = {
        color.removesuffix(".png"): pygame.image.load(
            join(BG_IMAGES_PATH, color)
        ).convert_alpha()
        for color in listdir(BG_IMAGES_PATH)
    }
    GRAVITY, player_run_speed, player_jump_speed, player = parse_config_json()
    terrain_handler = Passive.TerrainHandler(decode_terrain_image())
    level_json_data = parse_level_json(level_count)
    bg_image_color = level_json_data_user(level_json_data, terrain_handler)
    bg_image = get_bg_image(bg_image_color, BG_IMAGES)
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
                if event.key in [pygame.K_SPACE, pygame.K_UP]:
                    player.jumping(player_jump_speed)
        Neutral.player_handler(
            player, GRAVITY, current_fps, moving_vel=player_run_speed
        )
        Common.check_ground_collision(player, terrain_handler)
        draw(screen, bg_image, bg_pos, player, terrain_handler)
    pygame.quit()
    exit()


if __name__ == "__main__":
    main(screen)
