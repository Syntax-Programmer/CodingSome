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
    x_vel = 0
    y_vel = 0
    # NOTE: Add a statement in the child class animator that resets this variable if it gets too big.
    animation_count = 0
    on_ground = False
    jump_count = 0
    frame_jumped = 0

    def __init__(
        self,
        character_pos: tuple[int, int],
        character_assets: dict[str, list[pygame.Surface]],
        tag: Literal["Hostile", "Neutral", "Passive"],
        is_killable: bool,
        is_intractable: bool,
        character_heath: int,
        is_directional: bool,
    ) -> None:
        ObjectInit.__init__(
            self,
            character_pos,
            character_assets,
            tag,
            is_killable,
            is_intractable,
            is_directional,
        )
        Mechanics.__init__(self)
        Health.__init__(self, character_heath)

    def set_pos(self, pos_to_set: tuple[int, int]) -> None:
        self.rect.center = pos_to_set

    def move_object(self, fps: int) -> None:
        x_dist = self.calculate_delta_dist(self.x_vel, fps)
        y_dist = self.calculate_delta_dist(self.y_vel, fps)
        self.rect.move_ip(x_dist, y_dist)

    def moving_mechanics(
        self, moving_direction: Literal["R", "L"], moving_vel: float = 0
    ) -> None:
        self.x_vel = moving_vel if moving_direction == "R" else -moving_vel
        if self.direction != "N" and self.direction != moving_direction:
            self.direction = moving_direction
            self.animation_count = 0

    def jumping_mechanics(self, jumping_vel: float = 0) -> None:
        if self.on_ground and not self.jump_count:
            self.y_vel = jumping_vel
            self.jump_count = 1
            self.animation_count = 0
            self.on_ground = False
        elif not self.on_ground and self.jump_count == 1:
            self.y_vel = jumping_vel
            self.jump_count = 2
            self.animation_count = 0

    def apply_gravity(self, gravity: float, fps: int) -> None:
        if not self.on_ground:
            # This frame_jumped is used in the sense that:
            # delta_vel = gravity * delta_time; this delta vel is always constant.
            # delta_vel * frame_jumped is the gradual increase/decrease of the velocity due to acceleration.
            # We can interpret it like delta_time * frame_jumped is the gradual increase of time as time passed
            # increasing the velocity with it.
            # frame_jumped is the number of frames that the character has spend jumping.
            self.frame_jumped += 1
            self.y_vel += self.calculate_delta_vel(gravity, fps) * self.frame_jumped
        elif self.on_ground:
            self.jump_count = 0
            self.animation_count = 0
            self.frame_jumped = 0
