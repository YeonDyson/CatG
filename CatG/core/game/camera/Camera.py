from dataclasses import dataclass

import pygame
from pygame import Vector2, Surface

from CatG.core.game.camera.CameraFilter import CameraFilter
from CatG.core.object import CScript, CObject


# Just let me be your fan
# I wanna be your fan
# I'm still your biggest fan

class FilterLayer(CObject):
    layer: int = 0
    camera_filters: list[CameraFilter] = []

    def on_enable(self):
        pass


class Camera(CScript):
    camera_width: int = 0
    camera_height: int = 0
    back_ground_color: tuple = (0, 0, 0)
    position: Vector2 = Vector2(0, 0)
    filter_layers: list[FilterLayer] = []

    def on_enable(self):
        pass

    def pre_update(self):
        pass

    def update(self):
        pass

    def late_update(self):
        pass

    def get_screen_center_to_world(self) -> Vector2:
        return Vector2(int(self.gameObject.transform.position.x - (self.camera_width / 2)), int(self.gameObject.transform.position.y + (self.camera_height / 2)))

    def filter_rander(self, screen: Surface) -> Surface | None:
        if len(self.filter_layers) <= 0:
            return screen

        filtered_screens: list[Surface] = []
        _filter_layers = sorted(self.filter_layers, key=lambda it: it.layer)

        for layers in _filter_layers:
            filter_screen = screen.copy()
            camera_filters = sorted(layers.camera_filters, key=lambda it: it.layer)
            for camera_filter in camera_filters:
                camera_filter.filtering(filter_screen)

            filtered_screens.append(filter_screen)

        final_surface = Surface(screen.get_size(), pygame.SRCALPHA)

        for filtered in filtered_screens:
            final_surface.blit(filtered, (0, 0))

        return final_surface

    def add_filter(self, camera_filter: CameraFilter):
        pass

    def remove_filter(self, camera_filter: CameraFilter):
        pass