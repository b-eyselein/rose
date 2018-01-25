from field import *

from movable import Movable, Action


class MarkAction(Action):

    def printable(self) -> str:
        pass


class Robot(Movable):
    """Robot which is operating on a field, starting on an initial point in the field. A robot can also mark a field"""

    def __init__(self, robot_name: str, field: Field, initial_point: Point = Point(), color: Colors = Colors.BLACK):
        super().__init__(robot_name, field, initial_point)
        self.__color = color  # Robot marks field with this color
        self.__field = field

    @property
    def color(self) -> Colors:
        return self.__color

    def pos_is_marked(self) -> bool:
        return self.__field.get(self.position.x, self.position.y).is_marked()

    def mark(self) -> None:
        self.__field.get(self.position.x, self.position.y).mark(self.__color)

    def act(self, options) -> Action:
        raise NotImplementedError


class UserRobot(Robot):
    def act(self, options) -> Action:
        height = options['height']
        width = options['width']
        for h in range(height - 1):
            self.mark()
            return self.go_up()

        for w in range(width - 1):
            self.mark()
            return self.go_right()

        for h in range(height - 1):
            self.mark()
            return self.go_down()

        for w in range(width - 1):
            self.mark()
            return self.go_left()

        pass


class SampleRobot(Robot):
    def act(self, options) -> Action:
        height = options['height']
        width = options['width']
        for h in range(height - 1):
            self.mark()
            return self.go_up()

        for w in range(width - 1):
            self.mark()
            return self.go_right()

        for h in range(height - 1):
            self.mark()
            return self.go_down()

        for w in range(width - 1):
            self.mark()
            return self.go_left()
        pass
