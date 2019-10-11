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

# Criando a tela.
screen = turtle.Screen()
screen.title(" Atari Combat ")
screen.bgcolor("orange")
screen.setup(720, 585)
screen.tracer(0)

# dimensões da arena ( L -> 68, A -> 27)

# desenhando as paredes na tela
mapa = open("mapa.txt", "r")
alturaM = len(mapa.readlines())

posx_parede = -348
posy_parede = 275

x = posx_parede
y = posy_parede
mapa = open("mapa.txt", "r")
for i in range(alturaM):
    larguraM = mapa.readline()
    for j in range(len(larguraM)):
        if larguraM[j] == '1':
            pixel = create_hud("square", "yellow")
            pixel.turtlesize(1, 1)
            pixel.goto(x,y)
            pixel._tracer(5)
        x += 10.5
    x = posx_parede
    y -= 21

# tentativa 1 - desenhando o tanque verde
tanque1 = open("tanque1.txt", "r")
alturat1 = len(tanque1.readlines())

posx_tanque1 = -60
posy_tanque1 = 0

x = posx_tanque1
y = posy_tanque1
tanque1 = open("tanque1.txt", "r")
for i in range(alturat1):
    largurat1 = tanque1.readline()
    for j in range(len(largurat1)):
        if largurat1[j] == '1':
            pixel_tanque1 = create_hud("square", "green")
            pixel_tanque1.turtlesize(0.3, 0.3)
            pixel_tanque1.goto(x,y)
            pixel_tanque1._tracer(5)
        x += 3.5
    x = posx_tanque1
    y -= 7

# tentativa 1 - desenhando o tanque vermelho
tanque2 = open("tanque1.txt", "r")
alturat2 = len(tanque2.readlines())

posx_tanque2 = 0
posy_tanque2 = 0

x = posx_tanque2
y = posy_tanque2
tanque2 = open("tanque1.txt", "r")
for i in range(alturat2):
    largurat2 = tanque2.readline()
    for j in range(len(largurat2)):
        if largurat2[j] == '1':
            pixel_tanque2 = create_hud("square", "red")
            pixel_tanque2.turtlesize(0.3, 0.3)
            pixel_tanque2.goto(x,y)
            pixel_tanque2._tracer(5)
        x += 3.5
    x = posx_tanque2
    y -= 7

while True:
    screen.update()
