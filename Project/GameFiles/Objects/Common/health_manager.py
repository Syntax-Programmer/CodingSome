"""
This module handles and keeps track of the killable objects.
This handles the damaging, healing, dying(maybe not sure) etc.

__AUTHOR__ = Anand Maurya
"""


class Health:
    is_object_alive = True

    def __init__(self, object_health: int) -> None:
        # TODO: Add a health assets parameter and make it so that it can be assigned to NONE if no UI is to be displayed.
        self.health = self.health_bar = object_health

    def change_health(self, health_change: int) -> None:
        # If health change is positive the object heals.
        # If health change is negative the object loses health.
        if health_change > self.health_bar:
            health_change = self.health_bar
        self.health += health_change

    def increase_max_health(self, new_health_bar: int) -> None:
        self.health_bar = new_health_bar

    def is_object_dead(self) -> None:
        if self.health <= 0:
            self.is_object_alive = False

    def do_respawn(self, respawn_health: int | None = None) -> None:
        self.is_object_alive = True
        if respawn_health is None:
            respawn_health = self.health_bar
        self.health = self.health_bar
