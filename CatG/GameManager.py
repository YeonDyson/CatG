import pygame
from pygame import Surface
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from CatG.core.asset import AssetManager
    from CatG.core.event.key.KeyEventManager import KeyEventManager
    from CatG.core.game import GameSetting
    from CatG.core.level import LevelManager
    from CatG.core.object.CobjectManager import CObjectManager
    from CatG.core.object.container.ContainerManager import ContainerManager

class GameManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(GameManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.cobject_manager: CObjectManager = None
            self.container_manager: ContainerManager = None
            self.level_manager: LevelManager = None
            self.game_setting: GameSetting = None
            self.screen: Surface = None
            self.key_event_manager: KeyEventManager = None
            self.events = None
            self.delta_time = None

    def initialize(self):
        from CatG.core.asset import AssetManager
        from CatG.core.event.key.KeyEventManager import KeyEventManager
        from CatG.core.game import GameSetting
        from CatG.core.level import LevelManager
        from CatG.core.object.CobjectManager import CObjectManager
        from CatG.core.object.container.ContainerManager import ContainerManager

        self.cobject_manager = CObjectManager()
        self.container_manager = ContainerManager()
        self.level_manager = self.cobject_manager.instantiate(LevelManager)
        self.game_setting = AssetManager.load_assets("assets/game_setting", GameSetting)
        if self.game_setting.fullscreen:
            self.screen = pygame.display.set_mode(self.game_setting.get_screen_size(), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)
        else:
            self.screen = pygame.display.set_mode(self.game_setting.get_screen_size(), pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.key_event_manager = self.cobject_manager.instantiate(KeyEventManager)