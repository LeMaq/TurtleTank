""" Modulo com as funcoes da fisica do jogo, exemplo: colisoes """
from random import randint
import turtle


def collision_bullet_tank(x_tank, y_tank, x_ball, y_ball):
    if x_ball >= x_tank - 5 and x_ball <= x_tank + 35:
        if y_ball <= y_tank + 5 and y_ball >= y_tank - 34.29:
            return True
        else:
            return False
    return False


# Funcao que pega a posicao do canhao do tanque
def cannon_position(posx, posy, color, sprite):

    x = posx
    y = posy

    tanque = open(sprite, "r")
    for _i in range(27):
        largura = tanque.readline()
        for j in range(len(largura)):
            if largura[j] == '2':
                return x, y
            x += 2.5
        x = posx
        y -= 5


# verifica se o canhao do tanque toca um obstaculo
# se toca o tanque nao pode ir para frente
# essa funcao vai retornar pra funcao de fazer o tannque mover para frente
# o tanque so vai mover pra frente se for True
def can_move_forward(tank_pos_x, tank_pos_y, color, sprite):
    x_cannon, y_cannon = cannon_position(tank_pos_x, tank_pos_y, color, sprite)
    # Obstáculos do mapa 2

    # obstáculo 1
    if ((x_cannon >= -285.61 and x_cannon <= -200.4 and
         y_cannon <= 79.61 and y_cannon >= 44.34) or
        (x_cannon >= -244.7 and x_cannon <= -200.4 and
         y_cannon <= 79.61 and y_cannon >= -145.37) or
        (x_cannon >= -285.61 and x_cannon <= -200.4 and
         y_cannon <= -110.1 and y_cannon >= -145.37)):
        return False

    # obstáculo 2
    if (x_cannon >= -139.24 and x_cannon <= -29.24 and
            y_cannon <= 2.08 and y_cannon >= -70.05):
        return False

    # obstáculo 3
    if (x_cannon >= 24.24 and x_cannon <= 139.24 and
            y_cannon <= 2.08 and y_cannon >= -70.05):
        return False

    # obstáculo 4
    if (x_cannon >= -34.88 and x_cannon <= 34.88 and
            y_cannon <= 109.13 and y_cannon >= -2.20):
        return False

    # obstáculo 5
    if (x_cannon >= -34.88 and x_cannon <= 34.88 and
            y_cannon <= -45.05 and y_cannon >= -167.3):
        return False

    # obstáculo 6
    if ((x_cannon >= 200.4 and x_cannon <= 280.61 and
         y_cannon <= 79.61 and y_cannon >= 44.34) or
        (x_cannon >= 200.4 and x_cannon <= 244.7 and
         y_cannon <= 79.61 and y_cannon >= -145.37) or
        (x_cannon >= 200.4 and x_cannon <= 280.61 and
         y_cannon <= -110.1 and y_cannon >= -145.37)):
        return False

    return True


def tank_spawn():
    spawn_points = [[-150, 90], [-150, -90], [150, 90], [150, -90]]
    selected = randint(0, len(spawn_points) - 1)
    point = spawn_points[selected]
    return point[0], point[1]
