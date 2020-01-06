import turtle

window = turtle.Screen()
window.title("2d Ping-Pong")
# Размеры окна на весь монитор
window.setup(width=1.0, height=1.0)
# Задний фон
window.bgcolor("black")

# Отрисовка поля
border_rectangle = turtle.Turtle()
border_rectangle.color("white")
border_rectangle.speed(5)
# Спрятал отрисовку курсора
border_rectangle.hideturtle()
border_rectangle.up()
border_rectangle.goto(-500, 300)
border_rectangle.down()
border_rectangle.begin_fill()
border_rectangle.goto(500, 300)
border_rectangle.goto(500, -300)
border_rectangle.goto(-500, -300)
border_rectangle.goto(-500, 300)
border_rectangle.end_fill()

border_rectangle.goto(0, 300)
border_rectangle.color("black")
# Повернуться вниз
border_rectangle.setheading(270)

# Цикл для пунктира
for i in range(0, 25, 1):
    if i % 2 == 0:
        border_rectangle.forward(24)
    else:
        border_rectangle.up()
        border_rectangle.forward(24)
        border_rectangle.down()

rocket_a = turtle.Turtle()
rocket_a.color("black")
rocket_a.shape("square")
rocket_a.shapesize(stretch_len=1, stretch_wid=5)
# Не оставляет следов
rocket_a.penup()
rocket_a.goto(-450, 0)


def move_up_a():
    # Узнаю Y у ракетки
    y_rocket_a = rocket_a.ycor() + 80
    if y_rocket_a > 250:
        y_rocket_a = 250
    rocket_a.sety(y_rocket_a)


def move_down_a():
    # Узнаю Y у ракетки
    y_rocket_a = rocket_a.ycor() - 80
    if y_rocket_a < -250:
        y_rocket_a = -250
    rocket_a.sety(y_rocket_a)


rocket_b = turtle.Turtle()
rocket_b.color("black")
rocket_b.shape("square")
rocket_b.shapesize(stretch_len=1, stretch_wid=5)
# Не оставляет следов
rocket_b.penup()
rocket_b.goto(450, 0)


def move_up_b():
    # Узнаю Y у ракетки
    y_rocket_b = rocket_b.ycor() + 80
    if y_rocket_b > 250:
        y_rocket_b = 250
    rocket_b.sety(y_rocket_b)


def move_down_b():
    # Узнаю Y у ракетки
    y_rocket_b = rocket_b.ycor() - 80
    if y_rocket_b < -250:
        y_rocket_b = -250
    rocket_a.sety(y_rocket_b)


window.listen()
window.onkeypress(move_up_a, "q")
window.onkeypress(move_down_a, "a")
#window.onkeypress(move_up_b, "w")
#window.onkeypress(move_down_b, "s")

window.mainloop()
