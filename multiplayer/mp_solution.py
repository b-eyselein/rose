from typing import Dict
from multiplayer.mp_robots import MultiPlayerRobot
from base.actions import *


class UserRobot(MultiPlayerRobot):

    def act(self, options: Dict) -> Action:
        return NoneAction()
        pass


class SampleRobot(MultiPlayerRobot):

    def act(self, options: Dict) -> Action:
        return NoneAction()
        pass
