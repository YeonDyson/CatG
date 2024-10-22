from CatG.core.object import ContainerObject, GameCObject


class PrefabContainer(ContainerObject):
    prefab_name = 'Prefab'
    prefab_gameObject: GameCObject = None