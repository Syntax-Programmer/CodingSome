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
    """
    This is the fully complete player object that has all the methods the player can have.
    """

    ANIMATION_DELAY = 4

    def __init__(
        self,
        player_pos: tuple[int, int],
        player_assets: dict[str, list[pygame.Surface]],
    ) -> None:
        tag = "Neutral"
        is_killable = True
        is_intractable = True
        is_directional = True
        character_heath = 100
        is_double_jumpable = True
        super().__init__(
            player_pos,
            player_assets,
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
        try:
            sprites = self.assets[f"{action}_{self.direction}"]
        except KeyError:
            raise ValueError("Invalid/Incomplete asset set provided.")
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count += 1


# Here the moving vel is defaulted to zero to account for the time the player should move but can't because of some constraints.
def player_handler(
    player_object: Player,
    gravity: float,
    current_fps: float,
    health_change: int = 0,
    moving_vel: float = 0,
) -> None:
    # This handles the basic functionalities of the player.

    # TODO: Must be expanded on to incorporate all the functions, collisions and other stuff.
    # Reset the x_vel so that if the player does not press the key then it does not move.
    player_object.x_vel = 0
    key = pygame.key.get_pressed()
    if key[pygame.K_a] or key[pygame.K_LEFT]:
        player_object.running("L", moving_vel)
    if key[pygame.K_d] or key[pygame.K_RIGHT]:
        player_object.running("R", moving_vel)
    # The jump function is used in the main gameloop rather than here to make the jumping mechanics more natural.
    player_object.change_health(health_change)
    player_object.move_character(current_fps)
    player_object.apply_gravity(gravity, current_fps)
    player_object.animator()
    player_object.is_object_dead()
