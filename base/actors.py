from abc import ABC, abstractmethod
from base.actions import Action, NoneAction
from typing import Dict


class SinglePlayerActor(ABC):

    @abstractmethod
    def run(self, options: Dict) -> None:
        pass


class MultiPlayerActor(ABC):

    @abstractmethod
    def act(self, options: Dict) -> Action:
        pass
