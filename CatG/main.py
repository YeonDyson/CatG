import sys
import pygame

from CatG.core.asset import AssetManager
from CatG.GameManager import GameManager
from CatG.core.level import LevelContainer


def main():
    pygame.init()
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    GameManager().initialize()
    level_manager = GameManager().level_manager

    # 나의 하드코딩을 알까?
    # assets/test/landscape.cntr
    # assets/level/main.cntr
    level = AssetManager.load_assets("assets/level/landscape.cntr", LevelContainer)
    print(level.__dict__)
    level_manager.load_level(level)
    level_manager.activate_level(level)

    running = True
    while running:
        delta_time = clock.tick(60) / 1000.0

        GameManager().events = pygame.event.get()
        GameManager().delta_time = delta_time

        for event in GameManager().events:
            if event.type == pygame.QUIT:
                running = False


        GameManager().key_event_manager.update()

        GameManager().screen.fill((0, 0, 0))
        level_manager.update()
        pygame.display.flip()

        pygame.display.set_caption(f"{clock.get_fps()}")

    pygame.quit()
    sys.exit()
    pass

if __name__ == '__main__':
    main()
