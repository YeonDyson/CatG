import uuid
from dataclasses import dataclass

from CatG.core.object.Cobject import CObject

@dataclass
class ContainerObject(CObject):
    object_id: uuid.UUID = None

    def __post_init__(self):
        super().__init__(object_id=self.object_id)

    def on_enable(self):
        pass
