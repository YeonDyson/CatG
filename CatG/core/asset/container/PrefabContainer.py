from typing import TYPE_CHECKING

from CatG.core.object import ContainerObject

if TYPE_CHECKING:
    from CatG.core.object import GameCObject

class PrefabContainer(ContainerObject):
    prefab_name = 'Prefab'
    prefab_gameObject: 'GameCObject' = None