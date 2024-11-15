import pygame
from pygame import Vector2

from CatG.core.physics.Collider import Collider


class ColliderBox(Collider):
    position: Vector2 = Vector2(0, 0)
    size: Vector2 = Vector2(1, 1)
    trigger: bool = False
    _rect: pygame.rect.Rect = None

    def on_enable(self):
        rect_position = Vector2(
            (self.gameObject.transform.position.x + self.position.x) - (self.size.x / 2),
            (self.gameObject.transform.position.y + self.position.y) - (self.size.y / 2)
        )
        self._rect = pygame.Rect(rect_position.x, rect_position.y, self.size.x, self.size.y)

    def update(self):
        self._rect.center = (
            self.gameObject.transform.position.x + self.position.x,
            self.gameObject.transform.position.y + self.position.y
        )

    def get_mask(self):
        return pygame.mask.Mask(self._rect.size, fill=True)

    def get_size(self) -> Vector2:
        return self.size

    def get_position(self) -> Vector2:
        pos = Vector2(
            (self.gameObject.transform.position.x + self.position.x) - int(self.size.x / 2),
            (self.gameObject.transform.position.y + self.position.y) + int(self.size.y / 2)
        )

        return Vector2(int(pos.x), int(pos.y))

    def center(self) -> Vector2:
        return Vector2(
            (self.gameObject.transform.position.x + self.position.x),
            (self.gameObject.transform.position.y + self.position.y)
        )