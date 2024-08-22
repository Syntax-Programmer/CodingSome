"""
This module aims to make a common class that provides basic functionalities 
to all the game objects.
This tells about the type the object is either Living or Non-Living,
either Hostile or Neutral or Passive, either is killable or is intractable etc.

This class initializes the rect, image and assets and these tags mentioned above.
These help the object type to be identified and have its assets ready to be used.
"""

import pygame

from typing import Literal


class Object(pygame.sprite.Sprite):
    def __init__(
        self,
        object_pos: tuple[int, int],
        object_assets: dict[str, list[pygame.Surface]] | pygame.Surface,
        object_behavior: Literal["H", "N", "P"],
        is_killable: bool,
        is_intractable: bool,
    ) -> None:
        super().__init__()
        self.is_killable, self.is_intractable, self.behavior = (
            is_killable,
            is_intractable,
            object_behavior,
        )
        if isinstance(object_assets, pygame.Surface):
            self.image = object_assets
        elif isinstance(object_assets, dict):
            self.assets = object_assets
            self.image = list(self.assets.values())[0][0]
        self.mask = pygame.mask.from_surface(self.image)
        #! We need to keep consistency of having all the assets have the same size.
        self.rect = pygame.Rect(object_pos, self.image.get_size())
