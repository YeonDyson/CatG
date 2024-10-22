import uuid

from pygame import Vector2

from CatG.core.object.CScript import CScript
from CatG.core.object.UpdatableCObject import UpdatableCObject


class GameCObject(UpdatableCObject):
    name: str = ""
    tag: str = ""
    layer: bytes = 0
    child: list['GameCObject'] = []
    position: Vector2 = Vector2(0, 0)
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

