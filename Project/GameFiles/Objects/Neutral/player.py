"""
This modules has methods to handle and define player methods.

__AUTHOR__ = Anand Maurya
"""

import pygame

from sys import path
from os.path import join

COMMON_PATH = join("GameFiles", "Objects")
path.append(COMMON_PATH)
from Common import Characters


class Player(Characters):
    ANIMATION_DELAY = 4

    def __init__(
        self,
        character_pos: tuple[int, int],
        character_assets: dict[str, list[pygame.Surface]],
    ) -> None:
        tag = "Neutral"
        is_killable = True
        is_intractable = True
        is_directional = True
        character_heath = 100
        is_double_jumpable = True
        super().__init__(
            character_pos,
            character_assets,
            tag,
            is_killable,
            is_intractable,
            is_directional,
            is_double_jumpable,
            character_heath,
        )

    def animator(self) -> None:
        action = "Idle"
        # TODO: Add actions for hit and wall hit.
        if self.y_vel < 0:
            if self.jump_count == 1:
                action = "Jump"
            elif self.jump_count == 2:
                action = "DoubleJump"
        elif self.y_vel > 0:
            action = "Fall"
        elif self.x_vel != 0:
            action = "Run"
        sprites = self.assets[f"{action}_{self.direction}"]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count += 1


def player_handler(
    player_object: Player, gravity: float, fps: int, health_difference: int = 0
) -> None:
    # TODO: Must be expanded on to incorporate all the functions, collisions and other stuff.
    player_object.x_vel = 0
    key = pygame.key.get_pressed()
    if key[pygame.K_a] or key[pygame.K_LEFT]:
        pass
    if key[pygame.K_d] or key[pygame.K_RIGHT]:
        pass
    # The jump function is used in the main gameloop rather than here to make the jumping mechanics more natural.
    if health_difference > 0:
        player_object.do_healing(health_difference)
    elif health_difference < 0:
        player_object.deal_damage(health_difference)
    player_object.move_object(fps)
    player_object.apply_gravity(gravity, fps)
    player_object.animator()
