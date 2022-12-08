#turtle graphics
#CTI-110
#Jason Hunt
#11/6/2022

import turtle
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Initials")

jay = turtle.Turtle()
jay.color("purple")
jay.pensize(10)
jay.shape("turtle")

jay.penup()
jay.forward(100)
jay.right(90)
jay.pendown()
jay.forward(100)
jay.backward(200)
jay.forward(100)
jay.left(90)
jay.forward(100)
jay.right(90)
jay.forward(100)
jay.backward(200)
jay.penup()
jay.forward(100)
jay.right(90)
jay.forward(100)
jay.right(90)
jay.forward(100)
jay.left(90)
jay.forward(150)
jay.pendown()
jay.forward(100)
jay.backward(200)
jay.forward(100)
jay.left(90)
jay.forward(140)
jay.circle(-60,180)

wn.mainloop()

