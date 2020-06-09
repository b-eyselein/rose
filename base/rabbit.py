from random import randint

from base.actions import Action, NoneAction, MoveAction, Direction
from base.movable import Movable


class Rabbit(Movable):

    def save_action(self, options) -> Action:
        act_int = randint(0, 9)
        if act_int == 1:
            return MoveAction(Direction.LEFT)
        elif act_int == 2:
            return MoveAction(Direction.RIGHT)
        elif 3 <= act_int <= 4:
            return MoveAction(Direction.UP)
        elif 5 <= act_int <= 6:
            return MoveAction(Direction.DOWN)
        else:
            return NoneAction()
