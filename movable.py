from enum import Enum

from field import Field, Point


class Direction(Enum):
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4


class Action:
    def printable(self) -> str:
        raise NotImplementedError


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


class Actor:
    def act(self, options) -> Action:
        raise NotImplementedError


class Movable(Actor):
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

    def go_up(self) -> Action:
        if self.__position.x < self.__field.height:
            return MoveAction(Direction.UP)
        elif self.__field.has_border:
            return BumpWallAction(Direction.UP)
        else:
            return FallOffAction(Direction.UP)

    def go_right(self) -> Action:
        if self.__position.y < self.__field.width:
            return MoveAction(Direction.RIGHT)
        elif self.__field.has_border:
            return BumpWallAction(Direction.RIGHT)
        else:
            raise FallOffError(self, Direction.RIGHT)

    def go_down(self) -> Action:
        if self.__position.x > 0:
            return MoveAction(Direction.DOWN)
        elif self.__field.has_border:
            return BumpWallAction(Direction.DOWN)
        else:
            return FallOffAction(Direction.DOWN)

    def go_left(self) -> Action:
        if self.__position.y > 0:
            return MoveAction(Direction.LEFT)
        elif self.__field.has_border:
            return BumpWallAction(Direction.LEFT)
        else:
            return FallOffAction(Direction.LEFT)

    def act(self, options) -> Action:
        raise NotImplementedError


class FallOffError(Exception):
    """Exception raised if robot fell of field"""

    def __init__(self, movable: Movable, direction: Direction):
        self.robot_id = movable.name
        self.direction = direction

    def __str__(self):
        return "The Robot {} fell of the field while going {}".format(self.robot_id, self.direction)
