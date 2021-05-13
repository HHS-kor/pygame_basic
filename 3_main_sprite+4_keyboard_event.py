import pygame

pygame.init()  # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480  # 가로 480
screen_height = 640  # 세로 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")

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

# 이벤트 loop
running = True  # 게임이 진행중임
while running:
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생? (X누르기)
            running = False  # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는가?
            if event.key == pygame.K_LEFT:
                to_x_L -= 0.5
            elif event.key == pygame.K_RIGHT:
                to_x_R += 0.5
            elif event.key == pygame.K_UP:
                to_y -= 0.5
            elif event.key == pygame.K_DOWN:
                to_y += 0.5

        if event.type == pygame.KEYUP:  # 키 떼면 멈춤
            if event.key == pygame.K_LEFT:
                to_x_L = 0
            elif event.key == pygame.K_RIGHT:
                to_x_R = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x_L+to_x_R
    character_y_pos += to_y

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

    screen.blit(background, (0, 0))  # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기

    pygame.display.update()  # 게임 화면 다시 그리기! (반드시 계속 호출되어야)

# pygame 종료
pygame.quit()
