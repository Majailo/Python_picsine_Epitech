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

# Fonction de generation de list avec les index de la clef et du text
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
    combo=[]
    
    for elm in index_txt:

        if compteur >= len(key)-1:
            compteur= 0
            combo.append([elm, index_key[compteur]])

        else:
            combo.append([elm, index_key[compteur]])
            
        compteur+=1

    return combo


# fonction generation de d'alphabet par index
def generator(key,txt,alpha):
    secret=[]

    combo = code(key,txt,alpha)
    for elm in combo: # gener un nouveau alphabet sur la base du text
        n_alpha = []  # nouvelle alphabet pour la colonne text
                
        for idx_l in range(elm[0], 26):
            n_alpha.append(alpha[idx_l])

        for idx_l in range(0, elm[0]):
            n_alpha.append(alpha[idx_l])
        
        secret.append(n_alpha[elm[1]])
        
    
    print("".join(secret))

    # on a plus qu'a prendre la valeur de la cle pour avoir la lettre
    #print (n_alpha[elm[1]]) #



generator("abba","ciel",alpha)
