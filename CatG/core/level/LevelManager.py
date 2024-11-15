from typing import TYPE_CHECKING

from pygame.transform import scale

from CatG.core.object import UpdatableCObject

if TYPE_CHECKING:
    from CatG.core.level import Level, LevelContainer
    from CatG.core.object import GameCObject

class LevelManager(UpdatableCObject):
    __enable_level: list['Level'] = []
    __dont_destroy_object: list['GameCObject'] = []
    active_level: 'Level' = None

    def update(self):
        for game_object in self.__dont_destroy_object:
            if not game_object.enable:
                continue

            game_object.update()

        self.active_level.update()

    def on_enable(self):
        pass

    def activate_level(self, level: 'LevelContainer'):
        from CatG.core.level import Level
        from CatG.GameManager import GameManager
        if self.find_level(level) is not None:
            self.active_level = self.find_level(level)

            return

        level_ins = GameManager().cobject_manager.instantiate(Level, init=lambda it: (it.set_level_container(level)))
        level_ins.on_enable()
        self.active_level = level_ins

    def deactivate_level(self, level: 'LevelContainer'):
        pass

    def load_level(self, level: 'LevelContainer'):
        from CatG.core.level import Level
        from CatG.GameManager import GameManager
        if self.find_level(level) is None:
            level_ins = GameManager().cobject_manager.instantiate(Level, init=lambda it: (it.set_level_container(level)))
            self.__enable_level.append(level_ins)
            level_ins.on_enable()

    def unload_level(self, level: 'LevelContainer'):
        self.__enable_level.remove(self.find_level(level))

    def find_level(self, level: 'LevelContainer') -> 'Level':
        for _level in self.__enable_level:
            if _level.level_container == level:
                return _level

        return None
