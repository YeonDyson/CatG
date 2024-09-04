from typing import List
from pathlib import Path
from CatG.core.object import CObject

class CObjectManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(CObjectManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.cachingCObjects: Path = None
            self.enabledCObjects: List[CObject] = []
            self.dontDestroyCObjects: List[CObject] = []
            self.initialized = True

    def register_cobject(self, cobject: CObject):
        self.enabledCObjects.append(cobject)
        cobject.on_create()

    def unregister_cobject(self, cobject: CObject):
        if cobject in self.enabledCObjects:
            cobject.on_destroy()
            self.enabledCObjects.remove(cobject)

    def register_dont_destroy(self, cobject: CObject):
        if cobject in self.enabledCObjects:
            cobject.on_destroy()
            self.enabledCObjects.remove(cobject)

        self.dontDestroyCObjects.append(cobject)
