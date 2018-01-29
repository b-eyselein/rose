from abc import abstractmethod
from typing import Dict

from base.actions import Action
from base.robot import Robot
from multiplayer.mp_actor import MultiPlayerActor


class MultiPlayerRobot(Robot, MultiPlayerActor):

    @abstractmethod
    def act(self, options: Dict) -> Action:
        raise NotImplementedError
