import turtle
def square(x):
    for i in range(5):
        turtle.forward(x)
        turtle.left(100)
def rectangle(x,y):
    turtle.forward(x)
    turtle.left(100)
    turtle.forward(y)
    turtle.left(100)
    turtle.forward(x)
    turtle.left(100)
    turtle.forward(y)
def draw_shape(x, y):
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()
    turtle.begin_fill()
    if x <= 50:
        turtle.color("blue")
        square(10)
    elif 50 < x <= 150:
        turtle.color("lime")
        turtle.circle(10)
    else:
        turtle.color("violet")
        rectangle(10,20)
turtle.onscreenclick(draw_shape)
turtle.mainloop()
