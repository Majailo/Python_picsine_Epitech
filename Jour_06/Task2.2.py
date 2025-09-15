import string

def palindrom3 (txt):

    txt_s=txt.split()
    txt_j= "".join(txt_s)
    txt_j="".join(lettre.lower() for lettre in txt_j if lettre not in string.punctuation)
    # utilisation de punctuation pour supprimer les caracteres speciaux
    
    if len(txt_j)<1: # plus de caractere à traiter
        return True
    
    if txt_j[0] == txt_j[-1]:
        return palindrom3(txt_j[1:-1]) # reduit le text de 1 de chaque côté et je plomge
        

    return False
        
print(palindrom3("kayak"))
print(palindrom3("never odd or even!"))




    



    