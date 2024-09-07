import uuid

from CatG.core.object.Cscript import CScript
from CatG.core.object.UpdatableCObject import UpdatableCObject


class GameCObject(UpdatableCObject):
    x:bool = 0
    y:bool = 0
    cscripts: list[CScript] = []

    def draw(self):
        pass

    def on_enable(self):
        pass

    def update(self):
        pass

    def on_create(self):
        pass

    def on_destroy(self):
        pass

