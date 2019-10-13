
from Game_modules import objects
import random
import sys
import turtle
import time
import os


pause = False

# variaveis da posicao para o score do tanque verde
posx_score_green = -290
posy_score_green = 280

# variaveis da posicao para o score do tanque vermelho
posx_score_red = 250
posy_score_red = 280

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


# um dicionario com o angulo em graus e o respectivo sprites
sprite_tank = {0: "Sprites_tanks/tanque_right.txt",
               45: "Sprites_tanks/tanque_up_right.txt",
               90: "Sprites_tanks/tanque_up.txt",
               135: "Sprites_tanks/tanque_up_left.txt",
               180: "Sprites_tanks/tanque_left.txt",
               225: "Sprites_tanks/tanque_dow_left.txt",
               270: "Sprites_tanks/tanque_dow.txt",
               315: "Sprites_tanks/tanque_dow_right.txt"}

# vetor com todos os mapas
MapVector = ["Maps/mapa.txt", "Maps/mapa2.txt"]


# Escolhendo o mapa dentro do vetor
def random_map(x):
    y = random.randint(0, len(x)-1)
    return x[y]


# lista onde sera armazenado cada pixel dos tanques
tank_green = []
tank_red = []


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
            if largura[j] == '1':
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
    invisible_tank(color)
    x = 0
    y = 0
    if sprite == "Sprites_tanks/tanque_up.txt":
        y += 30
    elif sprite == "Sprites_tanks/tanque_dow.txt":
        y -= 30
    elif sprite == "Sprites_tanks/tanque_right.txt":
        x += 30
    elif sprite == "Sprites_tanks/tanque_left.txt":
        x -= 30
    elif sprite == "Sprites_tanks/tanque_up_right.txt":
        x += 15
        y += 15
    elif sprite == "Sprites_tanks/tanque_up_left.txt":
        x -= 15
        y += 15
    elif sprite == "Sprites_tanks/tanque_dow_left.txt":
        x -= 15
        y -= 15
    elif sprite == "Sprites_tanks/tanque_dow_right.txt":
        x += 15
        y -= 15
    if color == "green":
        pos_green_x = pos_green_x + x
        pos_green_y = pos_green_y + y
        create_tank(pos_green_x, pos_green_y, color, sprite)
    elif color == "red":
        pos_red_x = pos_red_x + x
        pos_red_y = pos_red_y + y
        create_tank(pos_red_x, pos_red_y, color, sprite)


# função que muda os sprites para dar movimento de rotação
def rotate_right(color):
    global ind_green, ind_red
    invisible_tank(color)
    if color == "green":
        ind_green -= 45
        if ind_green == -45:
            ind_green = 315
        create_tank(pos_green_x, pos_green_y, color, sprite_tank[ind_green])
    if color == "red":
        ind_red -= 45
        if ind_red == -45:
            ind_red = 315
        create_tank(pos_red_x, pos_red_y, color, sprite_tank[ind_red])


def rotate_left(color):
    global ind_green, ind_red
    invisible_tank(color)
    if color == "green":
        ind_green += 45
        if ind_green == 360:
            ind_green = 0
        create_tank(pos_green_x, pos_green_y, color, sprite_tank[ind_green])
    if color == "red":
        ind_red += 45
        if ind_red == 360:
            ind_red = 0
        create_tank(pos_red_x, pos_red_y, color, sprite_tank[ind_red])


# Criando a tela.
screen = turtle.Screen()
screen.title(" Atari Combat ")
screen.bgcolor("orange")
screen.setup(720, 585)
screen.tracer(0)

# dimensões da arena ( L -> 68, A -> 27)
# desenhando as paredes na tela
chosen_map = random_map(MapVector)
mapa = open(chosen_map, "r")
alturaM = len(mapa.readlines())

posx_parede = -348
posy_parede = 272

x = posx_parede
y = posy_parede
mapa = open(chosen_map, "r")
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

