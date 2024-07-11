import pygame

SC_W = 800
SC_H = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
pygame.display.set_caption("pygame")
screen = pygame.display.set_mode((SC_W, SC_H))
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(RED)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()