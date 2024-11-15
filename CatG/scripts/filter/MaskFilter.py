import pygame

from CatG.core.game.camera import CameraFilter


class MaskFilter(CameraFilter):
    def on_enable(self):
        pass

    def filtering(self, screen: pygame.Surface) -> pygame.Surface:
        pass