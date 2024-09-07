import uuid
from abc import ABC, abstractmethod


class CObject(ABC):
    object_id = None

    @abstractmethod
    def on_enable(self):
        pass

    def on_create(self):
        pass

    def on_destroy(self):
        pass