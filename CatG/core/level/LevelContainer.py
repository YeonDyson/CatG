from pygame import Vector2

from CatG.core.object import ContainerObject, GameCObject


class LevelContainer(ContainerObject):
    levelName: str = "sibal"
    tag: list[str] = []
    gameObject: list[GameCObject] = []