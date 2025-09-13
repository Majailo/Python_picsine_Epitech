# creer une fonction de generation de la table de viginere
# creer une fonction de cryptage
# creer une fonction de decryptage

alpha = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def code(key, txt, alpha):
    index_key = []
    index_txt = []
    for l in key:
        index_key.append(alpha.index(l))
    for lettre in txt:
        index_txt.append(alpha.index(lettre))

    print(index_txt)
    print(index_key)

    compteur = 0
    for elm in index_txt:
        if compteur <= len(key) + 1:
            combo = [elm, index_key[compteur]]
            print(combo)

        else:
            compteur = 0
        compteur += 1


def generator(combo):
    n_alpha = []  # nouvelle alphabet pour la colone text
    for idx_l in range(combo[0], 26):
        n_alpha.append(alpha[idx_l])
    for idx_l in range(0, combo[0]):
        n_alpha.append(alpha[idx_l])

    # on a plus qu'a prendre la valeur de la cle pour avoir la lettre
    return n_alpha[combo[1]]

    print(n_alpha)


print(generator([12, 8]))


code("abba", "ciel", alpha)
