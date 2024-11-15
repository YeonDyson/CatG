from CatG.core.gui.Canvas import Canvas
from CatG.core.object.container.ContainerObject import ContainerObject


class DialogData(ContainerObject):
    dialog: str = []

class DialogUI(Canvas):
    def setup_elements(self):
        pass

    def on_enable(self):
        pass