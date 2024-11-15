import abc


class Interaction(abc.ABC):
    @abc.abstractmethod
    def on_interaction(self):
        pass