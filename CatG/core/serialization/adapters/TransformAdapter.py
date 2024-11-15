from pygame import Vector2

from CatG.core.game import Transform
from CatG.core.serialization import CustomAdapter
from CatG.core.serialization.Serialize import serialize_adapter


@serialize_adapter(Transform)
class TransformAdapter(CustomAdapter):
    def to_dict(self, obj) -> dict:
        pass

    def from_dict(self, data: dict):
        transform = Transform()
        transform.position = Vector2(data["position"]["Vector2"]["x"], data["position"]["Vector2"]["y"])

        if data.get("flip_x"):
            transform.flip_x = data["flip_x"]

        if data.get("flip_y"):
            transform.flip_y = data["flip_y"]

        if data.get("rotation"):
            transform.rotation = data["rotation"]

        if data.get("scale"):
            transform.scale = Vector2(data["scale"]["Vector2"]["x"], data["scale"]["Vector2"]["y"])

        # self.flip_x = False
        # self.flip_y = False
        # self.rotation = 0
        # self.scale = Vector2(1, 1)

        return transform