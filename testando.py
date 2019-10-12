import random
import sys
import turtle
import time
import os

def create_hud(shape, color):
    hud = turtle.Turtle()
    hud.speed(0)
    hud.shape(shape)
    hud.color(color)
    hud.penup()
    return hud


def create_tank(posx, posy, color, frame):

    tanque = open(frame, "r")
    altura = len(tanque.readlines())

    x = posx
    y = posy

    tanque = open(frame, "r")
    for i in range(altura):
        largura = tanque.readline()
        for j in range(len(largura)):
            if largura[j] == '1':
                pixel_tanque = create_hud("square", color)
                pixel_tanque.turtlesize(0.3, 0.3)
                pixel_tanque.goto(x,y)
            x += 3.5
        x = posx
        y -= 7

# vetor com todos os mapas 
MapVector = ["mapa.txt", "mapa2.txt"]


#Escolhendo o mapa dentro do vetor
def random_map(x):
    y = random.randint(0,len(x)-1)
    return x[y] 


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
posy_parede = 275

x = posx_parede
y = posy_parede
mapa = open(chosen_map, "r")
for i in range(alturaM):
    larguraM = mapa.readline()
    for j in range(len(larguraM)):
        if larguraM[j] == '1':
            pixel = create_hud("square", "yellow")
            pixel.turtlesize(1, 1)
            pixel.goto(x,y)
        x += 10.5
    x = posx_parede
    y -= 21

# "lembrando que se alguem achar uma forma melhor de criar
# esses tanques pode colocar ai, pq ta complicado de movimentar isso"

# desenhando o tanque verde
create_tank(0, 60, "green", "tanque_up.txt")
create_tank(0, 0, "green", "tanque_up_right.txt")
create_tank(0, -60, "green", "tanque_right.txt")
# desenhando o tanque vermelho
create_tank(-60, 60, "red", "tanque_up.txt")
create_tank(-60, 0, "red", "tanque_up_right.txt")
create_tank(-60, -60, "red", "tanque_right.txt")

while True:
    screen.update()
