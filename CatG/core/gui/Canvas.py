import abc

import pygame_gui
from pygame_gui.core import UIElement

from CatG.core.object import UpdatableCObject

class Canvas(UpdatableCObject, abc.ABC):
    ui_manager: "pygame_gui.UIManager" = None
    enable: bool = True
    elements: list[UIElement] = []
    layer: int = 0

    @abc.abstractmethod
    def setup_elements(self):
        pass

    def update(self):
        if not self.enable:
            for element in self.elements:
                element.hide()
                element.disable()
        else:
            for element in self.elements:
                element.show()
                element.enable()

    def rander(self, surface):
        pass