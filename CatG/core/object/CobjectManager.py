import os
import sys

from typing import TypeVar

from CatG.core.level.Level import Level
from CatG.core.object.Cobject import CObject
from CatG.core.object.container.ContainerManager import ContainerManager
from CatG.core.object.container.ContainerObject import ContainerObject


class CObjectManager:
    _instance = None

    T = TypeVar('T')

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
            ContainerManager()

    def __load_cobject(self):
        import importlib
        import inspect

        root_package = os.path.dirname(sys.modules['__main__'].__file__)

        for (root, dirs, files) in os.walk(root_package):
            for file in files:
                if file.endswith('.py') and not file.startswith('__'):
                    root_path = root.replace(sys.path[1], '')
                    module_name = f"{root_path.replace('/', '.')}.{file[:-3]}"[1:]

                    module = importlib.import_module(module_name)

                    for name, obj in inspect.getmembers(module, inspect.isclass):
                        if issubclass(obj, CObject) and obj is not CObject:
                            self.cachingCObjects[name] = obj

    def is_cobject(self, name: str) -> bool:
        return name in self.cachingCObjects

    def instantiate(self, cobject: type[T], level: Level = None) -> T:
        if not issubclass(cobject, CObject):
            raise TypeError(f"{cobject.__name__} CObject가 아니잔아")

        cobject._can_instantiate = True
        instance = cobject()
        instance.on_enable()

        if issubclass(cobject, ContainerObject):
            ContainerManager().containerCObjects.append(instance)

        if level is not None:
            # TODO: 레벨 오브젝트 등록
            pass

        cobject._can_instantiate = False
        return instance

    def instantiate_by_name(self, name: str, level: Level = None) -> CObject:
        cobject: type = self.cachingCObjects.get(name)
        if cobject is None:
            raise NameError(f"{name}라는 CObject는 없음")

        cobject._can_instantiate = True

        instance = cobject()
        instance.on_enable()

        if issubclass(cobject, ContainerObject):
            ContainerManager().containerCObjects.append(instance)


        if level is not None:
            # TODO: 레벨 오브젝트 등록
            pass

        cobject._can_instantiate = False
        return instance

