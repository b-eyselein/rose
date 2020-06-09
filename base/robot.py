from dataclasses import dataclass

from base.actions import MarkAction
from base.field import Colors, Cell
from base.movable import Movable


@dataclass()
class Robot(Movable):
    """
    Robot which is operating on a field, starting on an initial point in the field. A robot can also mark a field.
    """
    _color: Colors = Colors.BLACK  # Robot marks field with this color

    @property
    def color(self) -> Colors:
        return self._color

    def pos_is_marked(self) -> bool:
        return self._field.get_by_pos(self.position).is_marked()

    def mark(self) -> None:
        cell_to_mark: Cell = self._field.get_by_pos(self.position)
        cell_to_mark.mark(self._color)
        self.save_action(MarkAction(cell_to_mark, self._color))
