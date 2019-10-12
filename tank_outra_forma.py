import turtle

screen = turtle.Screen()
screen.bgcolor("black")


rear_lenght = 25
front_lenght = rear_lenght
hull_lenght = 30
track_leght = rear_lenght + hull_lenght + front_lenght # comprimento da esteira
track_width = 15 # largura da esteira
cannon_lenght = 50 #comprimento do canhao
left_hull_width = 15
cannon_width = 10
right_hull_width = left_hull_width
hull_width = right_hull_width + cannon_width + left_hull_width
 
x = 200
y = 0

def create_tank(x,
                y,
                rear_lenght,
                front_lenght,
                hull_lenght,
                track_leght,
                track_width,
                cannon_lenght,
                cannon_width,
                left_hull_width,
                right_hull_width,
                hull_width,
                color):

    pen = turtle.Turtle()
    pen.goto(x, y)
    pen.color(color)
    pen.speed(0)

    pen.begin_fill()
    pen.forward(track_leght) # esteira esquerda parte 1
    pen.left(90)
    pen.forward(track_width)
    pen.left(90)

    pen.forward(rear_lenght) # carroceria traseira
    pen.right(90)
    pen.forward(hull_width)
    pen.right(90)
    pen.forward(rear_lenght)
    pen.left(90)

    pen.forward(track_width) # esteria direita
    pen.left(90)
    pen.forward(track_leght)
    pen.left(90)
    pen.forward(track_width)
    pen.left(90)

    pen.forward(front_lenght) # carroceria dianteira direita
    pen.right(90)
    pen.forward(right_hull_width)

    pen.right(90) #canhao
    pen.forward(cannon_lenght)
    pen.left(90)
    pen.forward(cannon_width)
    pen.left(90)
    pen.forward(cannon_lenght)
    pen.right(90)

    pen.forward(left_hull_width) # carroceria dianteira esquerda
    pen.right(90)
    pen.forward(front_lenght)
    pen.left(90)

    pen.forward(track_width) # esteria esquerda parte 2
    pen.left(90)
    pen.end_fill()
    pen.hideturtle()

    return pen


tank_red = create_tank(x,
                       y,
                       rear_lenght,
                       front_lenght,
                       hull_lenght,
                       track_leght,
                       track_width,
                       cannon_lenght,
                       cannon_width,
                       left_hull_width,
                       right_hull_width,
                       hull_width,
                       "red")

screen.exitonclick()