import importlib
import inspect
import json
from typing import Type

from pygame import Vector2

from CatG.core.object import CObject, ContainerObject
from CatG.core.object.container.ContainerManager import ContainerManager
from CatG.core.serialization.CustomAdapter import CustomAdapter


# 코드가 이븐하게 익지 않앗석요

# def serialize_filed(cls):
#     if not isinstance(cls, type):
#         print("암튼 이건 예외임")
#         return
#
#     cls.serialize_filed = True


def serialize_adapter(*types):
    def decorator(adapter_class: Type[CustomAdapter]):
        if not issubclass(adapter_class, CustomAdapter):
            raise TypeError("어덥터 전용임 ㅅㄱ")

        adapter_instance = adapter_class()
        for type_ in types:
            Serializer.serializer_rule[type_] = adapter_instance
            print(type_)

        return adapter_class

    return decorator


class Serializer:
    serializer_rule: dict[type, CustomAdapter] = {}

    @staticmethod
    def serialize(cls):
        if isinstance(cls, type):
            Serializer.__class_serialize(cls)
        elif isinstance(cls, CObject):
            Serializer.__cobject_serialize(cls)

    @staticmethod
    def add_serializer_rule(name, rule):
        Serializer.serializer_rule[name] = rule

    @staticmethod
    def remove_serializer_rule(name):
        Serializer.serializer_rule.pop(name, None)

    @staticmethod
    def __class_serialize(cls: type):
        hasattr(cls, "serialize_filed")

    @staticmethod
    def __cobject_serialize(cls: CObject):
        """
        그러케 영원히 구현될 일은 없었다고 한다
        :param cls:
        :return:
        """
        pass

    @staticmethod
    def __load_ref(ref_path: str):
        pass

    @staticmethod
    def deserialize(json_str: str) -> ContainerObject:
        from CatG.core.object import CObjectManager
        def die(data_dict: dict, ref: dict = None) -> type:
            name, value = next(iter(data_dict.items()))
            # print(name, "|||", value)

            if meta_types.get(name) is None:
                raise ValueError("메타 재대로 명시하신거 마자요? 없는데?")

            if CObjectManager().is_cobject(name):
                cobject_instance = CObjectManager().instantiate_by_name(name)
                # print(cobject_instance.__dict__, "sibal")

                for _key, _value in value.items():
                    if not hasattr(cobject_instance, _key):
                        # print("sans")
                        continue

                    if ref is not None and _key in ref:
                        cobject_instance.__dict__[_key] = ContainerManager().ref_container(ref[_key])
                        continue

                    if isinstance(_value, dict):
                        _ref = None
                        if _value.get("$ref") is not None:
                            _ref = _value["$ref"]
                            _value.pop("$ref")

                        if not _value and _ref is not None:
                            cobject_instance.__dict__[_key] = ContainerManager().ref_container(_ref["obj"])
                            continue

                        __key, __value = next(iter(_value.items()))

                        if not meta_types.get(__key) is None:
                            cobject_instance.__dict__[_key] = die(_value, _ref)
                            continue

                    if isinstance(_value, list) and len(_value) > 0 and isinstance(_value[0], dict):
                        # if meta_types.get(next(iter(_value[0]), None)) is not None:
                        _objs = []

                        for _obj in _value:
                            if not isinstance(_obj, dict):
                                raise ValueError("나는 매우 깐깐해")

                            _ref = None
                            if _obj.get("$ref") is not None:
                                _ref = _obj["$ref"]
                                _obj.pop("$ref")

                            if not _obj and _ref is not None:
                                _objs.append(ContainerManager().ref_container(_ref["obj"]))
                                continue

                            if meta_types.get(next(iter(_obj), None)) is None:
                                raise ValueError("메타 하라고 명시 하라고", f": {_obj}")

                            _objs.append(die(_obj, _ref))

                        cobject_instance.__dict__[_key] = _objs
                        continue

                    cobject_instance.__dict__[_key] = _value

                # print(cobject_instance.__dict__)
                return cobject_instance

            module_path, class_name = meta_types.get(name).rsplit(".", 1)
            adapter = None
            for (name_, obj_) in inspect.getmembers(importlib.import_module(module_path), inspect.isclass):
                if class_name == name_:
                    adapter = Serializer.serializer_rule[obj_]

            assert adapter is not None, "없다"
            # print(adapter.from_dict(value))

            # if Serializer.serializer_rule.get() is  None:
            return adapter.from_dict(value)

        json_en: dict[str] = json.loads(json_str)

        meta_types: dict[str, str] = json_en["$types"]
        json_en.pop("$types")

        meta_ref = None
        if json_en.get("$ref") is not None:
            meta_ref = json_en["$ref"]
            json_en.pop("$ref")

        root_key = next(iter(json_en), None)
        if root_key is None or meta_types.get(root_key) is None:
            raise ValueError("저런")

        if not CObjectManager().is_cobject(root_key):
            raise ValueError("뒤질레")

        root_instance: ContainerObject = die(json_en, meta_ref)

        # print(root_instance.__dict__)
        # print(type(root_instance))
        # print(root_instance.prefab_gameObject.__dict__)
        return root_instance
