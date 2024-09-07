import uuid

from CatG.core.object.UpdatableCObject import UpdatableCObject


class GameCObject(UpdatableCObject):
    def __init__(self, x:int, y:int, object_id: uuid.UUID = None):
        super().__init__(object_id=object_id)
        self.x = x
        self.y = y

    def draw(self):
        pass

    def on_enable(self):
        pass

    def update(self):
        pass

    def on_create(self):
        pass

    def on_destroy(self):
        pass

