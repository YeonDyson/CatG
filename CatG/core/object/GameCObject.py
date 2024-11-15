from typing import TypeVar, TYPE_CHECKING, Optional

from CatG.core.object.UpdatableCObject import UpdatableCObject
from CatG.core.game.Transform import Transform

if TYPE_CHECKING:
    from CatG.core.level import Level
    from CatG.core.game.Transform import Transform
    from CatG.core.object import CScript

class GameCObject(UpdatableCObject):
    _T = TypeVar("_T")
    _level: 'Level' = None
    _collision_other: 'GameCObject' = None
    name: str = ""
    tag: str = ""
    layer: bytes = 0
    child: list['GameCObject'] = []
    transform: 'Transform' = Transform()
    cscripts: list['CScript'] = []

    def on_enable(self):
        for cscript in self.cscripts:
            cscript.gameObject = self
            cscript.on_enable()

    def update(self):
        for cscript in self.cscripts:
            cscript.update()

    def on_destroy(self):
        pass

    def set_cscripts(self, cscript: 'CScript'):
        for _cscript in self.cscripts:
            if isinstance(cscript, type(_cscript)):
                raise ValueError("이미 있는데")

        self.cscripts.append(cscript)

    def get_cscript(self, cscript_type: type[_T]) -> Optional[_T]:
        for cscript in self.cscripts:
            if isinstance(cscript, cscript_type):
                return cscript

        return None

    def find_game_object(self):
        pass

    def on_collision_enter(self, other: 'GameCObject'):
        pass

    def on_collision_stay(self, other: 'GameCObject'):
        pass

    def on_collision_exit(self, other: 'GameCObject'):
        pass

    def on_trigger_enter(self, other: 'GameCObject'):
        pass

    def on_trigger_stay(self, other: 'GameCObject'):
        pass

    def on_trigger_exit(self, other: 'GameCObject'):
        pass