# posição inicial do tanque verde
pos_green_x = -310
pos_green_y = -15
# posição inicial do tanque vermelho
pos_red_x = 260
pos_red_y = -15
# indice do sprite inicial do tanque verde
ind_green = 0
# indice do sprite inicial do tanque vermelho
ind_red = 180
# criando o tanque verde
create_tank(pos_green_x, pos_green_y, "green", sprite_tank[ind_green])


# Movimentos do tanque verde
def forward_green():
    # O tanque verde fica parado enquanto pause for True
    if pause is False:
        move_tank("green", sprite_tank[ind_green])


def rotate_left_green():
    # O tanque verde fica parado enquanto pause for True
    if pause is False:
        rotate_left("green")


def rotate_right_green():
    # O tanque verde fica parado enquanto pause for True
    if pause is False:
        rotate_right("green")


# criando o tanque vermelho
create_tank(pos_red_x, pos_red_y, "red", sprite_tank[ind_red])


# Movimentos do tanque vermelho
def forward_red():
    # O tanque vermelho fica parado enquanto pause for True
    if pause is False:
        move_tank("red", sprite_tank[ind_red])


def rotate_left_red():
    # O tanque vermelho fica parado enquanto pause for True
    if pause is False:
        rotate_left("red")


def rotate_right_red():
    # O tanque vermelho fica parado enquanto pause for True
    if pause is False:
        rotate_right("red")


# contorles player verde
screen.listen()
screen.onkeypress(rotate_left_green, 'a')
screen.onkeypress(forward_green, 'w')
screen.onkeypress(rotate_right_green, 'd')

# controles player vermelho
screen.onkeypress(rotate_left_red, 'Left')
screen.onkeypress(forward_red, 'Up')
screen.onkeypress(rotate_right_red, 'Right')

# pause
screen.onkeypress(game_pause, 'p')

# cria o score inicial para o tanque verde
objects.create_score(posx_score_green, posy_score_green,
                     "green", "Scores/0.txt")

# cria o score inicial para o tanque vermelho
objects.create_score(posx_score_red, posy_score_red,
                     "red", "Scores/0.txt")


def wall_green(x, y, sprite):
    if x - 20 <= -360:
        x = -340
        invisible_tank("green")
        create_tank(x, y, "green", sprite_tank[ind_green])
    elif x + 20 >= 312:
        x = 292
        invisible_tank("green")
        create_tank(x, y, "green", sprite_tank[ind_green])

    elif y - 20 <= -232:
        y = -212
        invisible_tank("green")
        create_tank(x, y, "green", sprite_tank[ind_green])
    elif y + 20 >= 222:
        y = 202
        invisible_tank("green")
        create_tank(x, y, "green", sprite_tank[ind_green])


def wall_red(x, y):
    if x - 20 <= -360:
        x = -340
        invisible_tank("red")
        create_tank(x, y, "red", sprite_tank[ind_red])
    elif x + 20 >= 312:
        x = 292
        invisible_tank("red")
        create_tank(x, y, "red", sprite_tank[ind_red])

    elif y - 20 <= -232:
        y = -212
        invisible_tank("red")
        create_tank(x, y, "red", sprite_tank[ind_red])
    elif y + 20 >= 222:
        y = 202
        invisible_tank("red")
        create_tank(x, y, "red", sprite_tank[ind_red])


def wall_collide(color):
    if color == "green":
        wall_green(pos_green_x, pos_green_y, sprite_tank[ind_green])
    elif color == "red":
        wall_red(pos_red_x, pos_red_y)


score_red = 0  # pontuacao do tanque vermelho
score_green = 0  # pontuacao do tanque verde

while True:

    # Se o tanque vermelho atingir o tanque verde:
        # objects.change_score(posx_score_red, posy_score_red, "red", score_red)
        # score_red += 1

    # Se o tanque verde atingir o tanque vermelho:
        # objects.change_score(posx_score_green, posy_score_green, "green", score_green)
        # score_green += 1

    # Se score_red == 5 or score_green == 5:
        # fim de jogo (sair do while)
    screen.update()

    # colisão paredes (ainda tá meio cagado, mas não toca não que eu vou ajeitar)
    wall_collide("green")
    wall_collide("red")
