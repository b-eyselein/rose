from abc import ABC, abstractmethod
from base.actions import Action


class MultiPlayerActor(ABC):

    @abstractmethod
    def act(self, options) -> Action:
        pass
