import os
import keyboard
import time
import random


class io_handler:

    def __init__(self, dim, speed):
        self.x_size = dim[0]
        self.y_size = dim[1]
        self.game_speed = speed
        self.last_input = 'd'
        self.matrix = [[0] * self.x_size for _ in range(self.y_size)]

    
    def try_set(self, new_dir):
        oposto = {
        'w': 's',
        's': 'w',
        'a': 'd',
        'd': 'a'
    }

        if new_dir != oposto.get(self.last_input):
            self.last_input = new_dir    
    
    def record_inputs(self):
        keyboard.add_hotkey('w', lambda: self.try_set('w'))
        keyboard.add_hotkey('s', lambda: self.try_set('s'))
        keyboard.add_hotkey('a', lambda: self.try_set('a'))
        keyboard.add_hotkey('d', lambda: self.try_set('d'))
        keyboard.add_hotkey('esc', lambda: setattr(self, "last_input", 'end'))
        

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        print('+' + '--' * self.x_size + '+')
        for line in self.matrix:
            print('|', end='')
            for item in line:
                if item == 1:
                    print('[]', end='')
                elif item == 2:
                    print('<>', end='')
                elif item == 3:
                    print('()', end='')
                else:
                    print('  ', end='')
            print('|')
        print('+' + '--' * self.x_size + '+')


instance = io_handler((10, 10), 0.5)

cobra = [(0, 1), (0, 0)]
frutas = [(2, 2)]




def gera_posicao_valida(cobra, frutas):
    tentativas = 0

    while tentativas < 100:
        pos = (random.randint(0, 9), random.randint(0, 9))

        if pos not in cobra and pos not in frutas:
            return pos

        tentativas += 1

    return None


def gera_fruta(cobra, frutas):
    quantidade = 2 if len(cobra) % 10 == 0 else 1

    for _ in range(quantidade):
        pos = gera_posicao_valida(cobra, frutas)
        if pos:
            frutas.append(pos)

    return frutas



def movimentacao(cobra, direcao, frutas):
    x, y = cobra[0]

    movimentos = {
        'w': (0, -1),
        's': (0, 1),
        'a': (-1, 0),
        'd': (1, 0)
    }

    if direcao not in movimentos:
        return cobra, frutas, False

    dx, dy = movimentos[direcao]

    nova_x = (x + dx) % 10
    nova_y = (y + dy) % 10

    nova_cabeca = (nova_x, nova_y)

    
    if nova_cabeca in cobra:
        return cobra, frutas, True

    
    comeu = nova_cabeca in frutas

    cobra.insert(0, nova_cabeca)

    if comeu:
        frutas.remove(nova_cabeca)
        frutas = gera_fruta(cobra, frutas)
    else:
        cobra.pop()

    return cobra, frutas, False


def render(cobra, frutas):
    matrix = [[0] * 10 for _ in range(10)]

    for i, (x, y) in enumerate(cobra):
        if 0 <= x < 10 and 0 <= y < 10:
            matrix[y][x] = 2 if i == 0 else 1

    for x, y in frutas:
        if 0 <= x < 10 and 0 <= y < 10:
            matrix[y][x] = 3

    return matrix



def game_loop():
    instance.record_inputs()

    global cobra, frutas

    colidiu = False

    while not colidiu:

        if instance.last_input == 'end':
            break

        cobra, frutas, colidiu = movimentacao(
            cobra,
            instance.last_input,
            frutas
        )

        instance.matrix = render(cobra, frutas)

        instance.display()

        print("Ultimo input:", instance.last_input)

        time.sleep(instance.game_speed)


if __name__ == "__main__":
    game_loop()
