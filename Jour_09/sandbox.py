import random


def fr_word(long):
    l_fr = []
    rm = 0
    with open("mots_pendu.txt", "r") as f:
        mots_fr = f.readlines()  # la liste de mot dans le txt

    for elm in mots_fr:
        l_fr.append(elm=elm[-2:-1])

    print(l_fr)


"""
    while len(rm) != long:
        rm = random.choice(mots_fr)
    return rm
"""

(fr_word(6))
