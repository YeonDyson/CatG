import abc
import uuid

from CatG.core.object.Cobject import CObject


class UpdatableCObject(CObject):
    enable: bool = True

    @abc.abstractmethod
    def on_enable(self):
        pass

    @abc.abstractmethod
    def update(self):
        pass
