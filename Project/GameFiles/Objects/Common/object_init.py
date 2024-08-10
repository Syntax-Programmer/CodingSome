"""
This module initializes all the objects of the game,
these include the terrain, player and the NPCs.

__AUTHOR__ = Anand Maurya
"""

import pygame

from typing import Literal


class ObjectInit(pygame.sprite.Sprite):
    def __init__(
        self,
        object_pos: tuple[int, int],
        object_assets: dict[str, list[pygame.Surface]] | pygame.Surface,
        behavior: Literal["Hostile", "Neutral", "Passive"],
        is_killable: bool,
        is_intractable: bool,
        is_directional: bool,
    ) -> None:
        super().__init__()
        if isinstance(object_assets, dict):
            self.assets = object_assets
            self.image = list(self.assets.values())[0][0]
        elif isinstance(object_assets, pygame.Surface):
            self.image = object_assets
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = pygame.Rect(object_pos, self.image.get_size())
        self.tag = behavior
        self.is_killable = is_killable
        self.is_intractable = is_intractable
        if is_directional:
            self.direction = "R"
        else:
            self.direction = "N"
