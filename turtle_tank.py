from Game_modules import objects, physics, menus
from math import radians, sin, cos
import random
import sys
import turtle
import time
import os

# variaveis que armazenam o angulo do tanke nos sprites
ind_green = 0
ind_red = 0

# posição inicial do tanque verde
pos_green_x = -310
pos_green_y = -15

# posição inicial do tanque vermelho
pos_red_x = 260
pos_red_y = -15

# variaveis para ir guardando a posicao do tanque green
actual_pos_x_green = pos_green_x
actual_pos_y_green = pos_green_y

# variaveis para ir guardando a posicao do tanque red
actual_pos_x_red = pos_red_x
actual_pos_y_red = pos_red_y


def game_pause():
    global pause
    if pause is False:
        pause = True
    else:
        pause = False


def create_hud(shape, color):
    hud = turtle.Turtle()
    hud.speed(0)
    hud.shape(shape)
    hud.color(color)
    hud.penup()
    return hud


# Essa função acha a ponta do canhão e cria a bala nessa posição
def create_bullet(posx, posy, color, sprite):
    x = posx
    y = posy

    tanque = open(sprite, "r")
    for _i in range(27):
        largura = tanque.readline()
        for j in range(len(largura)):
            if largura[j] == '2':
                bullet = create_hud("circle", "black")
                bullet.turtlesize(0.2, 0.2)
                bullet.goto(x, y)
                bullet.dx = 0
                bullet.dy = 0
                bullet.hideturtle()
                bullets_list.append(bullet)
                break
            x += 2.5
        x = posx
        y -= 5


# Aqui eu acho a direção da ultima bala lançada
def move_bullet(color, sprite):
    # aqui eu defino o tamanho maximo da lista
    if len(bullets_list) > 10:
        bullets_list[0].hideturtle()
        del bullets_list[0]
    bullets_list[-1].showturtle()
    x = 0
    y = 0
    for i in sprite_tank:
        if sprite == sprite_tank[i]:
            x = cos(radians(i))*20
            y = sin(radians(i))*20
    bullets_list[-1].dx = x
    bullets_list[-1].dy = y


# função que lê o txt/sprite e desenha
def create_tank(posx, posy, color, sprite):

    tanque = open(sprite, "r")
    altura = len(tanque.readlines())

    x = posx
    y = posy

    tanque = open(sprite, "r")
    for _i in range(altura):
        largura = tanque.readline()
        line = []
        for j in range(len(largura)):
            if largura[j] == '1' or largura[j] == '2':
                pixel_tanque = create_hud("square", color)
                pixel_tanque.turtlesize(0.2, 0.2)
                pixel_tanque.goto(x, y)
                line.append(pixel_tanque)
            x += 2.5
        x = posx
        y -= 5
        if color == "green":
            tank_green.append(line)
        else:
            tank_red.append(line)


# função onde apago cada pixel do tanque
def invisible_tank(color):
    if color == "green":
        for i in range(len(tank_green)):
            for j in range(len(tank_green[i])):
                tank_green[i][j].hideturtle()
        tank_green.clear()
    if color == "red":
        for i in range(len(tank_red)):
            for j in range(len(tank_red[i])):
                tank_red[i][j].hideturtle()
        tank_red.clear()


# função que define a nova coordenada do tanque
def move_tank(color, sprite):
    global pos_green_x, pos_green_y
    global pos_red_x, pos_red_y
    global actual_pos_x_green, actual_pos_y_green
    global actual_pos_x_red, actual_pos_y_red
    invisible_tank(color)
    x = 0
    y = 0
    for i in sprite_tank:
        if sprite == sprite_tank[i]:
            x = cos(radians(i))*10
            y = sin(radians(i))*10
    if color == "green":
        actual_pos_x_green += x
        actual_pos_y_green += y
        create_tank(actual_pos_x_green, actual_pos_y_green, color, sprite)
    elif color == "red":
        actual_pos_x_red += x
        actual_pos_y_red += y
        create_tank(actual_pos_x_red, actual_pos_y_red, color, sprite)


# função que muda os sprites para dar movimento de rotação
def rotate_right(color):
    global ind_green, ind_red
    invisible_tank(color)
    if color == "green":
        ind_green -= 22.5
        if ind_green == -22.5:
            ind_green = 337.5
        create_tank(actual_pos_x_green, actual_pos_y_green, color,
                    sprite_tank[ind_green])
    if color == "red":
        ind_red -= 22.5
        if ind_red == -22.5:
            ind_red = 337.5
        create_tank(actual_pos_x_red, actual_pos_y_red, color,
                    sprite_tank[ind_red])


