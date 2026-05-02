import pygame

pygame.init()

screen = pygame.display.set_mode((640, 640))

head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()
head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()

clock = pygame.time.Clock()

x = 64
y = 64
step = 64

sprite = head_right

loop = True

while loop:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            loop = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                x += step
                sprite = head_right

            elif event.key == pygame.K_LEFT:
                x -= step
                sprite = head_left

            elif event.key == pygame.K_UP:
                y -= step
                sprite = head_up

            elif event.key == pygame.K_DOWN:
                y += step
                sprite = head_down

    screen.blit(sprite, (x, y))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
