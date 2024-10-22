from abc import ABC, abstractmethod

class CustomAdapter(ABC):
    @abstractmethod
    def to_dict(self, obj) -> dict:
        pass

    @abstractmethod
    def from_dict(self, data: dict):
        pass