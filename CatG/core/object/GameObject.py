from CatG.core.object import CObject

class GameObject(CObject):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.x: int = x
        self.y: int = y
        self.cscripts: list = list()

    def on_enable(self):
        pass

    def update(self):
        pass