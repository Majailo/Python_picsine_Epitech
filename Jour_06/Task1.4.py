def bread () :
    print (" <////////// > ")
def lettuce () :
    print (" ~~~~~~~~~~~~ ")
def tomato () :
    print ("O O O O O O")
def ham () :
    print("###########")


def commande (x):
    if type(x) == int:
        for i in range(x+1):
            bread()
            lettuce()
            tomato()
            ham()
            ham()
            bread()
    else :
        print("Je ne peux pas réléaliser des part de sandwich")

commande(4.2)

