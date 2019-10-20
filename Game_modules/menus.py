""" Modulo com os menus do jogo"""


import turtle


def winner_message(color):
    hud = turtle.Turtle()
    hud.speed(0)
    hud.shape("square")
    hud.color(color)
    hud.penup()
    hud.hideturtle()
    hud.goto(0, 0)
    hud.write("Congratulations " + color + " You are the winner!!!",
              align="center", font=("Press Start 2P", 20, "normal"))
