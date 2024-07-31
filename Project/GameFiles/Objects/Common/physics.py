"""
This module has all the physics related functions in the game.

__AUTHOR__ = Anand Maurya
"""


class Mechanics:
    """
    This class handles the mechanics(physics one) of the game.
    This may be used in combination to get the desired results.

    @attr: MILLISECONDS_IN_SECOND : int
        The number of milliseconds in one second.
    @attr: delta_time : float
        The time between each successive frame.

    The methods: calculate_delta_(dist/vel)
        calculate the specified values using the fact that:

        d
        -- distance = velocity.
        dt

        d
        -- velocity = acceleration.
        dt
    """

    MILLISECONDS_IN_SECOND = 1000
    delta_time = 0

    def __update_delta_time(self, fps: int) -> None:
        """
        This updates the delta time as the game goes on.
        This helps in consistent calculations even if the user is getting unstable framerate.

        @param: fps : int
            The CURRENT FPS of the game.
        """
        self.delta_time = fps / self.MILLISECONDS_IN_SECOND

    def calculate_delta_dist(self, vel: float, fps: int) -> float:
        """
        This calculates the delta distance a body of a given vel travels.

        @param: vel : float
            The current velocity of the object.
        @param: fps : int
            The CURRENT FPS of the game.
        """
        self.__update_delta_time(fps)
        return vel * self.delta_time

    def calculate_delta_vel(self, acc: float, fps: int) -> float:
        """
        This calculates the delta velocity a body of a given acceleration will have.

        @param: acc : float
            The current acceleration of the object.
        @param: fps : int
            The CURRENT FPS of the game.
        """
        self.__update_delta_time(fps)
        return acc * self.delta_time
