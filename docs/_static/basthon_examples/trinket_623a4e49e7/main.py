from turtle import *

shape("turtle")
color("blue")
speed(2)
pensize(10)

right(120)
forward(75)
right(120)
forward(75)
right(120)
forward(75)

penup()
goto((50,50))
pendown()

fillcolor("limegreen")
begin_fill()
circle(50)
end_fill()

fillcolor("red")
begin_fill()
left(60)
circle(100)
end_fill()

print(pos())