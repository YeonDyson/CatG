import types
from dataclasses import dataclass
from enum import Enum

import pygame.event

from CatG.GameManager import GameManager
from CatG.core.event.Event import Event
from CatG.core.event.Listener import Listener
from CatG.core.object import UpdatableCObject, CObject


class InputType(Enum):
    DOWN = 1
    UP = 2
    PRESSED = 3

@dataclass
class KeyData:
    func: types.MethodType
    input_type: InputType
    keys: list[int]

class KeyEvent(Event):
    def __init__(self, keys: list[int]):
        self.keys: list[int] = keys

class KeyEventManager(UpdatableCObject):
    key_events: dict[Listener, list[KeyData]] = {}

    @staticmethod
    def on_key(input_type: InputType, *keys):
        def decorator(func):
            func.is_key_event = True
            func.input_type = input_type
            func.keys = keys

            return func
        return decorator

    def on_create(self):
        pass

    def on_enable(self):
        pass

    def update(self):
        key_event_funcs: dict[types.MethodType, list[int]] = {}

        for event in GameManager().events:
            if event.type == pygame.KEYUP:
                for _ins, _key_datas in self.key_events.items():
                    if issubclass(type(_ins), UpdatableCObject):
                        if not _ins.enable:
                            continue

                    for key_data in _key_datas:
                        if event.key == key_data.keys and key_data.input_type == InputType.UP:
                            key_event_funcs.setdefault(key_data.func, []).append(event.key)

            if event.type == pygame.KEYDOWN:
                for _ins, _key_datas in self.key_events.items():
                    if issubclass(type(_ins), UpdatableCObject):
                        if not _ins.enable:
                            continue

                    for key_data in _key_datas:
                        if event.key == key_data.keys and key_data.input_type == InputType.DOWN:
                            key_event_funcs.setdefault(key_data.func, []).append(event.key)

        keys = pygame.key.get_pressed()
        for _ins, _key_datas in self.key_events.items():
            if issubclass(type(_ins), UpdatableCObject):
                if not _ins.enable:
                    continue

            for key_data in _key_datas:
                for key in key_data.keys:
                    if keys[key] and key_data.input_type == InputType.PRESSED:
                        key_event_funcs.setdefault(key_data.func, []).append(key)

        # print(key_pressed_funcs)
        # print(key_up_funcs)
        # print(key_down_funcs)

        for (func, keys) in key_event_funcs.items():
            func(KeyEvent(keys))

    def late_update(self):
        pass

    def register_listener(self, listener: 'Listener'):
        if not issubclass(listener.__class__, Listener):
            return

        event_methods = []

        for name in dir(listener):
            attr = getattr(listener, name)
            import types
            if isinstance(attr, types.MethodType) and getattr(attr.__func__, "is_key_event", False):
                event_methods.append((attr, attr.__func__.input_type, attr.__func__.keys))

        for attr, input_type, keys in event_methods:
            self.key_events.setdefault(listener, []).append(KeyData(attr, input_type, keys))


    def unregister_listener(self, listener: 'Listener'):
        if listener in self.key_events.keys():
            self.key_events.pop(listener)