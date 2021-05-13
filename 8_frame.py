import pygame
##########################################################
pygame.init()  # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480  # 가로 480
screen_height = 640  # 세로 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")

# FPS
clock = pygame.time.Clock()
##########################################################

# 1.사용자 게임 초기화 (배경화면, 게임이미지,좌표,속도, 폰트 등)

running = True  # 게임이 진행중임
while running:

    dt = clock.tick(30)  # fps설정

    # 2.이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3.캐릭터 위치 정의

    # 4. 충돌 처리

    # 5.화면에 그리기

    pygame.display.update()  # 게임 화면 다시 그리기! (반드시 계속 호출되어야)

# 잠시대기
pygame.time.delay(2000)  # 2000ms 대기 (2초)

# pygame 종료
pygame.quit()
