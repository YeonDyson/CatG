import sys
import pygame
from CatG.core.object import CObjectManager


def main():
    # 1. 초기화
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    CObjectManager()

    # 2. 게임 루프
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # 기타 이벤트 처리 (예: 키보드, 마우스)

        # 게임 상태 업데이트
        # 모든 게임 오브젝트들의 update() 호출

        # 화면 렌더링
        screen.fill((0, 0, 0))  # 화면 초기화 (검은색으로 채움)
        # 모든 게임 오브젝트들의 draw() 호출
        pygame.display.flip()

        # 프레임 속도 유지
        clock.tick(60)

    # 3. 종료 처리
    pygame.quit()
    sys.exit()
    pass

if __name__ == '__main__':
    main()