import abc

import pygame

from CatG.core.object import UpdatableCObject, CObject


class CameraFilter(CObject, abc.ABC):
    layer: int = 0

    @abc.abstractmethod
    def filtering(self, screen: pygame.Surface) -> pygame.Surface:
        pass