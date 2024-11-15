import abc
from typing import TYPE_CHECKING

from CatG.core.object import CObject

if TYPE_CHECKING:
    from CatG.core.object import GameCObject


class CScript(CObject):
    enable:bool = True
    gameObject: 'GameCObject' = None

    @abc.abstractmethod
    def on_enable(self):
        pass

    @abc.abstractmethod
    def pre_update(self):
        pass

    @abc.abstractmethod
    def update(self):
        pass

    @abc.abstractmethod
    def late_update(self):
        pass
