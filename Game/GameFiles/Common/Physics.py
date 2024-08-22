"""
This module aims to have functions that help in calculation of certain quantities
and determination of some variables.
This module have mechanics, collision like features.
"""

"""
#! ISSUE: This function currently assumes that the main game loop is executed exactly the specified fps
#! amount, this is wrong as we can't confirm that this is always true.
#! 
#! WHY WAS IT IMPLEMENTED: As currently the game is at a small scale, there is no issue in the game loop
#! to run at the specified fps times. It would have been too early to implement that functionality 
#! right now.
#! 
#! FIX: Calculate the amount taken in seconds between the last frame and the frame preceding it to
#! use it as the approximate(pretty good one) delta time.
#! 
#* NOTE: Change the method of implementation of all the references of this function.
"""


def integrate_wrt_time(quantity: int | float, fps: int) -> float:
    """
    This gives the definite integral of the quantity from 0 to delta time.
    """
    delta_time = fps / 1000  # 1000 is the number of ms in 1s.
    # The complete integral simplifies to the return expression for our use case.
    return delta_time * quantity
