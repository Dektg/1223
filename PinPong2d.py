import turtle

window = turtle.Screen()
window.title("2d Ping-Pong")
# Размеры окна на весь монитор
window.setup(width=1.0,height=1.0)
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
for i in range(0,25,1):
    if i % 2 == 0:
        border_rectangle.forward(24)
    else:
        border_rectangle.up()
        border_rectangle.forward(24)
        border_rectangle.down()


window.mainloop()