"""
This module has all the physics related functions in the game.

__AUTHOR__ = Anand Maurya
"""

import pygame


class Mechanics:
    # The methods: calculate_delta_(dist/vel)
    #    calculate the specified values using the fact that:
    #
    #    d
    #    -- distance = velocity.
    #    dt
    #
    #    d
    #    -- velocity = acceleration.
    #    dt
    #

    MILLISECONDS_IN_SECOND = 1000
    delta_time = 0

    def __update_delta_time(self, current_fps: float) -> None:
        # This updates the delta time b/w each frame for accurate calculations.
        self.delta_time = current_fps / self.MILLISECONDS_IN_SECOND

    def calculate_delta_dist(self, vel: float, current_fps: float) -> float:
        self.__update_delta_time(current_fps)
        return vel * self.delta_time

    def calculate_delta_vel(self, acc: float, current_fps: float) -> float:
        self.__update_delta_time(current_fps)
        return acc * self.delta_time


# It is not in the mechanics class because I would have had to initialize this class in the main function.
def check_ground_collision(player_obj, terrain_handler_obj) -> None:
    # As the animation of the player makes it so that the mask of the player is not on the same bottom y level each animation frame.
    # This causes the player to miss the collision even if it should have.
    # This causes the player to register it as falling instead of running causing messed up animation.
    # We add this little offset to account for it to the player's y each iteration.
    # We immediately reverse this change before the next iteration to allow the original player's y level being drawn.
    # NOTE: We don't reverse the addition of the offset if collision is detected as the 'player_obj.rect.bottom = terrain_block.rect.top'
    # accounts for the reversal of the offset and also to place the player correctly on the top of the terrain rect.
    PLAYER_Y_OFFSET = 7  # This value is precisely 6.5 but we take 7 for good luck.
    for terrain_block in terrain_handler_obj.terrain_group:
        player_obj.rect.y += PLAYER_Y_OFFSET
        if pygame.sprite.collide_mask(player_obj, terrain_block):
            player_obj.on_ground = True
            # As the player_handler function is executed before this one. Each iteration the player is moving the player gains 1 frame count.
            # This makes the player animator function think that the player is jumping while it is not.
            # This makes the animation of the player always to jumping one.
            player_obj.frame_jumped = 0
            player_obj.rect.bottom = terrain_block.rect.top
            break
        player_obj.rect.y -= PLAYER_Y_OFFSET
    else:
        player_obj.on_ground = False
