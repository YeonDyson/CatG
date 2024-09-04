from abc import ABC, abstractmethod


class CObject(ABC):
    def __init__(self, object_id=None):
        super().__init__()
        self.object_id = object_id
        self.enabled = True

    @abstractmethod
    def on_enable(self):
        pass

    @abstractmethod
    def update(self):
        pass

    def on_create(self):
        print(f"Object {self.object_id} created at ")

    def on_destroy(self):
        """객체가 삭제될 때 호출"""
        print(f"Object {self.object_id} is being destroyed.")
