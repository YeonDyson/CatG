from itertools import combinations

from pygame import Vector2

from CatG.core.object import CScript
from CatG.core.physics.PhysicsBody import PhysicsBody


class PixelPhysics(CScript):
    physics_bodies: list[PhysicsBody] = []

    def on_enable(self):
        game_objects = self.gameObject._level.get_game_objects_by_script(PhysicsBody)

        print(game_objects, "tqfusdk")
        for game_object in game_objects:
            self.physics_bodies.append(game_object.get_cscript(PhysicsBody))

    def pre_update(self):
        pass

    def update(self):
        for body in self.physics_bodies:
            if body.velocity == Vector2(0, 0):
                continue

            self.step(body)

        self.update_position()
        self.trigger_colliding()

    def late_update(self):
        pass

    def step(self, body: PhysicsBody):
        position = body._collider.get_position().copy()
        velocity = body.velocity.copy()

        count_velocity = Vector2(0, 0)
        f_velocity = Vector2(0, 0)
        while velocity != count_velocity:
            if velocity.x != count_velocity.x:
                count_velocity.x += 1 if velocity.x > 0 else -1
                f_velocity.x += 1 if velocity.x > 0 else -1

                if self.is_colliding(body, f_velocity):
                    f_velocity.x -= 1 if velocity.x > 0 else -1

            if velocity.y != count_velocity.y:
                count_velocity.y += 1 if velocity.y > 0 else -1
                f_velocity.y += 1 if velocity.y > 0 else -1

                if self.is_colliding(body, f_velocity):
                    f_velocity.y -= 1 if velocity.y > 0 else -1

        # print(f_velocity)

        body.velocity = f_velocity

    def update_position(self):
        for physics_body in self.physics_bodies:
            # if physics_body.body_type == BodyType.DYNAMIC:
            #     continue

            physics_body.gameObject.transform.position += physics_body.velocity

    def is_colliding(self, body: PhysicsBody, velocity: Vector2 = None) -> bool:
        target_collider = body._collider

        for physics_body in self.physics_bodies:
            if physics_body == body:
                continue

            if physics_body._collider.trigger:
                continue

            _collider = physics_body._collider

            offset = _collider.get_position() - (target_collider.get_position() + velocity)
            offset.x = -offset.x


            if _collider.get_mask().overlap(target_collider.get_mask(), offset):
                return True

        return False

    def trigger_colliding(self):
        trigger_bodies = [body for body in self.physics_bodies if body._collider.trigger]

        for body in self.physics_bodies:
            body_collider = body._collider

            for trigger_body in trigger_bodies:
                if body == trigger_body:
                    continue
                trigger_body_collider = trigger_body._collider

                offset = body_collider.get_position() - trigger_body_collider.get_position()
                offset.x = -offset.x

                if body_collider.get_mask().overlap(trigger_body_collider.get_mask(), offset):
                    pass
