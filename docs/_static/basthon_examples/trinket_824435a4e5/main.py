from turtle import *

bakgrunn = Screen()
bakgrunn.bgcolor("cyan")

Shelly = Turtle()  # Lager et skilpaddeobjekt
Raphael = Turtle() # Lager et annet skilpaddeobjekt

Shelly.shape("turtle")
Raphael.shape("turtle")

Shelly.color("green")
Raphael.color("red")

Shelly.speed(5)
Raphael.speed(2)

Shelly.forward(100)
Raphael.right(180)
Raphael.forward(100)