from abc import ABC, abstractmethod

from base.field import Direction, Cell, Colors


class Action(ABC):

    @abstractmethod
    def __str__(self) -> str:
        pass


class NoneAction(Action):
    def __str__(self) -> str:
        return "None"


class MoveAction(Action):

    def __init__(self, direction: Direction):
        self.__direction__ = direction

    @property
    def direction(self) -> Direction:
        return self.__direction__

    def __str__(self) -> str:
        return str(self.__direction__.name)


class BumpWallAction(MoveAction):
    pass


class FallOffAction(Action):
    def __init__(self, direction: Direction):
        self.__direction__ = direction

    @property
    def direction(self) -> Direction:
        return self.__direction__

    def __str__(self) -> str:
        return "FallOf"


class MarkAction(Action):

    def __init__(self, cell: Cell, color: Colors):
        self.__cell__ = cell
        self.__color__ = color

    def __str__(self) -> str:
        return str(self.__color__)
