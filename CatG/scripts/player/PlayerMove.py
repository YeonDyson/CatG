import pygame
from pygame import Vector2

from CatG.GameManager import GameManager
from CatG.core.event.Listener import Listener
from CatG.core.event.key.KeyEventManager import KeyEventManager, InputType, KeyEvent
from CatG.core.game import SpriteRender, Transform
from CatG.core.game.anim.Animation import Animation
from CatG.core.object import CScript
from CatG.core.physics.PhysicsBody import PhysicsBody, BodyType
from CatG.core.physics.RayLine import RayLine


class PlayerMove(CScript, Listener):
    _physics_body: PhysicsBody = None
    _last_velocity: Vector2 = Vector2(0, 0)
    _sprite_render: SpriteRender = None
    _animation: Animation = None
    _transform: Transform = None

    def on_enable(self):
        GameManager().key_event_manager.register_listener(self)
        self._physics_body = self.gameObject.get_cscript(PhysicsBody)

        print(self._physics_body.body_type)
        print(BodyType.DYNAMIC)

        self._sprite_render = self.gameObject.get_cscript(SpriteRender)
        self._animation = self.gameObject.get_cscript(Animation)
        self._transform = self.gameObject.transform


    def on_destroy(self):
        GameManager().key_event_manager.unregister_listener(self)

    def pre_update(self):
        pass

    def update(self):
        pass
    #     RayLine(self.gameObject.transform.position, Vector2(0, 1), 3, self.sans, self.gameObject._level, self.gameObject)
    #
    # def sans(self, a):
    #     print(a.name, "aaaaaaaaa")

    def late_update(self):
        if self._physics_body.velocity == Vector2(0, 0):
            if self._last_velocity.x > 0:
                self._animation.switch_clip("player_idle_side")
                self._transform.flip_x = True
            elif self._last_velocity.x < 0:
                self._animation.switch_clip("player_idle_side")
                self._transform.flip_x = False
            elif self._last_velocity.y > 0:
                self._animation.switch_clip("player_idle_back")
            elif self._last_velocity.y < 0:
                self._animation.switch_clip("player_idle")
        else:
            if self._physics_body.velocity.x > 0:
                self._animation.switch_clip("player_walk_side")
                self._transform.flip_x = True
            elif self._physics_body.velocity.x < 0:
                self._animation.switch_clip("player_walk_side")
                self._transform.flip_x = False
            elif self._physics_body.velocity.y > 0:
                self._animation.switch_clip("player_walk_back")
            elif self._physics_body.velocity.y < 0:
                self._animation.switch_clip("player_walk")

            self._physics_body.velocity = Vector2(0, 0)

    @KeyEventManager.on_key(InputType.PRESSED, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)
    def move(self, event: KeyEvent):
        velocity = Vector2(0, 0)

        if pygame.K_UP in event.keys:
            velocity.y += 1
        if pygame.K_DOWN in event.keys:
            velocity.y -= 1
        if pygame.K_LEFT in event.keys:
            velocity.x -= 1
        if pygame.K_RIGHT in event.keys:
            velocity.x += 1

        if velocity != Vector2(0, 0):
            self._last_velocity = velocity

        self._physics_body.velocity = velocity