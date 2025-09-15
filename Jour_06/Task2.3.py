import os

#print (os.getcwd()) #donne l'emplacement actuel

#print(os.listdir("/home/cyrille/Epitech/Python")) # donne la liste des fichier et dossier 

def dossier (chemin) :

    print(f"{chemin.split("/")[-1]} : ") # dossier en cour
    print(f"        {os.listdir(chemin)}")
    for elm in os.listdir(chemin):
        conca=chemin + "/" +elm

        if os.path.isdir(conca) :
            dossier(conca)

chemin ="/home/cyrille/Epitech/Python/Piscine/Jour_06/Dossier_text_recur"
dossier(chemin)

