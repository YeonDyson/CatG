import sys
import pygame

from CatG.core.asset import PrefabContainer, AssetManager
from CatG.core.object import CObjectManager


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    CObjectManager()
    # test start
    AssetManager.load_assets("assets/test/refTest", PrefabContainer)

    # test end

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        screen.fill((0, 0, 0))

        pygame.display.flip()


        clock.tick(60)

    pygame.quit()
    sys.exit()
    pass

if __name__ == '__main__':
    main()
