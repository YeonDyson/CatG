import copy
import uuid
from abc import ABC, abstractmethod


class CObject(ABC):
    object_id = None
    _can_instantiate = False

    def __new__(cls, *args, **kwargs):
        if not cls._can_instantiate:
            raise TypeError(f"'{cls.__name__}' 클래스는 직접 인스턴스화 할수 없음 꺼져")

        __instance = super().__new__(cls)

        cls.object_id = uuid.uuid4()
        for name, value in cls.__dict__.items():
            if not name.startswith('__') and not name.startswith('_abc') and name != '_can_instantiate' and not callable(value):
                try:
                    setattr(__instance, name, copy.deepcopy(value))
                except TypeError:
                    setattr(__instance, name, value)

        return __instance

    @abstractmethod
    def on_enable(self):
        pass

    def on_create(self):
        pass

    def on_destroy(self):
        pass