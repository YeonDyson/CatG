from typing import TYPE_CHECKING

import pygame
from pygame import Surface, Vector2

from CatG.GameManager import GameManager
from CatG.core.object.CScript import CScript
from CatG.core.asset.container import ImageContainer

if TYPE_CHECKING:
    from CatG.core.asset.container import ImageContainer


class SpriteRender(CScript):
    image: 'ImageContainer' = None

    def on_enable(self):
        self.image.on_enable()

    def pre_update(self):
        pass

    def update(self):
        pass

    def late_update(self):
        pass

    def render(self) -> Surface:
        transform =  self.gameObject.transform
        image = self.image._image
        render_surface = pygame.transform.scale(
            image,
            (int(image.get_width() * transform.scale.x), int(image.get_height() * transform.scale.y))
        )
        render_surface = pygame.transform.rotate(render_surface, transform.rotation)
        render_surface = pygame.transform.flip(render_surface, transform.flip_x, transform.flip_y)

        return render_surface