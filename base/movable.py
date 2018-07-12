from abc import ABCMeta
from typing import List

from base.actions import *
from base.field import Direction
from base.field import Field, Vector2D


class Movable(metaclass=ABCMeta):
    """Base class for everything that can move on a field"""

    def __init__(self, name: str, field: Field, initial_point: Vector2D = Vector2D()):
        self.__name: str = name
        self.__field: Field = field
        self.__initial_position: Vector2D = initial_point
        self.__position: Vector2D = initial_point
        self.__actions: List[Action] = []

    @property
    def name(self) -> str:
        return self.__name

    @property
    def initial_position(self) -> Vector2D:
        return self.__initial_position

    @property
    def position(self) -> Vector2D:
        return self.__position

    @property
    def actions(self) -> List[Action]:
        return self.__actions

    def can_go_up(self) -> bool:
        return self.__position.x < self.__field.height

    def can_go_down(self) -> bool:
        return self.__position.x > 0

    def can_go_left(self) -> bool:
        return self.__position.y > 0

    def can_go_right(self) -> bool:
        return self.__position.x < self.__field.width

    def save_action(self, action: Action):
        self.__actions.append(action)

    def __move(self, direction: Direction):
        # Get movement in x and y direction as int in [-1, 0, 1]
        (mov_x, mov_y) = (direction.movement_x(), direction.movement_y())

        # If movement is possible within field
        mov_x_okay = (0 <= self.position.x + mov_x < self.__field.height)
        mov_y_okay = (0 <= self.position.y + mov_y < self.__field.height)

        if mov_x_okay and mov_y_okay:  # Update position
            self.__position = Vector2D(self.position.x + mov_x, self.position.y + mov_y)
            action = MoveAction(direction)
        elif self.__field.has_border:  # bump into wall if there are any
            action = BumpWallAction(direction)
        else:  # fall off field if there are no walls
            action = FallOffAction(direction)
        self.save_action(action)

    def go_up(self) -> None:
        self.__move(Direction.UP)

    def go_right(self) -> None:
        self.__move(Direction.RIGHT)

    def go_down(self) -> None:
        self.__move(Direction.DOWN)

    def go_left(self) -> None:
        self.__move(Direction.LEFT)
