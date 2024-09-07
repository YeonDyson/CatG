import uuid

from CatG.core.object.Cobject import CObject


class ContainerObject(CObject):
    def __init__(self, object_id: uuid.UUID = None):
        super().__init__(object_id=object_id)

    def on_enable(self):
        pass