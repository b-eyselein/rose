from typing import Dict

from base.actions import *
from base.actors import MultiPlayerActor
from base.robot import Robot


class UserRobot(Robot, MultiPlayerActor):

    def act(self, options: Dict) -> Action:
        return NoneAction()
        pass


class SampleRobot(Robot, MultiPlayerActor):

    def act(self, options: Dict) -> Action:
        return NoneAction()
        pass