def rotate_left(color):
    global ind_green, ind_red
    invisible_tank(color)
    if color == "green":
        ind_green += 22.5
        if ind_green == 360:
            ind_green = 0
        create_tank(actual_pos_x_green, actual_pos_y_green, color,
                    sprite_tank[ind_green])
    if color == "red":
        ind_red += 22.5
        if ind_red == 360:
            ind_red = 0
        create_tank(actual_pos_x_red, actual_pos_y_red, color,
                    sprite_tank[ind_red])


# Movimentos do tanque verde
def forward_green():
    # O tanque verde fica parado enquanto pause for True
    if pause is False:
        # O tanque verde só pode se mover pra frente
        # se não tiver um muro na frente
        if physics.can_move_forward(actual_pos_x_green, actual_pos_y_green,
                                    "green", sprite_tank[ind_green]) is True:

            move_tank("green", sprite_tank[ind_green])


def rotate_left_green():
    # O tanque verde fica parado enquanto pause for True
    if pause is False:
        rotate_left("green")


def rotate_right_green():
    # O tanque verde fica parado enquanto pause for True
    if pause is False:
        rotate_right("green")


def move_bullet_green():
    # O tanque nao consegue atirar se pause for True
    if pause is False:
        create_bullet(actual_pos_x_green, actual_pos_y_green,
                      "green", sprite_tank[ind_green])
        move_bullet("green", sprite_tank[ind_green])


# Movimentos do tanque vermelho
def forward_red():
    # O tanque vermelho fica parado enquanto pause for True
    if pause is False:
        # O tanque red só pode se mover pra frente
        # se não tiver um muro na frente
        if physics.can_move_forward(actual_pos_x_red, actual_pos_y_red,
                                    "red", sprite_tank[ind_red]) is True:
            move_tank("red", sprite_tank[ind_red])


def rotate_left_red():
    # O tanque vermelho fica parado enquanto pause for True
    if pause is False:
        rotate_left("red")


def rotate_right_red():
    # O tanque vermelho fica parado enquanto pause for True
    if pause is False:
        rotate_right("red")


def move_bullet_red():
    # O tanque nao consegue atirar se pause for True
    if pause is False:
        create_bullet(actual_pos_x_red, actual_pos_y_red,
                      "red", sprite_tank[ind_red])
        move_bullet("red", sprite_tank[ind_red])


# Criando a tela.
screen = turtle.Screen()
screen.title(" Atari Combat ")
screen.bgcolor("orange")
screen.setup(720, 585)
screen.tracer(0)

pause = False

# variaveis da posicao para o score do tanque verde
posx_score_green = -290
posy_score_green = 280

# variaveis da posicao para o score do tanque vermelho
posx_score_red = 250
posy_score_red = 280

# um dicionario com o angulo em graus e o respectivo sprite
sprite_tank = {0: "Sprites_tanks/tank_0.txt",
               22.5: "Sprites_tanks/tank_22.5.txt",
               45: "Sprites_tanks/tank_45.txt",
               67.5: "Sprites_tanks/tank_67.5.txt",
               90: "Sprites_tanks/tank_90.txt",
               112.5: "Sprites_tanks/tank_112.5.txt",
               135: "Sprites_tanks/tank_135.txt",
               157.5: "Sprites_tanks/tank_157.5.txt",
               180: "Sprites_tanks/tank_180.txt",
               202.5: "Sprites_tanks/tank_202.5.txt",
               225: "Sprites_tanks/tank_225.txt",
               247.5: "Sprites_tanks/tank_247.5.txt",
               270: "Sprites_tanks/tank_270.txt",
               292.5: "Sprites_tanks/tank_292.5.txt",
               315: "Sprites_tanks/tank_315.txt",
               337.5: "Sprites_tanks/tank_337.5.txt"}

# lista onde sera armazenado cada pixel dos tanques
tank_green = []
tank_red = []

# Lista de balas na tela "qtd máxima 10!"
bullets_list = []


# por enquanto so o mapa 2 (mapa1) tem fisica
# chamando mapa1 pelo terminal
mapa = open("Maps/" + sys.argv[1], "r")
alturaM = len(mapa.readlines())

# dimensões da arena ( L -> 68, A -> 27)
# desenhando as paredes na tela
posx_parede = -348
posy_parede = 272

x = posx_parede
y = posy_parede
mapa = open("Maps/" + sys.argv[1], "r")
for i in range(alturaM):
    larguraM = mapa.readline()
    for j in range(len(larguraM)):
        if larguraM[j] == '1':
            pixel = create_hud("square", "yellow")
            pixel.turtlesize(1, 1)
            pixel.goto(x, y)
        x += 10.5
    x = posx_parede
    y -= 21


