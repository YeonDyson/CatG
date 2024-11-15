import pygame
import numpy as np
from CatG.core.game.camera import CameraFilter

class BlackAndWhiteFilter(CameraFilter):
    # 색상 계열별 강도 비율 (0 ~ 100)
    red_weight: int = 0
    yellow_weight: int = 0
    green_weight: int = 0
    cyan_weight: int = 0
    blue_weight: int = 0
    magenta_weight: int = 0

    def on_enable(self):
        pass

    def filtering(self, screen: pygame.Surface) -> pygame.Surface:
        screen_array = pygame.surfarray.pixels3d(screen).astype(np.int16)

        red_channel = screen_array[..., 0] * (self.red_weight / 100)
        yellow_channel = (screen_array[..., 0] + screen_array[..., 1]) * (self.yellow_weight / 100)
        green_channel = screen_array[..., 1] * (self.green_weight / 100)
        cyan_channel = (screen_array[..., 1] + screen_array[..., 2]) * (self.cyan_weight / 100)
        blue_channel = screen_array[..., 2] * (self.blue_weight / 100)
        magenta_channel = (screen_array[..., 0] + screen_array[..., 2]) * (self.magenta_weight / 100)

        gray_values = red_channel + yellow_channel + green_channel + cyan_channel + blue_channel + magenta_channel
        gray_values = np.clip(gray_values, 0, 255).astype(np.uint8)

        filtered_array = np.stack((gray_values,)*3, axis=-1)

        filtered_surface = pygame.surfarray.make_surface(filtered_array)

        return filtered_surface
