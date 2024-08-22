"""
This module has most of the things the player must need and a handler class
that handles the player of the game.
"""

import pygame

from sys import path
from os.path import join

COMMON_PATH = join("GameFiles")
path.append(COMMON_PATH)
from Common import Character


class Player(Character):
    ANIMATION_DELAY = 5

    def __init__(
        self,
        player_pos: tuple[int, int],
        player_assets: dict[str, list[pygame.Surface]],
    ) -> None:
        is_respawnable = is_directional = True
        health = 100
        behavior = "N"
        super().__init__(
            is_respawnable, behavior, player_pos, player_assets, health, is_directional
        )

    def animator(self) -> None:
        raise NotImplementedError("Implement this function.")


class PlayerHandler:
    def __init__(
        self,
        player_pos: tuple[int, int],
        player_assets: dict[str, list[pygame.Surface]],
    ) -> None:
        self.player_object = Player(player_pos, player_assets)
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self.player_object)

    def draw(self, screen: pygame.Surface) -> None:
        self.player_group.draw(screen)

    def attribute_handler(self, vel: int, fps: int, health_change: int = 0) -> None:
        self.player_object.x_vel = self.player_object.y_vel = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_w] or key[pygame.K_UP]:
            self.player_object.running(vel, "U")
        if key[pygame.K_s] or key[pygame.K_DOWN]:
            self.player_object.running(vel, "D")
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            self.player_object.running(vel, "L")
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            self.player_object.running(vel, "R")
        self.player_object.move(fps)
        self.player_object.change_health(health_change)
        self.player_object.is_dead()
