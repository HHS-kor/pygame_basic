import random
import pygame
##########################################################
pygame.init()  # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480  # 가로 480
screen_height = 640  # 세로 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Quiz")

# FPS
clock = pygame.time.Clock()
##########################################################

# 1.사용자 게임 초기화 (배경화면, 게임이미지,좌표,속도, 폰트 등)
background = pygame.image.load(
    "C:/Users/user/Documents/pygame_basic/background.png")

character = pygame.image.load(
    "C:/Users/user/Documents/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width/2)
character_y_pos = screen_height-character_height

to_x_L = 0
to_x_R = 0

character_speed = 0.5

ddong = pygame.image.load(
    "C:/Users/user/Documents/pygame_basic/enemy.png")
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_x_pos = random.randint(0, screen_width-ddong_width)
ddong_y_pos = 0
ddong_speed = 10

running = True  # 게임이 진행중임
while running:

    dt = clock.tick(60)  # fps설정

    # 2.이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는가?
            if event.key == pygame.K_LEFT:
                to_x_L -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x_R += character_speed

        if event.type == pygame.KEYUP:  # 키 떼면 멈춤
            if event.key == pygame.K_LEFT:
                to_x_L = 0
            elif event.key == pygame.K_RIGHT:
                to_x_R = 0

    # 3.캐릭터 위치 정의
    character_x_pos += (to_x_L+to_x_R)*dt
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width-character_width:
        character_x_pos = screen_width-character_width

    ddong_y_pos += ddong_speed

    if ddong_y_pos > screen_height:
        ddong_y_pos = 0
        ddong_x_pos = random.randint(0, screen_width-ddong_width)

    # 4.충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

    if character_rect.colliderect(ddong_rect):
        print("충돌")
        running = False

    # 5.화면에 그리기

    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos))

    pygame.display.update()  # 게임 화면 다시 그리기! (반드시 계속 호출되어야)

# 잠시대기
pygame.time.delay(1000)  # 2000ms 대기 (2초)

# pygame 종료
pygame.quit()
