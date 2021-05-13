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

# 이벤트 loop
running = True  # 게임이 진행중임
while running:
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생? (X누르기)
            running = False  # 게임이 진행중이 아님
    screen.blit(background, (0, 0))  # 배경 그리기
    # screen.fill((0, 0, 255)) #RGB
    pygame.display.update()  # 게임 화면 다시 그리기! (반드시 계속 호출되어야)

# pygame 종료
pygame.quit()
