from abc import ABCMeta
from typing import List

from base.actions import Action, MoveAction, BumpWallAction, FallOffAction
from base.field import Direction
from base.field import Field, Point


class Movable(metaclass=ABCMeta):
    """Base class for everything that can move on a field"""

    def __init__(self, name, field: Field, initial_point: Point = Point()):
        self.__name__ = name
        self.__field__ = field
        self.__initial_position__ = initial_point
        self.__position__ = initial_point
        self.__actions__: List[Action] = []

    @property
    def name(self) -> str:
        return self.__name__

    @property
    def initial_position(self) -> Point:
        return self.__initial_position__

    @property
    def position(self) -> Point:
        return self.__position__

    @property
    def actions(self) -> List[Action]:
        return self.__actions__

    def can_go_up(self) -> bool:
        return self.__position__.y < self.__field__.height

    def can_go_down(self) -> bool:
        return self.__position__.y > 0

    def can_go_left(self) -> bool:
        return self.__position__.x > 0

    def can_go_right(self) -> bool:
        return self.__position__.x < self.__field__.width

    def save_action(self, action: Action):
        self.__actions__.append(action)

    def __move__(self, direction: Direction):
        # Get movement in x and y direction as int in [-1, 0, 1]
        (mov_x, mov_y) = (direction.movement_x(), direction.movement_y())

        # If movement is possible within field
        mov_x_okay = (0 <= self.position.x + mov_x < self.__field__.height)
        mov_y_okay = (0 <= self.position.y + mov_y < self.__field__.height)

        if mov_x_okay and mov_y_okay:  # Update position
            self.__position__ = Point(self.position.x + mov_x, self.position.y + mov_y)
            action = MoveAction(direction)
        elif self.__field__.has_border:  # bump into wall if there are any
            action = BumpWallAction(direction)
        else:  # fall off field if there are no walls
            action = FallOffAction(direction)
        self.save_action(action)

    def go_up(self) -> None:
        self.__move__(Direction.UP)

    def go_right(self) -> None:
        self.__move__(Direction.RIGHT)

    def go_down(self) -> None:
        self.__move__(Direction.DOWN)

    def go_left(self) -> None:
        self.__move__(Direction.LEFT)
