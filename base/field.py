from enum import Enum
from abc import ABC


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


class Point:
    """Simple point with x- and y-coordinate"""

    def __init__(self, x: int = 0, y: int = 0):
        assert x >= 0 and y >= 0, "Beide Koordinaten eines Punktes müssen größer als 0 sein!"
        self.__x = x
        self.__y = y

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    def __str__(self):
        return "({}, {})".format(self.__x, self.__y)


class Cell:
    """Single panel of a field"""

    def __init__(self, position: Point = Point(0, 0)):
        self.__position = position
        self.__color = Colors.WHITE

    @property
    def color(self):
        return self.__color

    @property
    def position(self) -> Point:
        return self.__position

    def mark(self, color: Colors) -> None:
        self.__color = color

    def is_marked(self) -> bool:
        return self.__color != Colors.WHITE

    def __str__(self):
        if self.is_marked():
            return ' X '
        else:
            return ' O '


class Field:
    """Two dimensional field of cells"""

    def __init__(self, height: int = 10, width: int = 10, has_border: bool = False):
        assert 0 < height < 100, 'Größe des Feldes muss zwischen 0 und 100 (jeweils exklusiv) liegen!'
        assert 0 < width < 100, 'Breite des Feldes muss  zwischen 0 und 100 (jeweils exklusiv liegen!'
        self.__height = height
        self.__width = width
        self.__has_border = has_border
        self.__panels = [[Cell(Point(x, y)) for x in range(width)] for y in range(height)]

    @property
    def height(self) -> int:
        return self.__height

    @property
    def width(self) -> int:
        return self.__width

    @property
    def has_border(self) -> bool:
        return self.__has_border

    def get_by_coordinates(self, x: int, y: int) -> Cell:
        return self.__panels[x][y]

    def get_by_pos(self, position: Point) -> Cell:
        return self.__panels[position.x][position.y]

    def __str__(self):
        string = ''
        for row_index, row in enumerate(self.__panels[::-1]):
            row_string = ''

            for cell in row:
                row_string += str(cell)

            string += "{:3d} | ".format(self.__height - row_index) + row_string + '\n'

        coordinate_x = '    | ' + ''.join(map(lambda w: "{:^3d}".format(w + 1), range(self.__width)))
        string += ('-' * len(coordinate_x)) + '\n' + coordinate_x

        return string


class FieldObject(ABC):
    pass
