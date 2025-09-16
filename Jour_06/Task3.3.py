# faire 3 fonction qui donner un bollene en fonction du nombre de carractet rentrée
import Task3_1

password="mysecretpassword1!!!"
password2= True

def passcheck(password):
    # test du type saisie avec gestion des erreur:

    try:
        if Task3_1.long(password,16) and Task3_1.digit(password,1) and Task3_1.ponct(password,3):
            return True
        
        print("Veuillez saisir un password correcte")
        return False

    except:
        print("veuiller saisir un chaine de caracter avec lettre chiffre et caractere spécial")


print(passcheck(password2))