# chiffre cesar
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


def decrypt(txt):

    for key in range(0, 26):
        secret = []
        for l in txt:  # on va cherche chaque lettre du text
            if l == " ":
                secret.append(
                    " "
                )  # si on a un " " on l'ajoute au texte sans recherche suplementaire
            else:
                ind = alpha.index(
                    l
                )  # on regarde l'index de cette lettre dans la list de l'aphabet
                c_ind = ind + key  # on ajoute la clef à l index pour le decalage

                if (
                    c_ind >= 25
                ):  # si l'index depasse celui de l'aphabet on repart à zero
                    c_ind = ind + key - 26
                secret.append(alpha[c_ind])
        print("".join(secret))


decrypt("le chat du voisin")
