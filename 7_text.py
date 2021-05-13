import pygame

pygame.init()  # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480  # 가로 480
screen_height = 640  # 세로 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load(
    "C:\\Users\\user\\Documents\\pygame_basic\\background.png")  # 탈출문자 \\ or /

# 스프라이트(캐릭터) 불러오기
character = pygame.image.load(
    "C:\\Users\\user\\Documents\\pygame_basic\\character.png")
character_size = character.get_rect().size  # 이미지의 크기를 구해옴
character_width = character_size[0]  # 가로
character_height = character_size[1]  # 세로
character_x_pos = (screen_width / 2) - \
    (character_width/2)  # 화면 가로의 절반 위치 - 캐릭터 가로의 절반
character_y_pos = screen_height - character_height  # 화면 세로 가장 아래 위치 - 캐릭터 세로

# 이동할 좌표
to_x_L = 0
to_x_R = 0
to_y = 0

# 이동속도
character_speed = 0.6

# 적 캐릭터
enemy = pygame.image.load(
    "C:\\Users\\user\\Documents\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size  # 이미지의 크기를 구해옴
enemy_width = enemy_size[0]  # 가로
enemy_height = enemy_size[1]  # 세로
enemy_x_pos = (screen_width / 2) - (enemy_width/2)  # 화면 가로의 절반 위치 - 캐릭터 가로의 절반
enemy_y_pos = (screen_height / 2) - (enemy_height/2)  # 화면 세로 가장 아래 위치 - 캐릭터 세로

# 폰트 정의
game_font = pygame.font.Font(None, 40)  # 폰트 객체 생성 (폰트, 크기)

# 총시간
total_time = 10

# 시작 시간 정보
start_ticks = pygame.time.get_ticks()  # 시작 tick을 받아옴

# 이벤트 loop
running = True  # 게임이 진행중임
while running:

    dt = clock.tick(60)  # fps설정

    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생? (X누르기)
            running = False  # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는가?
            if event.key == pygame.K_LEFT:
                to_x_L -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x_R += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:  # 키 떼면 멈춤
            if event.key == pygame.K_LEFT:
                to_x_L = 0
            elif event.key == pygame.K_RIGHT:
                to_x_R = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += (to_x_L+to_x_R) * dt  # 프레임에 따라 이속 보정
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width-character_width:
        character_x_pos = screen_width-character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height-character_height:
        character_y_pos = screen_height-character_height

    # 충돌 처리 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌")
        running = False

    screen.blit(background, (0, 0))  # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기

    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))  # 적 그리기

    # 경과시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000  # ms -> s

    # 타이머 넣기
    timer = game_font.render(
        str(int(total_time-elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))

    # 시간이 0이면 게임 종료
    if total_time - elapsed_time <= 0:
        print("timeout")
        running = False

    pygame.display.update()  # 게임 화면 다시 그리기! (반드시 계속 호출되어야)

# 잠시대기
pygame.time.delay(2000)  # 2000ms 대기 (2초)

# pygame 종료
pygame.quit()
