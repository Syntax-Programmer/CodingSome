"""
This module is the parent to all the living NPCs and players.
This contains many commonly shared functionalities by these living creatures.

__AUTHOR__ = Anand Maurya
"""

import pygame

from sys import path
from os.path import join

COMMON_PATH = join("GameFiles", "Objects", "Common")
path.append(COMMON_PATH)
from object_init import ObjectInit
from physics import Mechanics
from health_manager import Health
from typing import Literal


class Characters(ObjectInit, Mechanics, Health):
    """
    This is the parent class to all the living beings in this game.

    @attr: x_vel : float
        The velocity of the character in the x direction.
    @attr: y_vel : float
        The velocity of the character in the y direction.
    @attr: animation_count : int
        The number of frames that the current animation has been going for.
    @attr: on_ground : bool
        The identifier that if the character is on the ground or not.
    @attr: jump_count : int
        The identifier that what type of jump the character is currently doing.
    @attr: frame_jumped : int
        The number of frames the character has spent during jumping.
    @attr: is_double_jumpable : bool
        The identifier to check if the character can double jump or not.
    """

    x_vel = 0
    y_vel = 0
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
        is_directional: bool,
        is_double_jumpable: bool,
        character_heath: int,
    ) -> None:
        """
        This initializes the Character class.

        @param: character_pos : tuple[int, int]
            The initial pos of the object.
        @param: character_assets : dict[str, list[Surface]] | Surface
            The assets of the object. This can either be an image or sprite sheets.
        @param: tag : Literal["Hostile", "Neutral", "Passive"]
            This tells what type of object is child class.
        @param: is_killable : bool
            This tells if the child class is killable or not.
            This extends to if the object can be mined etc.
        @param: is_intractable : bool
            This tells if the object can be interacted with by other objects.
        @param: is_directional : bool
            Tells if the object changes can face different ways.
        @param: is_double_jumpable : bool
            The identifier to check if the character can double jump or not.
        @param: character_health : int
            The initial and the max health the object can have.
        """
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
        self.is_double_jumpable = is_double_jumpable

    def set_pos(self, pos_to_set: tuple[int, int]) -> None:
        """
        This sets the pos of the character to specified pos.

        @pos_to_set : tuple[int, int]
            The position of the character to set.
        """
        self.rect.center = pos_to_set

    def move_object(self, fps: int) -> None:
        """
        This moves the character according to its velocities.

        @param: fps : int
            The current fps of the game.
        """
        x_dist = self.calculate_delta_dist(self.x_vel, fps)
        y_dist = self.calculate_delta_dist(self.y_vel, fps)
        self.rect.move_ip(x_dist, y_dist)

    def moving_mechanics(
        self, moving_direction: Literal["R", "L"], moving_vel: float = 0
    ) -> None:
        """
        This sets the velocity to the character for it to move in the x direction.

        @param: moving_direction : Literal["R", "L"]
            The direction the character is moving towards.
        @param: moving_vel : float
            The velocity with which the character runs.
        """
        self.x_vel = moving_vel if moving_direction == "R" else -moving_vel
        if self.direction != "N" and self.direction != moving_direction:
            self.direction = moving_direction
            self.animation_count = 0

    def jumping_mechanics(self, jumping_vel: float = 0) -> None:
        """
        This sets the velocity to the character for it to jump.

        @param: jumping_vel : float
            The velocity with which the character is jumping.
        """
        if self.on_ground and not self.jump_count:
            self.y_vel = jumping_vel
            self.jump_count = 1
            self.animation_count = 0
            self.on_ground = False
        elif not self.on_ground and self.jump_count == 1 and self.is_double_jumpable:
            self.y_vel = jumping_vel
            self.jump_count = 2
            self.animation_count = 0

    def apply_gravity(self, gravity: float, fps: int) -> None:
        """
        This applies gravity to the character.

        @param: gravity : float
            The acceleration due to gravity of the world.
        @param: fps : int
            The current fps of the game.
        """
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
            self.y_vel = 0
            
    def draw(self, screen: pygame.Surface) -> None:
        """
        This draws the character on the screen.

        @param: screen : pygame.Surface
            The screen that hosts the game.
        """
        screen.blit(self.image, self.rect.topleft)

