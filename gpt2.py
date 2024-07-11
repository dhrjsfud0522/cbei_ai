import pygame
import random

# Pygame 초기화
pygame.init()

# 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jump to Avoid Obstacles")

# 색상 정의
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# 게임 설정
clock = pygame.time.Clock()
running = True

# 점수 설정
score = 0
font = pygame.font.SysFont(None, 55)

def display_score(score):
    text = font.render(f"Score: {score}", True, black)
    screen.blit(text, [10, 10])

# 플레이어 클래스
class Player:
    def __init__(self):
        self.size = 50
        self.x = 100
        self.y = screen_height - self.size
        self.y_velocity = 0
        self.jump_force = 15
        self.gravity = 1

    def jump(self):
        if self.y == screen_height - self.size:
            self.y_velocity = -self.jump_force

    def move(self):
        self.y_velocity += self.gravity
        self.y += self.y_velocity
        if self.y > screen_height - self.size:
            self.y = screen_height - self.size
            self.y_velocity = 0

    def draw(self):
        pygame.draw.rect(screen, black, [self.x, self.y, self.size, self.size])

# 장애물 클래스
class Obstacle:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = screen_width
        self.y = screen_height - self.height
        self.speed = 10

    def move(self):
        self.x -= self.speed
        if self.x < -self.width:
            self.x = screen_width
            global score
            score += 1

    def draw(self):
        pygame.draw.rect(screen, red, [self.x, self.y, self.width, self.height])

    def check_collision(self, player):
        if player.x < self.x + self.width and player.x + player.size > self.x and player.y + player.size > self.y:
            return True
        return False

# 인스턴스 생성
player = Player()
obstacle = Obstacle()

# 게임 루프
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()

    # 플레이어와 장애물 이동
    player.move()
    obstacle.move()

    # 충돌 감지
    if obstacle.check_collision(player):
        running = False

    # 화면 그리기
    screen.fill(white)
    player.draw()
    obstacle.draw()
    display_score(score)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
