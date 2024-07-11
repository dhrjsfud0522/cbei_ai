import pygame
import random
import os

pygame.init()

sc_w = 800
sc_h = 600
screen = pygame.display.set_mode((sc_w, sc_h))
pygame.display.set_caption('game')
clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, "assets")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

score = 0
font = pygame.font.SysFont(None, 55)

def display_score(score):
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, [10, 10])

class Player:
    def __init__(self):
        self.img = pygame.image.load(os.path.join(assets_path, 'dino.png'))
        self.w = self.img.get_rect().width
        self.h = self.img.get_rect().height
        self.x = 100
        self.y = sc_h - self.h
        self.v = 0
        self.jump_force = 15
        self.g = 1

    def jump(self):
        if self.y == sc_h - self.h:
            self.v = - self.jump_force

    def move(self):
        self.v += self.g
        self.y += self.v
        if self.y > sc_h - self.h:
            self.y = sc_h - self.h
            self.v = 0

    def draw(self):
        screen.blit(self.img, [self.x, self.y])

class Obstacle:
    def __init__(self):
        self.w = 50
        self.h = 50
        self.x = sc_w
        self.y = sc_h - self.h
        self.speed = 15
    
    def move(self):
        global score
        self.x -= self.speed
        if self.x < -self.w:
            self.x = sc_w
            score += 1

    def draw(self):
        pygame.draw.rect(screen, RED, [self.x, self.y, self.w, self.h])

    def check_collision(self, player):
        if player.x < self.x + self.w and player.x + player.w > self.x and player.y + player.h > self.y:
            return True
        return False
    
player = Player()
obstacle = Obstacle()

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()
        
        player.move()
        obstacle.move()

        if obstacle.check_collision(player):
            running = False

        screen.fill(WHITE)
        player.draw()
        obstacle.draw()
        display_score(score)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

main()