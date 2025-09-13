# task2.6

m = [x // 2 if x % 2 == 0 else x * 2 for x in [42, 3, 4, 18, 3, 10]]
# print(m)
# si le chiffre et paire tu affiche la division par 2 sinon tu le multiplie par 2

# Task 2.7

k = [*enumerate([42, 3, 4, 18, 3, 10])]
# pourquoi le * decompose l objet ?
# https://geekflare.com/fr/python-unpacking-operators/

# enumerate perlmet donner les l index et chaque elment a cette index puis le
# * decomposer l'objet dans un liste
# print(k)


first_names = [" Jackie ", " Chuck ", " Arnold ", " Sylvester "]
last_names = [" Stallone ", " Schwarzenegger ", " Norris ", " Chan "]
magic = [*zip(first_names, last_names[::-1])]
print(magic[0])
print(magic[3])
print(magic[1][0])
print(magic[0][1])
print(magic[2])
print(magic)


# la fonction zip comprime les 2 liste . La liste 2 est mise en reverse
# le * decompose dans la liste
