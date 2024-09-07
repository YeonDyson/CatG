import uuid
from abc import ABC, abstractmethod


class CObject(ABC):
    def __init__(self, object_id: uuid.UUID = None):
        self.object_id = object_id

    @abstractmethod
    def on_enable(self):
        pass

    def on_create(self):
        pass

    def on_destroy(self):
        pass