def bread () :
    print (" <////////// > ")
def lettuce () :
    print (" ~~~~~~~~~~~~ ")
def tomato () :
    print ("O O O O O O")
def ham () :
    print("###########")


def commande (x):
    for i in range(x+1):
        bread()
        lettuce()
        tomato()
        ham()
        ham()
        bread()

commande(4)