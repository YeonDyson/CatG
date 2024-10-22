import uuid
from dataclasses import dataclass

from CatG.core.object.Cobject import CObject

class ContainerObject(CObject):
    _path: str = None
    # def __post_init__(self):
    #     super().__init__()

    def on_enable(self):
        pass
