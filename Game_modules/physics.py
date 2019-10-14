""" Modulo com as funcoes da fisica do jogo, exemplo: colisoes """
import turtle


def collision_bullet_tank(x_tank, y_tank, x_ball, y_ball):
    if x_ball >= x_tank - 5 and x_ball <= x_tank + 35:
        if y_ball <= y_tank + 5 and y_ball >= y_tank - 34.29:
            return True
        else:
            return False
    return False
