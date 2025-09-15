def bread () :
    print (" <////////// > ")
def lettuce () :
    print (" ~~~~~~~~~~~~ ")
def tomato () :
    print ("O O O O O O")
def ham () :
    print("###########")
def veg () :
    print("VVVVVVVVVVV")


def commande (x, arg = True):
       
    if type(x) == int:
        if arg == True:
            for i in range(x+1):
                bread()
                lettuce()
                tomato()
                ham()
                ham()
                bread()
        
        elif arg == False:
                bread()
                lettuce()
                tomato()
                veg()
                veg()
                bread()

    else :
        print("Je ne peux pas réléaliser des part de sandwich")

commande(5,False)

