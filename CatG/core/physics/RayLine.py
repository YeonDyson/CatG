from collections.abc import Callable

import pygame
from pygame import Vector2

from CatG.core.level import Level
from CatG.core.object import GameCObject
from CatG.core.physics.Collider import Collider


class RayLine:
    def __init__(self, origin: Vector2, direction: Vector2, length: int, func: Callable, level: Level, ignore_object: GameCObject = None):
        self.origin = origin
        self.direction = direction
        self.length = length
        self.func = func
        self.level = level
        self.ignore_object = ignore_object

        self.ray()

    def ray(self):
        direction = self.direction.normalize()

        ray_surface = pygame.Surface((self.length * 2, self.length * 2), pygame.SRCALPHA)
        ray_surface = ray_surface.convert_alpha()

        end_point = self.origin + direction * self.length
        pygame.draw.line(ray_surface, (255, 255, 255), (self.length, self.length), (end_point.x, end_point.y), 1)

        ray_mask = pygame.mask.from_surface(ray_surface)
        self.__ray_collide(ray_mask)

    def __ray_collide(self, ray_mask: pygame.mask):
        ray_world_position = Vector2(self.origin.x - self.length / 2, self.origin.y + self.length / 2)

        for gameObject in self.level.get_game_objects_by_script(Collider):
            if gameObject == self.ignore_object:
                continue

            collider = gameObject.get_cscript(Collider)

            offset = collider.get_position() - ray_world_position
            offset.x = -offset.x

            if collider.get_mask().overlap(ray_mask, offset):
                self.func(gameObject)