"""
This is the player script of the game.
This contains the player class and a handler function
that uses the player class and implements it as intended.

__AUTHOR__ = Anand Maurya
"""

import pygame

from sys import path
from os.path import join
from pygame import Surface

path.append(join("GameFiles", "Objects"))
from Common import ObjectInit, calculate_delta_dist, set_move_speeds


class Player(ObjectInit):
    vel = (0.0, 0.0)

    def __init__(
        self,
        player_pos: tuple[int, int],
        player_assets: dict[str, list[Surface]],
    ) -> None:
        # * The player is not intractable for now. This can be changed later for reasons.
        super().__init__(player_pos, player_assets, "Neutral", True, False)

    def set_pos(self, pos: tuple[int, int]) -> None:
        self.rect.center = pos

    def move(self, fps: int) -> None:
        # TODO: Normalize to movement vector for the diagonal speed to be the same as the
        # TODO: horizontal and vertical speed.
        dist = calculate_delta_dist(self.vel, fps)
        self.rect.move_ip(dist)

    def animator(self) -> None:
        # TODO: implement the animation when you get the appropriate assets.
        pass


def player_handler(player: Player, fps: int, move_vel: float = 5) -> None:
    direction = "NULL"
    key = pygame.key.get_pressed()
    if key[pygame.K_w] or key[pygame.K_UP]:
        direction = "U"
    if key[pygame.K_s] or key[pygame.K_DOWN]:
        direction = "D"
    if key[pygame.K_a] or key[pygame.K_LEFT]:
        direction = "L"
    if key[pygame.K_d] or key[pygame.K_RIGHT]:
        direction = "R"
    player.vel = set_move_speeds(direction, move_vel)
    player.move(fps)
