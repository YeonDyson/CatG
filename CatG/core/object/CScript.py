from CatG.core.object import CObject, GameObject


class CScript(CObject):
    def __init__(self, game_object: GameObject):
        super().__init__()
        self.game_object = game_object

    def on_enable(self):
        pass

    def update(self):
        pass