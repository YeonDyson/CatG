import pygame

from pygame_gui.elements import UIButton, UILabel, UIImage

from CatG.core.asset import AssetManager
from CatG.core.gui.Canvas import Canvas


class MainUI(Canvas):

    def on_enable(self):
        pass

    def setup_elements(self):
        # 황금비율 위치 계산
        screen_width, screen_height = pygame.display.get_surface().get_size()
        logo = AssetManager.load_image("assets/sprite/gui/logo.png")

        # UIImage로 로고 이미지 표시
        logo_ui = UIImage(
            relative_rect=pygame.Rect((10, 10), logo.get_size()),
            image_surface=logo,
            manager=self.ui_manager
        )

        # UIImage를 elements 리스트에 추가하여 관리
        self.elements.append(logo_ui)

        self.elements.extend([])

    def update(self):
        super().update()