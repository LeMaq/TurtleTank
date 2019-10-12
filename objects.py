""" Modulo com as funcoes de criacao de objetos"""

import turtle

def create_hud(shape, color):
    hud = turtle.Turtle()
    hud.speed(0)
    hud.shape(shape)
    hud.color(color)
    hud.penup()
    return hud

score_red = []
score_green = []

def create_score(posx, posy, color, sprite):

    score = open(sprite, "r")
    altura = len(score.readlines())

    x = posx
    y = posy

    score = open(sprite, "r")
    for _i in range(altura):
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


# função onde apago cada pixel de um score
def invisible_score(color):
    if color == "green":
        for i in range(len(score_green)):
            for j in range(len(score_green[i])):
                score_green[i][j].hideturtle()
        score_green.clear()
    if color == "red":
        for i in range(len(score_red)):
            for j in range(len(score_red[i])):
                score_red[i][j].hideturtle()
        score_red.clear()

# lista dos arquivos txt dos scores para facilitar a mudanca de um score
'''scores = ['Scores/0.txt', 'Scores/1.txt',
          'Scores/2.txt', 'Scores/3.txt',
          'Scores/4.txt', 'Scores/5.txt']
'''
def change_score(posx, posy, color, actual_score):
    invisible_score(color)
    if actual_score == 0:
        create_score(posx, posy, color, 'Scores/1.txt')
    elif actual_score == 1: 
        create_score(posx, posy, color, 'Scores/2.txt')
    elif actual_score == 2:
        create_score(posx, posy, color, 'Scores/3.txt')
    elif actual_score == 3:
        create_score(posx, posy, color, 'Scores/4.txt')
    elif actual_score == 4:
        create_score(posx, posy, color, 'Scores/5.txt')
    

