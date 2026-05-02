import pygame
import snake

pygame.init()

CELL = 64

screen = pygame.display.set_mode((640, 640))

head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()
head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()

apple = pygame.image.load('Graphics/apple.png').convert_alpha()

cobra = [(0,1),(0,0)]
frutas = [(2,2)]
direcao = 'd'

clock = pygame.time.Clock()
loop = True


while loop:

    screen.fill((0,0,0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            loop = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                direcao = 'd'
            elif event.key == pygame.K_LEFT:
                direcao = 'a'
            elif event.key == pygame.K_UP:
                direcao = 'w'
            elif event.key == pygame.K_DOWN:
                direcao = 's'

    cobra, frutas, colidiu = snake.movimentacao(cobra, direcao, frutas)

    for i, (x,y) in enumerate(cobra):
        if i == 0:
            screen.blit(head_right, (x*CELL,y*CELL))

    for fx, fy in frutas:
        screen.blit(apple, (fx*CELL, fy*CELL))

    pygame.display.flip()
    clock.tick(4)

pygame.quit()
