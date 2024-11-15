from pygame import Vector2


class Transform:
    def __init__(self):
        self.position: Vector2 = Vector2(0, 0)
        self.flip_x = False
        self.flip_y = False
        self.rotation = 0
        self.scale = Vector2(1, 1)