import turtle

import tkinter


toto = turtle.Screen ()  # affiche l'ecran
toto.bgcolor("black") # creer un fond noir
titi = turtle.Turtle () # creer l objet turtul pour le faire bouger
titi.color("red") # met le traçage en rouge

for i in range (3) :
    titi.right (90) # tourne de 90° à droit
    titi.circle (42)  # contruit un cercle de 42 px de rayon

toto.exitonclick ()

