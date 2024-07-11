import pygame
import random

pygame.init()

sc_w = 800
sc_h = 600
screen = pygame.display.set_mode((sc_w, sc_h))
pygame.display.set_caption("game")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# 플레이어 설정
player_size = 50
player_x = 100
player_y = sc_h - player_size
player_y_velocity = 0
jump_force = 15
gravity = 1

# 장애물 설정
obstacle_width = 50
obstacle_height = 50
obstacle_x = sc_w
obstacle_y = sc_h - obstacle_height
obstacle_speed = 10

# 게임 루프 설정
clock = pygame.time.Clock()
running = True

# 점수 설정
score = 0
font = pygame.font.SysFont(None, 55)

def display_score(score):
    text = font.render(f"Score: {score}", True, black)
    screen.blit(text, [10, 10])

# 게임 루프
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_y == sc_h - player_size:
                player_y_velocity = -jump_force

    # 플레이어 중력 적용 및 위치 업데이트
    player_y_velocity += gravity
    player_y += player_y_velocity

    # 플레이어가 바닥에 닿으면 위치 고정
    if player_y > sc_h - player_size:
        player_y = sc_h - player_size
        player_y_velocity = 0

    # 장애물 이동 및 화면 밖으로 나가면 초기화
    obstacle_x -= obstacle_speed
    if obstacle_x < -obstacle_width:
        obstacle_x = sc_w
        score += 1

    # 충돌 감지
    if player_x < obstacle_x + obstacle_width and player_x + player_size > obstacle_x and player_y + player_size > obstacle_y:
        running = False

    # 화면 그리기
    screen.fill(white)
    pygame.draw.rect(screen, black, [player_x, player_y, player_size, player_size])
    pygame.draw.rect(screen, red, [obstacle_x, obstacle_y, obstacle_width, obstacle_height])
    display_score(score)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()