import turtle

import tkinter


toto = turtle.Screen ()  # affiche l'ecran
toto.bgcolor("black") # creer un fond noir
tt = turtle.Turtle () # creer l objet turtul pour le faire bouger
tt.color("red") # met le traçage en rouge



def contr(x):
        
    for i in range (x) :
        tt.right (360/x) # tourne de 90° à droit
        tt.forward(100)

    toto.exitonclick ()

contr(6)