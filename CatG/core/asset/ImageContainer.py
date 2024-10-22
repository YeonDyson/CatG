import pygame

from CatG.core.object import ContainerObject

class ImageContainer(ContainerObject):
    image_path: str = None
    _image: pygame.Surface = None
    image_size: tuple = (0, 0)

    def on_enable(self):
        pass