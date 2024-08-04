"""
This module handles everything about the terrain of the game.

__AUTHOR__ = Anand Maurya
"""

import pygame

from sys import path
from os.path import join
from typing import Literal

COMMON_PATH = join("GameFiles", "Objects")
path.append(COMMON_PATH)
from Common import ObjectInit


class TerrainBlock(ObjectInit):
    def __init__(
        self,
        block_pos: tuple[int, int],
        block_assets: pygame.Surface,
    ) -> None:
        behavior = "Passive"
        # NOTE: By making the is_killable tag False we are hardcoding that no INDIVIDUAL terrain block could be broken ever.
        # Only the whole screen can be emptied at once.
        is_killable = is_intractable = is_directional = False
        super().__init__(
            block_pos,
            block_assets,
            behavior,
            is_killable,
            is_intractable,
            is_directional,
        )


class TerrainHandler:

    terrain_group = pygame.sprite.Group()

    def __init__(self, terrain_assets: dict[str, pygame.Surface]) -> None:
        self.terrain_assets = terrain_assets

    def add_terrain_blocks(
        self, level_terrain_data: dict[Literal["type", "pos"], str | list[int]]
    ) -> None:
        # In param level_terrain_data: example: [{'type': 'type1', 'pos': [5, 2]}]
        for block_dict in level_terrain_data:
            # Couldn't figure the type hint for this var so we gonna avoid errors.
            # Example are given for reference.
            terrain_block = TerrainBlock(
                block_dict["pos"],  # type:ignore
                self.terrain_assets[block_dict["type"]],  # type:ignore
            )
            self.terrain_group.add(terrain_block)

    def clear_terrain_blocks(self) -> None:
        self.terrain_group.empty()

    def draw(self, screen: pygame.Surface) -> None:
        self.terrain_group.draw(screen)
