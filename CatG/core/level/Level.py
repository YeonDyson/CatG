from typing import TYPE_CHECKING

import pygame
from pygame import Vector2

from CatG.GameManager import GameManager
from CatG.core.gui.CatUiManager import CatUiManager
from CatG.core.level import LevelContainer
from CatG.core.object import UpdatableCObject

if TYPE_CHECKING:
    from CatG.core.object import GameCObject
    from CatG.core.level import LevelContainer
    from CatG.core.object import CScript

class Level(UpdatableCObject):
    __dont_destroy_object: list['GameCObject'] = []
    level_container: 'LevelContainer' = None
    level_name: str = None
    tags: list[str] = None
    gameCObjects: list['GameCObject'] = None
    main_camera: 'GameCObject' = None
    cat_ui_manager: 'CatUiManager' = None

    def on_enable(self):
        self.gameCObjects = self.level_container.gameObject
        self.tags = self.level_container.tag
        self.level_name = self.level_container.levelName
        self.cat_ui_manager = GameManager().cobject_manager.instantiate(CatUiManager)

        for gameCObject in self.gameCObjects:
            gameCObject._level = self

            gameCObject.on_enable()

        if self.main_camera is None:
            self.main_camera = self.find_game_object_by_name("main camera")

        from CatG.core.physics.PixelPhysics import PixelPhysics
        from CatG.core.object import GameCObject
        if self.find_game_object_by_script(PixelPhysics) is None:
            self.register_game_object(GameManager().cobject_manager.instantiate(
                GameCObject, init= lambda it: (
                    it.set_cscripts(GameManager().cobject_manager.instantiate(PixelPhysics)),
                    setattr(it, 'name', "pixel physics"),
                    setattr(it, 'tag', "physics")
                )
            ))

    def update(self):
        for _gameCObject in self.gameCObjects:
            for cscript in _gameCObject.cscripts:
                cscript.pre_update()

        for _gameCObject in self.gameCObjects:
            _gameCObject.update()

        self.cat_ui_manager.update()

        self.__render()

        for _gameCObject in self.gameCObjects:
            for cscript in _gameCObject.cscripts:
                cscript.late_update()

    def __render(self):
        from CatG.core.game.SpriteRender import SpriteRender
        from CatG.core.game.camera import Camera

        _gameCObjects = sorted(self.gameCObjects, key=lambda it: it.layer)
        camera_script = self.main_camera.get_cscript(Camera)

        camera_size = Vector2(camera_script.camera_width, camera_script.camera_width)
        screen_size = Vector2(GameManager().screen.get_size())
        scale_ratio = screen_size.x / camera_size.x

        render_surface = pygame.Surface(camera_size)
        render_surface.fill(tuple(camera_script.back_ground_color))

        for _game_object in _gameCObjects:
            if not _game_object.enable:
                continue

            sprite_render = _game_object.get_cscript(SpriteRender)
            if sprite_render is None:
                continue

            sprite = sprite_render.render()

            object_screen_offset = (_game_object.transform.position - camera_script.get_screen_center_to_world())
            object_screen_offset.y = -object_screen_offset.y

            offset = pygame.Vector2(int(sprite.get_size()[0] / 2), int(sprite.get_size()[1] / 2))
            offset_position = object_screen_offset - offset

            render_surface.blit(sprite, offset_position)

        filter_screen = camera_script.filter_rander(render_surface)
        scaled_render_surface = pygame.transform.scale(filter_screen, camera_size*scale_ratio)
        GameManager().screen.blit(scaled_render_surface, (0, 0))

        GameManager().screen.blit(self.cat_ui_manager.get_screen(), (0, 0))

    def find_game_object_by_name(self, name: str) -> 'GameCObject':
        for gameCObject in self.gameCObjects:
            if gameCObject.name == name:
                return gameCObject

        return None

    def find_game_object_by_script(self, cscript: type['CScript']) -> 'GameCObject':
        for gameCObject in self.gameCObjects:
            if gameCObject.get_cscript(cscript) is not None:
                return gameCObject

        return None

    def get_game_objects_by_script(self, cscript: type['CScript']) -> list['GameCObject']:
        game_objects = []
        for gameCObject in self.gameCObjects:
            if gameCObject.get_cscript(cscript) is not None:
                game_objects.append(gameCObject)

        return game_objects

    def register_game_object(self, game_object: 'GameCObject'):
        if game_object not in self.gameCObjects:
            self.gameCObjects.append(game_object)
            game_object._level = self
            game_object.on_enable()

    def unregister_game_object(self, game_object: 'GameCObject'):
        pass

    def set_level_container(self, level_container: 'LevelContainer'):
        self.level_container = level_container