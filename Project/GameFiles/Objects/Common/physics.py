"""
This handles the physics of the game.
This has all the physics related functions that help other things work.

__AUTHOR__ = Anand Maurya
"""

from typing import Literal


"""
We assume that no object can accelerate ever.

If anyone wishes to change that you can do so by making a
function that takes the acceleration and calculate the delta
vel the same way as the calculate_delta_dist function and return acc * delta time.
Same can be done for if the object can experience jerk(variable acceleration).
"""


def calculate_delta_dist(vel: tuple[float, float], fps: int) -> tuple[float, float]:
    """
    This calculates the distance that object need to travel with the given vel.

    @param: vel : tuple[float, float]
        The (x_vel, y_vel) of the object.
    @param: fps : int
        The current framerate of the game.

    @returns: tuple[float, float]
        The (x_dist, y_dist) of the object.
    """
    # Here the final result comes from the definite integral of the velocity
    # from 0(considering the last frame's velocity as initial velocity) to delta time
    # with respect to time.
    delta_time = fps / 1000
    # This returns the ∆x of the player.
    return vel[0] * delta_time, vel[1] * delta_time


def set_move_speeds(
    direction: Literal["R", "L", "U", "D", "NULL"], move_vel: float = 5
) -> tuple[float, float]:
    """
    This sets the speed for moving in the given direction.

    @param: direction : Literal["R", "L", "U", "D", "NULL"]
        1. R : Object is moving right.
        2. L : Object is moving left.
        3. U : Object is moving up.
        4. D : Object is moving down.
        5. NULL : Object is moving nowhere.
    @param: move_vel : float
        The velocity with which the object moves.

    @returns: tuple[float, float]
        The (x_vel, y_vel) of the object.
    """
    vel = (0, 0)
    direction_const = 1 if direction in ["R", "D"] else -1
    if direction in ["R", "L"]:
        vel = move_vel * direction_const, 0
    elif direction in ["U", "D"]:
        vel = 0, move_vel * direction_const
    # If we get any garbage direction, it will be considered as NULL.
    return vel
