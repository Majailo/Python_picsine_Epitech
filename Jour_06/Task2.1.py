def nb_entier (x):
    if x== 0:
        return 0
    else:
        z= x + nb_entier(x-1)
        return z

print(nb_entier(42))

