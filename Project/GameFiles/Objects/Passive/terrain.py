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


class __TerrainBlock(ObjectInit):
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

    def add_terrain_blocks(self) -> None:
        # TODO: Implement it.
        pass

    def clear_terrain_blocks(self) -> None:
        self.terrain_group.empty()

    def draw(self, screen: pygame.Surface) -> None:
        self.terrain_group.draw(screen)
