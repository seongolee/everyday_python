import pygame

pygame.init()  # 초기화(반드시 필요)

# 화면 크기 설정
screen_width = 480  # 가로 길이
screen_height = 640  # 세로 길이
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado game")  # 게임 이름 설정

# 배경 이미지 불러오기
background = pygame.image.load("/Users/leesungo/PycharmProjects/everyday/pygame_basic/pygame_background.png/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("/Users/leesungo/PycharmProjects/everyday/pygame_basic/character.png")
character_size = character.get_rect().size  # 이미지의 크기를 가져옴
character_width = character_size[0]  # 캐릭터의 가로 크기
character_height = character_size[1]   # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2)  # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height  # 화면 세로 크기 가장 아래에 해당하는 곳에 위치


# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 255))
    # screen.blit(background, (0, 0))  # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update()  # 게임화면을 다시 그리기!

# pygame 종료
pygame.quit()