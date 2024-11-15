from enum import EnumType

from pygame import Vector2

from CatG.core.object import CScript, GameCObject
from CatG.core.physics.Collider import Collider


class BodyType(EnumType):
    DYNAMIC = "dynamic"
    KINEMATIC = "kinematic"
    STATIC = "static"

class PhysicsBody(CScript):
    body_type: BodyType = BodyType.DYNAMIC
    velocity: Vector2 = Vector2(0, 0)
    mass: float = 0
    _collider: Collider = None

    def on_enable(self):
        self._collider = self.gameObject.get_cscript(Collider)

    def pre_update(self):
        pass

    def update(self):
        pass

    def late_update(self):
        pass