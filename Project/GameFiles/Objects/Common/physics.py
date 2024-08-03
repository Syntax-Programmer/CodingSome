"""
This module has all the physics related functions in the game.

__AUTHOR__ = Anand Maurya
"""


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
