from abc import ABC, abstractmethod

from field import Direction


class Action(ABC):

    @abstractmethod
    def __str__(self) -> str:
        pass


class NoneAction(Action):

    def __str__(self) -> str:
        return "None"


class MoveAction(Action):

    def __init__(self, direction: Direction):
        self.__direction = direction

    @property
    def direction(self) -> Direction:
        return self.__direction

    def __str__(self) -> str:
        return str(self.__direction.name)


class BumpWallAction(MoveAction):
    pass


class FallOffAction(Action):
    def __init__(self, direction: Direction):
        self.__direction = direction

    @property
    def direction(self) -> Direction:
        return self.__direction

    def __str__(self) -> str:
        return "FallOf"
