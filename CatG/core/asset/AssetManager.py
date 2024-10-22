import os
import pygame
from dataclasses import dataclass
from typing import TypeVar, Type, Any

from pygame import Surface

from CatG.core.asset import ImageContainer, SoundContainer
from CatG.core.object import ContainerObject, CObjectManager
from CatG.core.serialization.Serialize import Serializer

T = TypeVar('T')

@dataclass
class AssetData:
    path: str
    data: Any = None

class AssetManager:
    _cache: dict[str, AssetData] = {}

    @staticmethod
    def load_assets(path, t: Type[T] = None) -> T:
        path = path if path.endswith('.cntr') else path + ".cntr"
        path = os.path.abspath(path)

        if not issubclass(t, ContainerObject):
            raise TypeError

        if path in AssetManager._cache.keys():
            return AssetManager._cache[path].data

        with open(path, 'r') as f:
            data = f.read()

            container_object = Serializer.deserialize(data)
            container_object._path = path

        AssetManager._cache[path] = AssetData(path, container_object)

        return container_object

    @staticmethod
    def load_image(path) -> Surface:
        path = os.path.abspath(path)
        if path in AssetManager._cache:
            return AssetManager._cache[path].data

        image = pygame.image.load(path)
        return image

    @staticmethod
    def load_sound(path) -> SoundContainer:
        pass
