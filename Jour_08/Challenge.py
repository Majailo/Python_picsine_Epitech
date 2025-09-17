import turtle
import random
import tkinter


toto = turtle.Screen ()  # affiche l'ecran
turtle.colormode(255)
#toto.bgcolor("black") # creer un fond noir
tt = turtle.Turtle () # creer l objet turtul pour le faire bouger
tt.color("red") # met le traçage en rouge
tt.speed(0)



def contr(x):
        
    for i in range (x) :
        tt.right (360/x) # tourne de 90° à droit
        tt.forward(100)

    toto.exitonclick ()

#contr(6)


def spiral (x):

    for i in range (x):
        tt.circle(i,10) # creation de cercle de 10 ° avec un augementation de chque tours du rayon 
    
    toto.exitonclick()

#spiral(300)


""" 
trace un tringle 
va a la moitier d'un côté et trace un nouveau triangle 



"""


def fractal_triangle():

    #for x in range(10):

    for i in range (3):
        tt.right(360/3)
        tt.forward(500)
    toto.exitonclick()
    
#fractal_triangle()

"""
faire un spirale puis gener un carré  et reproduite a chaque fois


"""
def color():
    a=random.randint(0,256)
    b=random.randint(0,256)
    c=random.randint(0,256)
    print(a,b,c)
    return a, b ,c 

def carre(x):
    a,b,c = color()
    tt.begin_fill()
    tt.fillcolor(a,b,c)
    
    for i in range (4):
        
        tt.right(90)
        tt.forward(x)
    
    tt.end_fill()


def in_spiral (x):
    
    for i in range (x):
        tt.circle(x-i,10) # creation de cercle de 10 ° avec un augementation de chque tours du rayon 
    
    toto.exitonclick()

#in_spiral(300)


def rep_carre(x):

    for i in range (x,0,-50): #taille des carre 
        for ang in range(36): # nombre de carré sur 360°
            carre(i)
            tt.right(10) # creation de cercle de 10 ° avec un augementation de chque tours du rayon
    
    
    toto.exitonclick()

rep_carre(500)
