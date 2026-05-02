import pygame

pygame.init()

screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Snake")

head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()

clock = pygame.time.Clock()

x = 64
y = 64
loop = True

while loop:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    screen.blit(head_right, (x, y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
