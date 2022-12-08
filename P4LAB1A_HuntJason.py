#turtle graphics
#CTI-110
#Jason Hunt
#11/6/2022

import turtle
wn = turtle.Screen()
wn.bgcolor("yellow")
wn.title("Triangle & Square")

jay = turtle.Turtle()
jay.color("red")

chelse = turtle.Turtle()
chelse.color("black")

for j in range(4):
    jay.forward(50)
    jay.left(90)

for c in range(3):
    chelse.backward(80)
    chelse.right(120)

wn.mainloop()

