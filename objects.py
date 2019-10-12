""" Modulo com as funcoes de criacao de objetos"""

import turtle

def create_hud(shape, color):
    hud = turtle.Turtle()
    hud.speed(0)
    hud.shape(shape)
    hud.color(color)
    hud.penup()
    return hud

def create_score(posx, posy, color, sprite):

    score_red = []
    score_green = []
    score = open(sprite, "r")
    altura = len(score.readlines())

    x = posx
    y = posy

    score = open(sprite, "r")
    for i in range(altura):
        largura = score.readline()
        line = []
        for j in range(len(largura)):
            if largura[j] == '1':
                pixel_score = create_hud("square", color)
                pixel_score.turtlesize(0.3, 0.3)
                pixel_score.goto(x,y)
                line.append(pixel_score)
            x += 3.5
        x = posx
        y -= 7
        if color == "green":
            score_green.append(line)
        else:
            score_red.append(line)