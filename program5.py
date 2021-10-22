import turtle
turtle.bgcolor("white")
turtle.color("green")
turtle.pensize(1)
for angle in range(0,360,10):
    turtle.seth(angle)
    turtle.circle(50)
