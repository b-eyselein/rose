from abc import ABC, abstractmethod
from typing import Dict

from base.actions import Action


class SinglePlayerActor(ABC):

    @abstractmethod
    def run(self, options: Dict) -> None:
        pass


class MultiPlayerActor(ABC):

    @abstractmethod
    def act(self, options: Dict) -> Action:
        pass
