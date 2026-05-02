import pygame
import snake

pygame.init()

CELL = 64
GRID = 10

screen = pygame.display.set_mode((CELL * GRID, CELL * GRID))
pygame.display.set_caption("Snake")

# Assets
apple = pygame.image.load('Graphics/apple.png').convert_alpha()

head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()
head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()

body_bottomleft = pygame.image.load('Graphics/body_bottomleft.png').convert_alpha()
body_bottomright = pygame.image.load('Graphics/body_bottomright.png').convert_alpha()
body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()
body_topleft = pygame.image.load('Graphics/body_topleft.png').convert_alpha()
body_topright = pygame.image.load('Graphics/body_topright.png').convert_alpha()

tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()
tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()

# Escala
apple = pygame.transform.scale(apple, (CELL, CELL))

head_right = pygame.transform.scale(head_right, (CELL, CELL))
head_left = pygame.transform.scale(head_left, (CELL, CELL))
head_down = pygame.transform.scale(head_down, (CELL, CELL))
head_up = pygame.transform.scale(head_up, (CELL, CELL))

body_bottomleft = pygame.transform.scale(body_bottomleft, (CELL, CELL))
body_bottomright = pygame.transform.scale(body_bottomright, (CELL, CELL))
body_vertical = pygame.transform.scale(body_vertical, (CELL, CELL))
body_horizontal = pygame.transform.scale(body_horizontal, (CELL, CELL))
body_topleft = pygame.transform.scale(body_topleft, (CELL, CELL))
body_topright = pygame.transform.scale(body_topright, (CELL, CELL))

tail_down = pygame.transform.scale(tail_down, (CELL, CELL))
tail_up = pygame.transform.scale(tail_up, (CELL, CELL))
tail_left = pygame.transform.scale(tail_left, (CELL, CELL))
tail_right = pygame.transform.scale(tail_right, (CELL, CELL))

cobra = [(0, 1), (0, 0)]
frutas = [(2, 2)]
direcao = 'd'

clock = pygame.time.Clock()
loop = True
colidiu = False


def try_set(nova_dir):
    global direcao

    oposto = {
        'w': 's',
        's': 'w',
        'a': 'd',
        'd': 'a'
    }

    if nova_dir != oposto[direcao]:
        direcao = nova_dir


def desenhar():
    screen.fill((0, 0, 0))

    for i, (x, y) in enumerate(cobra):
        px = x * CELL
        py = y * CELL

        # Cabeça
        if i == 0:
            if direcao == 'd':
                sprite = head_right
            elif direcao == 'a':
                sprite = head_left
            elif direcao == 'w':
                sprite = head_up
            else:
                sprite = head_down

        # Cauda
        elif i == len(cobra) - 1:
            tx, ty = cobra[i]
            px2, py2 = cobra[i - 1]

            if px2 > tx:
                sprite = tail_left
            elif px2 < tx:
                sprite = tail_right
            elif py2 > ty:
                sprite = tail_up
            else:
                sprite = tail_down

        # Corpo
        else:
            prev_x, prev_y = cobra[i - 1]
            next_x, next_y = cobra[i + 1]

            if prev_y == y and next_y == y:
                sprite = body_horizontal

            elif prev_x == x and next_x == x:
                sprite = body_vertical

            elif (
                (prev_x < x and next_y < y) or
                (next_x < x and prev_y < y)
            ):
                sprite = body_topleft

            elif (
                (prev_x > x and next_y < y) or
                (next_x > x and prev_y < y)
            ):
                sprite = body_topright

            elif (
                (prev_x < x and next_y > y) or
                (next_x < x and prev_y > y)
            ):
                sprite = body_bottomleft

            else:
                sprite = body_bottomright

        screen.blit(sprite, (px, py))

    for fx, fy in frutas:
        screen.blit(apple, (fx * CELL, fy * CELL))

    pygame.display.flip()


while loop and not colidiu:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            loop = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                try_set('d')

            elif event.key == pygame.K_LEFT:
                try_set('a')

            elif event.key == pygame.K_UP:
                try_set('w')

            elif event.key == pygame.K_DOWN:
                try_set('s')

            elif event.key == pygame.K_ESCAPE:
                loop = False

    cobra, frutas, colidiu = snake.movimentacao(
        cobra,
        direcao,
        frutas
    )

    desenhar()

    clock.tick(4)

pygame.quit()
