"""
This module initializes all the objects of the game,
these include the terrain, player and the NPCs.

__AUTHOR__ = Anand Maurya
"""

import pygame

from typing import Literal


class ObjectInit(pygame.sprite.Sprite):
    """
    This class is the parent class of all the objects in the game.
    This initializes all of the basic components of all the objects.

    @attr: assets : dict[str, list[pygame.Surface]]
        The variable that holds all the assets if the object has many.
    @attr: image : pygame.Surface
        The image of the object at any given frame.
    @attr: rect : pygame.Rect
        The rect of the object defining its hitbox.
    @attr: mask : pygame.mask
        The mask of the object image at any given frame.
    @attr: tag : Literal["Hostile", "Neutral", "Passive"]
        This tells what type of object inherits from this class.
    @attr: is_killable : bool
        This tells if the object is killable or not.
    @attr: is_intractable : bool
        This tells if the object can be interacted with.
    @attr: direction : Literal["R", "L", "N]
        Tells the current way the object is facing.
    """

    def __init__(
        self,
        object_pos: tuple[int, int],
        object_assets: dict[str, list[pygame.Surface]] | pygame.Surface,
        tag: Literal["Hostile", "Neutral", "Passive"],
        is_killable: bool,
        is_intractable: bool,
        is_directional: bool,
    ) -> None:
        """
        This initializes the object based on its pos and its assets.

        @param: object_pos : tuple[int, int]
            The initial pos of the object.
        @param: object_assets : dict[str, list[Surface]] | Surface
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
        """
        super().__init__()
        if isinstance(object_assets, dict):
            self.assets = object_assets
            self.image = list(self.assets.values())[0][0]
        elif isinstance(object_assets, pygame.Surface):
            self.image = object_assets
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = pygame.Rect(object_pos, self.image.get_size())
        self.tag = tag
        self.is_killable = is_killable
        self.is_intractable = is_intractable
        if is_directional:
            self.direction = "R"
        else:
            self.direction = "N"
