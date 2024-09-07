import abc
import uuid

from CatG.core.object.Cobject import CObject


class UpdatableCObject(CObject):
    def __init__(self, object_id: uuid.UUID = None, enable: bool = True):
        super().__init__(object_id)
        self.enable = enable

    @abc.abstractmethod
    def on_enable(self):
        pass

    @abc.abstractmethod
    def update(self):
        pass
