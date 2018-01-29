from typing import Dict
from abc import abstractmethod
from base.robot import Robot


class SingleActorRobot(Robot):

    @abstractmethod
    def run(self, options: Dict) -> None:
        pass
