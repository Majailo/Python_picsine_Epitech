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


def crypt(txt, key):
    secret = []
    for l in txt:
        if l == " ":
            secret.append(" ")
        else:
            ind = alpha.index(l)
            c_ind = ind + key
            secret.append(alpha[c_ind])
    print("".join(secret))


crypt("le chat du voisin", 3)
