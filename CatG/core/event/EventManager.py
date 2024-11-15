import types
from typing import TYPE_CHECKING

from CatG.core.object import CObject

if TYPE_CHECKING:
    from CatG.core.event.Listener import Listener, event_handler
    from CatG.core.event.Event import Event

class EventManager(CObject):
    events: dict[type['Event'], dict['Listener', list['types.MethodType']]] = None

    def on_enable(self):
        self.events = {}

    def update(self):
        pass

    def register_listener(self, listener: 'Listener'):
        if not issubclass(listener.__class__, Listener):
            return

        event_methods = []

        for name in dir(listener):
            attr = getattr(listener, name)
            if isinstance(attr, types.MethodType) and getattr(attr.__func__, "is_listener", False):
                event_methods.append((attr, attr.__func__.listener_event))

        for attr, event in event_methods:
            if not self.events[event][listener]:
                self.events[event][listener] = []
            self.events[event][listener].append(attr)

    def unregister_listener(self, listener: 'Listener'):
        for (k, v) in self.events.items():
            if listener in v.keys():
                v.pop(listener)

    def call_event(self, event: 'Event'):
        for (listener, funcs) in self.events[event.__class__].items():
            for func in funcs:
                func(event)
