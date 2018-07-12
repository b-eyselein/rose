from base.actions import MarkAction
from base.field import Field, Vector2D, Colors
from base.movable import Movable


class Robot(Movable):
    """Robot which is operating on a field, starting on an initial point in the field. A robot can also mark a field"""

    def __init__(self, robot_name: str, field: Field, initial_point: Vector2D = Vector2D(), color: Colors = Colors.BLACK):
        super().__init__(robot_name, field, initial_point)
        self.__color = color  # Robot marks field with this color
        self.__field = field

    @property
    def color(self) -> Colors:
        return self.__color

    def pos_is_marked(self) -> bool:
        return self.__field.get_by_pos(self.position).is_marked()

    def mark(self) -> None:
        cell_to_mark = self.__field.get_by_pos(self.position)
        cell_to_mark.mark(self.__color)
        self.save_action(MarkAction(cell_to_mark, self.__color))
