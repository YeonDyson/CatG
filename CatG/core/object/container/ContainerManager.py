import os
import sys
from itertools import count
from os.path import split
from typing import TypeVar, Any


class ContainerManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ContainerManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            T = TypeVar('T')
            self.cache_paths: list[str] = []
            from CatG.core.object import ContainerObject
            self.containerCObjects: list[ContainerObject] = []
            self.initialized = True
            self.__load_container()

    def __load_container(self):
        from CatG.core.object import ContainerObject
        from CatG.core.asset import AssetManager

        root_package = os.path.dirname(sys.modules['__main__'].__file__)
        for (root, dirs, files) in os.walk(root_package):
            for file in files:
                if file.endswith('.cntr'):
                    self.cache_paths.append(os.path.join(root, file))

        for path in self.cache_paths:
            instance = AssetManager.load_assets(path, ContainerObject)
            if instance not in self.containerCObjects:
                self.containerCObjects.append(instance)

        print(self.containerCObjects[0].gameObject[0].__dict__)

    def ref_container(self, path) -> Any:
        ref_path = path.split('.')
        for cached_path in self.cache_paths:
            root = os.path.dirname(sys.modules['__main__'].__file__)
            split_path = cached_path.removeprefix(root).lstrip("/").split("/")

            file_index = -1

            for i, e in enumerate(split_path):

                if e == ref_path[i]:
                    continue

                if e.endswith(".cntr") and e.replace(".cntr", "") == ref_path[i]:
                    file_index = i + 1
                    break

            if file_index == -1:
                continue

            ref_obj = None
            for object in self.containerCObjects:
                if object._path == cached_path:
                    ref_obj = object

            if ref_obj is None:
                from CatG.core.object import ContainerObject
                from CatG.core.asset import AssetManager
                ref_obj = AssetManager.load_assets(cached_path, ContainerObject)
                print(cached_path, "ssssssssss")
                print(ref_obj)

            variable_path: list[str] = ref_path[file_index:]
            target_obj = ref_obj
            final_obj = None
            for index, attr_name in enumerate(variable_path):
                if hasattr(target_obj, attr_name):
                    final_obj = getattr(target_obj, attr_name)

                    if isinstance(target_obj, (int, float, str, tuple)):
                        final_obj = lambda: getattr(target_obj, attr_name)
                        break

                    if index == len(variable_path) - 1:
                        break

                    target_obj = final_obj
                else:
                    raise ValueError("ㅉ")

            print(final_obj)
            return final_obj

        raise ValueError("주소 없다?")
