import pygame
from pygame import Vector2

from CatG.core.game import SpriteRender
from CatG.core.physics.Collider import Collider


class ColliderMask(Collider):
    _mask: pygame.mask = None

    def on_enable(self):
        sprite = self.gameObject.get_cscript(SpriteRender)
        if sprite is not None:
            self._mask = pygame.mask.from_surface(sprite.image._image)
        else:
            print(f"스프라이트 없으면 안되는데 {self.gameObject.name}: {self.__name__}")

    def update(self):
        pass

    def get_mask(self):
        return self._mask


    def get_size(self) -> Vector2:
        return Vector2(self._mask.get_size())

    def get_position(self) -> Vector2:
        return Vector2(
            self.gameObject.transform.position.x - int((self._mask.get_size()[0] / 2)),
            self.gameObject.transform.position.y + int((self._mask.get_size()[1] / 2))
        )

    def center(self) -> Vector2:
        return Vector2(
            self.gameObject.transform.position.x,
            self.gameObject.transform.position.y
        )