import turtle
color = ["red","orange","yellow","green","blue","violet","pink"]
turtle.tracer(0,0)
for i in range(50):
    turtle.pensize(5)
    turtle.color(color[i % 7])
    turtle.pendown()
    turtle.forward(2 + i * 5)
    turtle.left(50)
    turtle.width(i)
    turtle.penup()

