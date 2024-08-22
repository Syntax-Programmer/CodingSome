"""
This module aims to make a common class that provides basic functionalities 
to all the living and killable objects in the game.
"""

import pygame

from sys import path
from os.path import join
from typing import Literal

COMMON_PATH = join("GameFiles", "Common")
path.append(COMMON_PATH)
from HealthManager import Health
from Objects import Object
from Physics import integrate_wrt_time


class Character(Health, Object):
    x_vel = y_vel = animation_count = 0

    def __init__(
        self,
        is_respawnable: bool,
        character_behavior: Literal["H", "N", "P"],
        character_pos: tuple[int, int],
        character_assets: dict[str, list[pygame.Surface]],
        character_health: int,
        is_directional: bool,
    ) -> None:
        #! These attributes may need some tweaking with specific use case.
        is_intractable, is_killable = True, True
        Object.__init__(
            self,
            character_pos,
            character_assets,
            character_behavior,
            is_killable,
            is_intractable,
        )
        Health.__init__(self, character_health, is_respawnable)
        if is_directional:
            self.direction = "R"
        else:
            self.direction = "N"

    def set_pos(self, pos: tuple[int, int]) -> None:
        self.rect.center = pos

    def move(self, fps: int) -> None:
        x_dist = integrate_wrt_time(self.x_vel, fps)
        y_dist = integrate_wrt_time(self.y_vel, fps)
        self.rect.move_ip(x_dist, y_dist)

    def running(self, vel: int | float, direction: Literal["R", "L", "U", "D"]) -> None:
        direction_const = 1 if direction in ["R", "D"] else -1
        if direction in ["R", "L"]:
            self.x_vel = vel * direction_const
        elif direction in ["U", "D"]:
            self.y_vel = vel * direction_const
        if self.direction not in ["N", direction]:
            self.direction = direction
            self.animation_count = 0
