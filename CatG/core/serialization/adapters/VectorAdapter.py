from pygame import Vector2, Vector3

from CatG.core.serialization.CustomAdapter import CustomAdapter
from CatG.core.serialization.Serialize import serialize_adapter

@serialize_adapter(Vector2, Vector3)
class VectorAdapter(CustomAdapter):
    def to_dict(self, vector) -> dict:
        if isinstance(vector, Vector3):
            return {
                "x": vector.x,
                "y": vector.y,
                "z": vector.z
            }
        elif isinstance(vector, Vector2):
            return {
                "x": vector.x,
                "y": vector.y,
            }

        raise TypeError(f"Unsupported type {type(vector)}")


    def from_dict(self, data: dict):
        if data.get("z") is not None:
            return Vector3(data["x"], data["y"], data["z"])
        else:
            return Vector2(data["x"], data["y"])