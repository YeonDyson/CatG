from CatG.GameManager import GameManager
from CatG.core.gui.Canvas import Canvas
from CatG.core.object import CScript
from CatG.scripts.ui.MainUI import MainUI


class LoadUI(CScript):
    canvas: Canvas = None

    def on_enable(self):
        self.gameObject._level.cat_ui_manager.add_canvas(self.canvas)

    def pre_update(self):
        pass

    def update(self):
        pass

    def late_update(self):
        pass