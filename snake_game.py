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
sprites = [
    apple, head_right, head_left, head_down, head_up,
    body_bottomleft, body_bottomright, body_vertical,
    body_horizontal, body_topleft, body_topright,
    tail_down, tail_up, tail_left, tail_right
]

for i in range(len(sprites)):
    sprites[i] = pygame.transform.scale(sprites[i], (CELL, CELL))

(
    apple, head_right, head_left, head_down, head_up,
    body_bottomleft, body_bottomright, body_vertical,
    body_horizontal, body_topleft, body_topright,
    tail_down, tail_up, tail_left, tail_right
) = sprites


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


def get_head_sprite(d):
    if d == 'd':
        return head_right
    elif d == 'a':
        return head_left
    elif d == 'w':
        return head_up
    return head_down


def get_tail_sprite(cobra):
    tx, ty = cobra[-1]
    px, py = cobra[-2]

    if px > tx:
        return tail_left
    elif px < tx:
        return tail_right
    elif py > ty:
        return tail_up
    return tail_down


def get_body_sprite(cobra, i):
    x, y = cobra[i]
    prev_x, prev_y = cobra[i - 1]
    next_x, next_y = cobra[i + 1]

    if prev_y == y and next_y == y:
        return body_horizontal

    elif prev_x == x and next_x == x:
        return body_vertical

    elif (
        (prev_x < x and next_y < y) or
        (next_x < x and prev_y < y)
    ):
        return body_topleft

    elif (
        (prev_x > x and next_y < y) or
        (next_x > x and prev_y < y)
    ):
        return body_topright

    elif (
        (prev_x < x and next_y > y) or
        (next_x < x and prev_y > y)
    ):
        return body_bottomleft

    return body_bottomright


def desenhar():
    screen.fill((0, 0, 0))

    for i, (x, y) in enumerate(cobra):
        px = x * CELL
        py = y * CELL

        if i == 0:
            sprite = get_head_sprite(direcao)

        elif i == len(cobra) - 1:
            sprite = get_tail_sprite(cobra)

        else:
            sprite = get_body_sprite(cobra, i)

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
