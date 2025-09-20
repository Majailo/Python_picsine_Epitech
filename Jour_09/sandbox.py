import random


def fr_word(long):
    l_fr = []
    rm = 0
    with open("mots_pendu.txt", "r") as f:
        mots_fr = f.readlines()  # la liste de mot dans le txt


# fr_word(6)


ligne = ["" for _ in range(3)]  # gener que des espace

morpion = [ligne for _ in range(3)]

morpion[1][1] = "0"  # on modifie la ligne dans morpion donc c'est ligne qui est modifié
# on modifi l objet ligne qui est reproduit plusieur fois a l affichage
