"""
This module is the parent to all the living NPCs and players.
This contains many commonly shared functionalities by these living creatures.

__AUTHOR__ = Anand Maurya
"""

import pygame

from object_init import ObjectInit
from physics import Mechanics
from health_manager import Health
from typing import Literal


class Characters(ObjectInit, Mechanics, Health):
    def __init__(
        self,
        character_pos: tuple[int, int],
        character_assets: dict[str, list[pygame.Surface]],
        tag: Literal["Hostile", "Neutral", "Passive"],
        is_killable: bool,
        is_intractable: bool,
        character_heath: int,
    ) -> None:
        ObjectInit.__init__(
            self, character_pos, character_assets, tag, is_killable, is_intractable
        )
        Mechanics.__init__(self)
        Health.__init__(self, character_heath)

    def set_pos(self, pos_to_set: tuple[int, int]) -> None:
        self.rect.center = pos_to_set
