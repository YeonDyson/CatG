from CatG.core.asset.container import ImageContainer
from CatG.core.object import CObject
from CatG.core.object.container.ContainerObject import ContainerObject

class Frame(CObject):
    image: ImageContainer = None
    duration: int = 100

    def on_enable(self):
        pass


class AnimationClip(ContainerObject):
    name: str = None
    frames: list[Frame] = None
    loop: bool = False

    def on_enable(self):
        pass