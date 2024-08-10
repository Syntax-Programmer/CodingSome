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
from Common import check_ground_collision


class Player(Characters):
    ANIMATION_DELAY = 4

    def __init__(
        self,
        player_pos: tuple[int, int],
        player_assets: dict[str, list[pygame.Surface]],
    ) -> None:
        tag = "Neutral"
        is_intractable = is_directional = is_double_jumpable = True
        character_heath = 100
        super().__init__(
            player_pos,
            player_assets,
            tag,
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


class PlayerHandler:
    def __init__(self, player_pos: tuple[int, int], player_assets) -> None:
        self.player_group = pygame.sprite.Group()
        self.player_object = Player(player_pos, player_assets)
        self.player_group.add(self.player_object)

    # Here the moving_vel is defaulted to zero to account for the time the player should move but can't because of some constraints.
    def player_attribute_handler(
        self,
        gravity: float,
        terrain_handler_obj,
        current_fps: float,
        health_change: int = 0,
        moving_vel: float = 0,
    ) -> None:
        # This handles the basic functionalities of the player.
        # TODO: Must be expanded on to incorporate all the functions, collisions and other stuff.
        # Reset the x_vel so that if the player does not press the key then it does not move.
        self.player_object.x_vel = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            self.player_object.running("L", moving_vel)
        elif key[pygame.K_d] or key[pygame.K_RIGHT]:
            self.player_object.running("R", moving_vel)
        # The jump function is used in the main gameloop rather than here to make the jumping mechanics more natural.
        # NOTE: The damage of/ heal of the player shall be very small as this function is executed each frame making
        # high damage too quick to kill the player.
        self.player_object.change_health(health_change)
        self.player_object.move_character(current_fps)
        check_ground_collision(self.player_object, terrain_handler_obj)
        self.player_object.apply_gravity(gravity, current_fps)
        self.player_object.animator()
        self.player_object.is_object_dead()

    def trigger_jump_event(self, player_jump_speed: float) -> None:
        self.player_object.jumping(player_jump_speed)
