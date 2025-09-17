import turtle

import tkinter
tt = turtle.Turtle()

for i in range(4):
    print(tt.position())
    tt.color("red")
    tt.forward(100)
    tt.right(90)

turtle.done()