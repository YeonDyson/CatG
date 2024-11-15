from typing import TYPE_CHECKING

from CatG.core.object import ContainerObject

if TYPE_CHECKING:
    from CatG.core.object import GameCObject

class LevelContainer(ContainerObject):
    levelName: str = "sibal"
    tag: list[str] = []
    gameObject: list['GameCObject'] = []

    def on_enable(self):
        pass