import pygame

# 초기화

pygame.init()
screen_width = 1280 # 가로 크기
screen_height = 720 # 세로 크기

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Memory Game")

# 게임 루프 만들기


running = True  # 현재 게임 실행 상태

while running :
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT : # 창이 닫히는 이벤트
            running = False # 게임이 실행 중이 아니다.
# 게임 종료
pygame.quit()