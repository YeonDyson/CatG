from typing import Type, TYPE_CHECKING

if TYPE_CHECKING:
    from CatG.core.event.Event import Event


def event_handler(event: type['Event']):
    def decorator(func):
        func.is_listener = True
        func.listener_event = event

        return func
    return decorator


class Listener:
    def weeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee(self):
        print('이것은 위대한 리스너라는 증표인것이다')