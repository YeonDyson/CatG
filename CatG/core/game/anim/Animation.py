import pygame

from CatG.core.game import SpriteRender
from CatG.core.game.anim.AnimationClip import AnimationClip
from CatG.core.object import CScript
from CatG.core.object.container.ContainerObject import ContainerObject

class Animation(CScript):
    _sprite_rander: SpriteRender
    animation_clips: list[AnimationClip] = []
    current_clip: AnimationClip = None
    tasking_animation_task: 'Animation._AnimationTask' = None

    def on_enable(self):
        self._sprite_rander = self.gameObject.get_cscript(SpriteRender)
        print("tq")

        for clip in self.animation_clips:
            for frame in clip.frames:
                frame.image.on_enable()

    def pre_update(self):
        pass

    def update(self):
        pass

    def late_update(self):
        if not self.current_clip:
            return

        if self.tasking_animation_task:
            self.tasking_animation_task.update()

    def switch_clip(self, name: str):
        for clip in self.animation_clips:
            if clip.name == name:
                self.current_clip = clip

                if self.tasking_animation_task is None or self.tasking_animation_task.anim_clip != self.current_clip:
                    self.tasking_animation_task = self._AnimationTask(self.current_clip, self._sprite_rander)

                return

        print(f"뭐 그럴수도 있는데 대충 이건 오류인데 나는 오류 나는거 싫어하니깐 이딴거로 대체하는 그런 요오상한 프린트: 암튼 {name}라는 클립이 없는데 재대로 이름 한거 마자요?")

    class _AnimationTask:
        def __init__(self, anim_clip: AnimationClip, sprite_rander: SpriteRender):
            self.anim_clip = anim_clip
            self.current_index = 0
            self.last_update_time = pygame.time.get_ticks()
            self.sprite_rander = sprite_rander
            self._ahafwiq = False

            self.sprite_rander.image = self.anim_clip.frames[self.current_index].image

        def update(self):
            if self._ahafwiq:
                return

            current_time = pygame.time.get_ticks()

            if current_time - self.last_update_time >= self.anim_clip.frames[self.current_index].duration:
                self.last_update_time = current_time

                self.current_index += 1

                if self.current_index >= len(self.anim_clip.frames):
                    if self.anim_clip.loop:
                        self.current_index = 0
                    else:
                        self._ahafwiq = True
                        return

                self.sprite_rander.image = self.anim_clip.frames[self.current_index].image