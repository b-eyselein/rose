from abc import ABCMeta
from dataclasses import dataclass
from typing import List

from base.actions import Action, MoveAction, BumpWallAction, FallOffAction
from base.field import Direction
from base.field import Field, Point


@dataclass()
class Movable(metaclass=ABCMeta):
    """Base class for everything that can move on a field"""
    _name: str
    _field: Field
    _initial_position: Point = Point()

    def __post_init__(self):
        self._position = self._initial_position
        self._actions: List[Action] = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def initial_position(self) -> Point:
        return self._initial_position

    @property
    def position(self) -> Point:
        return self._position

    @property
    def actions(self) -> List[Action]:
        return self._actions

    def can_go_up(self) -> bool:
        return self._position.y < self._field.height

    def can_go_down(self) -> bool:
        return self._position.y > 0

    def can_go_left(self) -> bool:
        return self._position.x > 0

    def can_go_right(self) -> bool:
        return self._position.x < self._field.width

    def save_action(self, action: Action):
        self._actions.append(action)

    def _move(self, direction: Direction):
        # Get movement in x and y direction as int in [-1, 0, 1]
        mov_x: int = direction.movement_x()
        mov_y: int = direction.movement_y()

        # If movement is possible within field
        mov_x_okay: bool = 0 <= self.position.x + mov_x < self._field.height
        mov_y_okay: bool = 0 <= self.position.y + mov_y < self._field.height

        action: Action
        if mov_x_okay and mov_y_okay:
            # Update position
            self._position = Point(self.position.x + mov_x, self.position.y + mov_y)
            action = MoveAction(direction)
        elif self._field.has_border:
            # bump into wall if there are any
            action = BumpWallAction(direction)
        else:
            # fall off field if there are no walls
            action = FallOffAction(direction)

        self.save_action(action)

    def go_up(self) -> None:
        self._move(Direction.UP)

    def go_right(self) -> None:
        self._move(Direction.RIGHT)

    def go_down(self) -> None:
        self._move(Direction.DOWN)

    def go_left(self) -> None:
        self._move(Direction.LEFT)
