from pylab import *
from turtle import *

Screen().bgcolor("black")
farger = ["limegreen", "firebrick", "hotpink", "navy", "gold", "darkorchid", "deepskyblue", "yellow", "papayawhip", "indianred", "royalblue"]

def tegn_firkanter(n):
  x = 1
  while x < n:
    farge = choice(farger)
    color(farge)
    forward(50 + x) 
    right(90.9)
    x = x + 1 

def kronblad(r, vinkel):
  farge = choice(farger)
  fillcolor(farge)
  begin_fill()
  for i in range(2):
    circle(r, vinkel)
    left(180 - vinkel)
  end_fill()

def blomst(n, r, vinkel):
  for i in range(n):
    kronblad(r, vinkel)
    left(360/n)

speed(0)

tegn_firkanter(201)
penup()
goto((25,-25))
pendown()
speed(6)
shape("turtle")
color("green")
blomst(11, 70, 70)
penup()
goto((0,150))
left(90)

exitonclick()