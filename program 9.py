from turtle import *
color('blue', 'light blue')
begin_fill()
while True:
    forward(150)
    left(100)
    if abs(pos()) < 1:
        break
end_fill()
done()
