import pygame

from CatG.core.asset import AssetManager
from CatG.core.object import ContainerObject

class ImageContainer(ContainerObject):
    image_path: str = None
    _image: pygame.Surface = None

    def on_enable(self):
        from CatG.core.asset import AssetManager

        if self.image_path is not None:
            self._image = AssetManager.load_image(self.image_path)