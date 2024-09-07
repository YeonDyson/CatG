import os
import sys

from typing import TypeVar

from CatG.core.object.Cobject import CObject


class CObjectManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(CObjectManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            T = TypeVar('T')
            self.cachingCObjects: dict[str, T] = {}
            self.initialized = True
            self.__load_cobject()

    def __load_cobject(self):
        import importlib
        import inspect


        root_package = os.path.dirname(sys.modules['__main__'].__file__)
        root_package_path = root_package.replace(sys.path[1], '')

        for (root, dirs, files) in os.walk(root_package):
            for file in files:
                if file.endswith('.py') and not file.startswith('__'):
                    root_sibal = root.replace(sys.path[1], '')
                    module_name = f"{root_sibal.replace('/', '.')}.{file[:-3]}"[1:]

                    module = importlib.import_module(module_name)

                    for name, obj in inspect.getmembers(module, inspect.isclass):
                        if issubclass(obj, CObject) and obj is not CObject:
                            self.cachingCObjects[name] = obj
