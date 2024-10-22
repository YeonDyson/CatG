from CatG.core.object import GameCObject
from CatG.core.object.Cobject import CObject


class Level(CObject):
    enable_gameCObject: list[GameCObject]

    def on_enable(self):
        pass