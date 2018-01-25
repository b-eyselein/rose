from abc import abstractmethod
from typing import Dict, List

from field import *
from movable import Action, Movable


class MarkAction(Action):

    def __init__(self, cell: Cell, color: Colors):
        self.__cell = cell
        self.__color = color

    def printable(self) -> str:
        return "Marking cell {} with color {}.".format(self.__cell.position, self.__color)


class Robot(Movable):
    """Robot which is operating on a field, starting on an initial point in the field. A robot can also mark a field"""

    def save_action(self, action: Action):
        self.__actions.append(action)

    def __init__(self, robot_name: str, field: Field, initial_point: Point = Point(), color: Colors = Colors.BLACK):
        super().__init__(robot_name, field, initial_point)
        self.__color = color  # Robot marks field with this color
        self.__field = field
        self.__actions: List[Action] = []

    @property
    def color(self) -> Colors:
        return self.__color

    def pos_is_marked(self) -> bool:
        return self.__field.get_by_pos(self.position).is_marked()

    def mark(self) -> None:
        cell_to_mark = self.__field.get_by_pos(self.position)
        cell_to_mark.mark(self.__color)
        self.save_action(MarkAction(cell_to_mark, self.__color))


class SingleActorRobot(Robot):

    @abstractmethod
    def run(self, options: Dict) -> None:
        pass
