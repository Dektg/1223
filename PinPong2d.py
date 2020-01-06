import turtle

window = turtle.Screen()
window.title("2d Ping-Pong")
window.setup(width=1.0,height=1.0)# Размеры окна на весь монитор
window.bgcolor("black")# Задний фон

border_rectangle = turtle.Turtle()
border_rectangle.color("white")
border_rectangle.up()
border_rectangle.goto(-500, 300)
border_rectangle.down()
border_rectangle.goto(500, 300)
border_rectangle.goto(500, -300)
border_rectangle.goto(-500, -300)
border_rectangle.goto(-500, 300)

window.mainloop()