# indice do sprite inicial do tanque verde
ind_green = 0

# indice do sprite inicial do tanque vermelho
ind_red = 180

# criando o tanque verde
create_tank(pos_green_x, pos_green_y, "green", sprite_tank[ind_green])

# criando o tanque vermelho
create_tank(pos_red_x, pos_red_y, "red", sprite_tank[ind_red])

# contorles player verde
screen.listen()
screen.onkeypress(rotate_left_green, 'a')
screen.onkeypress(forward_green, 'w')
screen.onkeypress(rotate_right_green, 'd')
screen.onkeypress(move_bullet_green, 's')

# controles player vermelho
screen.onkeypress(rotate_left_red, 'Left')
screen.onkeypress(forward_red, 'Up')
screen.onkeypress(rotate_right_red, 'Right')
screen.onkeypress(move_bullet_red, 'Down')

# pause
screen.onkeypress(game_pause, 'p')

# cria o score inicial para o tanque verde
objects.create_score(posx_score_green, posy_score_green,
                     "green", "Scores/0.txt")

# cria o score inicial para o tanque vermelho
objects.create_score(posx_score_red, posy_score_red,
                     "red", "Scores/0.txt")

score_red = 0  # pontuacao do tanque vermelho
score_green = 0  # pontuacao do tanque verde
hit = False  # variável que informa quando um tanque é atingido
end = False  # variável pra encerrar o jogo

while end is False:

    screen.update()

    # As balas tem que ficar paradas se pause for True
    if pause is False:
        # aqui faço a movimentação de todas as balas
        for i in range(len(bullets_list)):
            bullets_list[i].sety(bullets_list[i].ycor() + bullets_list[i].dy)
            bullets_list[i].setx(bullets_list[i].xcor() + bullets_list[i].dx)

            # Verifica se a bala atingiu uma parede interna
            if physics.bullet_hit_inside_wall(bullets_list[i].xcor(),
                                              bullets_list[i].ycor()):
                # mando as balas pra longe apos o hit
                bullets_list[i].setx(400)
                bullets_list[i].sety(500)

            # Verifica se o tanque vermelho foi atingido
            hit = physics.collision_bullet_tank(actual_pos_x_red,
                                                actual_pos_y_red,
                                                bullets_list[i].xcor(),
                                                bullets_list[i].ycor())
            if hit is True:
                # so funcionou direito mandando as balas pra longe apos o hit
                bullets_list[i].setx(400)
                bullets_list[i].sety(500)
                objects.change_score(posx_score_green, posy_score_green,
                                     "green", score_green)

                # evita o "empate"
                if score_red < 5:
                    spawn_x, spawn_y = physics.tank_spawn()
                    invisible_tank("red")
                    create_tank(spawn_x, spawn_y, "red",
                                sprite_tank[ind_red])
                    actual_pos_x_red = spawn_x
                    actual_pos_y_red = spawn_y
                    # faz o score mudar neste exato momento
                    screen.update()
                    score_green += 1
                    hit = False

            # Verifica se o tanque verde foi atingido
            hit = physics.collision_bullet_tank(actual_pos_x_green,
                                                actual_pos_y_green,
                                                bullets_list[i].xcor(),
                                                bullets_list[i].ycor())
            if hit is True:
                # so funcionou direito mandando as balas pra longe apos o hit
                bullets_list[i].setx(400)
                bullets_list[i].sety(500)
                objects.change_score(posx_score_red, posy_score_red,
                                     "red", score_red)

                # evita o "empate"
                if score_green < 5:
                    spawn_x, spawn_y = physics.tank_spawn()
                    invisible_tank("green")
                    create_tank(spawn_x, spawn_y, "green",
                                sprite_tank[ind_green])
                    actual_pos_x_green = spawn_x
                    actual_pos_y_green = spawn_y
                    # faz o score mudar neste exato momento
                    screen.update()

                    score_red += 1
                    hit = False

            # Colisão balas com a parede superior
            if(bullets_list[i].ycor() > 210):
                bullets_list[i].hideturtle()

            # Colisão balascom a parede inferior
            if(bullets_list[i].ycor() < -270):
                bullets_list[i].hideturtle()

            # Colisão balas com a parede direita
            if (bullets_list[i].xcor() > 340):
                bullets_list[i].hideturtle()

            # Colisão balas com a parede esquerda
            if(bullets_list[i].xcor() < -345):
                bullets_list[i].hideturtle()

        if score_green == 5:
            menus.winner_message("green")
            time.sleep(3)
            end = True
        elif score_red == 5:
            menus.winner_message("red")
            time.sleep(3)
            end = True
