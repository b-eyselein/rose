from abc import ABC, abstractmethod
from dataclasses import dataclass

from base.field import Direction, Cell, Colors


class Action(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass


class NoneAction(Action):
    def __str__(self) -> str:
        return "None"


@dataclass()
class MoveAction(Action):
    _direction: Direction

    @property
    def direction(self) -> Direction:
        return self._direction

    def __str__(self) -> str:
        return str(self._direction.name)


class BumpWallAction(MoveAction):
    pass


@dataclass()
class FallOffAction(Action):
    _direction: Direction

    @property
    def direction(self) -> Direction:
        return self._direction

    def __str__(self) -> str:
        return "FallOf"


@dataclass()
class MarkAction(Action):
    _cell: Cell
    _color: Colors

    def __str__(self) -> str:
        return str(self._color)
