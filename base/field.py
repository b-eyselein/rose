from dataclasses import dataclass
from enum import Enum


class Colors(Enum):
    WHITE = 0
    RED = 1
    ORANGE = 2
    YELLOW = 3
    GREEN = 4
    BLUE = 5
    PURPLE = 6
    BLACK = 7

    def __str__(self):
        return self.name


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


@dataclass()
class Point:
    """Simple point with x- and y-coordinate"""
    _x: int = 0
    _y: int = 0

    def __post_init__(self):
        assert self._x >= 0 and self._y >= 0, "Beide Koordinaten eines Punktes müssen größer als 0 sein!"

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y


@dataclass()
class Cell:
    """Single panel of a field"""
    _position: Point
    _color: Colors = Colors.WHITE

    @property
    def color(self):
        return self._color

    @property
    def position(self) -> Point:
        return self._position

    def mark(self, color: Colors) -> None:
        self._color = color

    def is_marked(self) -> bool:
        return self._color != Colors.WHITE

    def __str__(self):
        if self.is_marked():
            return ' X '
        else:
            return ' O '


class Field:
    """Two dimensional field of cells"""

    def __init__(self, height: int = 10, width: int = 10, has_border: bool = False):
        assert 0 < height < 100, 'Größe des Feldes muss zwischen 0 und 100 (jeweils exklusiv) liegen!'
        assert 0 < width < 100, 'Breite des Feldes muss  zwischen 0 und 100 (jeweils exklusiv) liegen!'

        self.__height__ = height
        self.__width__ = width
        self.__has_border__ = has_border
        self._cells = [
            [
                Cell(Point(x, y)) for x in range(width)
            ] for y in range(height)
        ]

    @property
    def height(self) -> int:
        return self.__height__

    @property
    def width(self) -> int:
        return self.__width__

    @property
    def has_border(self) -> bool:
        return self.__has_border__

    def get_by_coordinates(self, x: int, y: int) -> Cell:
        return self._cells[x][y]

    def get_by_pos(self, position: Point) -> Cell:
        return self._cells[position.x][position.y]

    def __str__(self):
        string = ''
        for row_index, row in enumerate(self._cells[::-1]):
            row_string = ''

            for cell in row:
                row_string += str(cell)

            string += "{:3d} | ".format(self.__height__ - row_index) + row_string + '\n'

        coordinate_x = '    | ' + ''.join(map(lambda w: "{:^3d}".format(w + 1), range(self.__width__)))
        string += ('-' * len(coordinate_x)) + '\n' + coordinate_x

        return string
