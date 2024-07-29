"""
This module handles and keeps track of the killable objects.
This handles the damaging, healing, dying(maybe not sure) etc.

__AUTHOR__ = Anand Maurya
"""

"""
As the assets pack have hearts as the manager of health. 
A general advise is to have the health in terms of hearts i.e., multiples of 0.25(for the heart_1.png)
and multiples of 0.33(for the heart_2.png and heart_3.png).
You can still assign a random number of hearts. But the floor state of the hearts will be displayed.
"""


class Health:
    """
    This class manages the health of all the objects it derives.
    This is meant for only those objects who have the is_killable tag as true.

    @attr: is_alive : bool
        The checker if the object is alive or not.
    @attr: health : int
        The health of the object at any given time.
    @attr: health_pool : int
        A reserve and the identifier of how much health the object
        is supposed to have.
    """

    is_alive = True

    def __init__(self, object_health: int) -> None:
        """
        This initializes the Health class.

        @param: object_health : int
            The initial and the max health the object can have.
        """
        # TODO: Add a health assets parameter and make it so that it can be assigned to NONE if no UI is to be displayed.
        self.health = object_health
        self.health_pool = object_health

    def deal_damage(self, damage: int) -> None:
        """
        This deals damage to the object.

        @param: damage : int
            The amount of damage that is to be inflicted to the object.
        """
        self.health -= damage

    def do_healing(self, heal_amount: int) -> None:
        """
        This heals the object.

        @param: heal_amount : int
            The amount of health to be restored.
        """
        # This prevents the object to over heal.
        if heal_amount > self.health_pool:
            heal_amount = self.health_pool
        self.health += heal_amount

    def is_dead(self) -> None:
        """
        This checks if the object is dead ot not.
        """
        if self.health <= 0:
            self.is_alive = False

    def do_respawn(self, respawn_health: int | None = None) -> None:
        """
        This respawns the object by restoring its health.

        @param: respawn_health : int | None
            The health the object restores when respawning.
            If respawn_health is None then the object will restore to full health.
        """
        self.is_alive = True
        if respawn_health is None:
            respawn_health = self.health_pool
        self.health = self.health_pool
