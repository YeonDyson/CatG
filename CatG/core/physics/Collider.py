import abc

import pygame
from pygame import Vector2

from CatG.core.object import CScript


class Collider(CScript, abc.ABC):
    trigger: bool = False
    position: Vector2 = Vector2(0, 0)

    def on_enable(self):
        pass

    def pre_update(self):
        pass

    def update(self):
        pass

    def late_update(self):
        pass

    @abc.abstractmethod
    def get_mask(self) -> pygame.mask.Mask:
        pass

    @abc.abstractmethod
    def get_size(self) -> Vector2:
        pass

    @abc.abstractmethod
    def get_position(self) -> Vector2:
        pass

    @abc.abstractmethod
    def center(self) -> Vector2:
        pass