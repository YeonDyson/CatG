import pygame
import pygame_gui

from CatG.GameManager import GameManager
from CatG.core.gui.Canvas import Canvas
from CatG.core.object import UpdatableCObject


class CatUiManager(UpdatableCObject):
    ui_manager = None
    canvas: list["Canvas"] = []

    def on_create(self):
        self.ui_manager = pygame_gui.UIManager(GameManager().screen.size)

    def on_enable(self):
        for _canvas in self.canvas:
            _canvas.on_enable()
            _canvas.setup_elements()

    def update(self):
        for event in GameManager().events:
            self.ui_manager.process_events(event)
        self.ui_manager.update(GameManager().delta_time)

        for _canvas in self.canvas:
            _canvas.update()


    def add_canvas(self, canvas: "Canvas"):
        canvas.ui_manager = self.ui_manager
        canvas.setup_elements()
        canvas.on_enable()
        self.canvas.append(canvas)

    def remove_canvas(self, canvas: "Canvas"):
        pass

    def get_screen(self) -> pygame.Surface:
        ui_surface = pygame.Surface(GameManager().screen.size, pygame.SRCALPHA)
        ui_surface.fill((0, 0, 0, 0))
        self.ui_manager.draw_ui(ui_surface)

        return ui_surface