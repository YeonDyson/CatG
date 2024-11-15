import numpy as np
import pygame

from CatG.core.game.camera import CameraFilter


class BrightnessContrastFilter(CameraFilter):
    brightness: int = 0
    contrast: int = 0

    def on_enable(self):
        pass

    def filtering(self, screen: pygame.Surface) -> pygame.Surface:
        screen_array = pygame.surfarray.pixels3d(screen).astype(np.int16)
        screen_array += self.brightness

        factor = (259 * (self.contrast + 255)) / (255 * (259 - self.contrast))
        screen_array = 128 + factor * (screen_array - 128)

        screen_array = np.clip(screen_array, 0, 255).astype(np.uint8)

        filtered_surface = pygame.surfarray.make_surface(screen_array)

        return filtered_surface