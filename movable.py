from enum import Enum

from field import Field, Point

from abc import ABC, abstractmethod


class Direction(Enum):
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4

    def movement_x(self) -> int:
        if self == Direction.UP:
            return 1
        elif self == Direction.DOWN:
            return -1
        else:
            return 0

    def movement_y(self) -> int:
        if self == Direction.RIGHT:
            return 1
        elif self == Direction.LEFT:
            return -1
        else:
            return 0


# Actions

class Action(ABC):

    @abstractmethod
    def printable(self) -> str:
        pass


class NoneAction(Action):

    def printable(self) -> str:
        return "None"


class MoveAction(Action):

    def __init__(self, direction: Direction):
        self.__direction = direction

    @property
    def direction(self) -> Direction:
        return self.__direction

    def printable(self) -> str:
        return str(self.__direction)


class BumpWallAction(MoveAction):
    pass


class FallOffAction(Action):
    def __init__(self, direction: Direction):
        self.__direction = direction

    @property
    def direction(self) -> Direction:
        return self.__direction

    def printable(self) -> str:
        return "Falling off..."


class Movable(ABC):
    """Base class for everything that can move on a field"""

    def __init__(self, name, field: Field, initial_point: Point = Point()):
        self.__name = name
        self.__field = field
        self.__position = initial_point

    @property
    def name(self) -> str:
        return self.__name

    @property
    def position(self) -> Point:
        return self.__position

    def can_go_up(self) -> bool:
        return self.__position.x < self.__field.height

    def can_go_down(self) -> bool:
        return self.__position.x > 0

    def can_go_left(self) -> bool:
        return self.__position.y > 0

    def can_go_right(self) -> bool:
        return self.__position.x < self.__field.width

    @abstractmethod
    def save_action(self, action: Action):
        raise NotImplementedError

    def __move(self, direction: Direction):
        # Get movement in x and y direction as int in [-1, 0, 1]
        (mov_x, mov_y) = (direction.movement_x(), direction.movement_y())
        print("Moving from {} into direction {} with mov {}, {}".format(self.position, direction, mov_x, mov_y))

        # If movement is possible within field
        mov_x_okay = (0 <= self.position.x + mov_x < self.__field.height)
        mov_y_okay = (0 <= self.position.y + mov_y < self.__field.height)

        print("{} and {}".format(mov_x_okay, mov_y_okay))

        if mov_x_okay and mov_y_okay:
            # Update position
            self.__position = Point(self.position.x + mov_x, self.position.y + mov_y)
        elif self.__field.has_border:
            # bump into wall if there are any
            self.save_action(BumpWallAction(direction))
        else:
            # fall off field if there are no walls
            self.save_action(FallOffAction(direction))
        print("")

    def go_up(self) -> None:
        self.__move(Direction.UP)

    def go_right(self) -> None:
        self.__move(Direction.RIGHT)

    def go_down(self) -> None:
        self.__move(Direction.DOWN)

    def go_left(self) -> None:
        self.__move(Direction.LEFT)
