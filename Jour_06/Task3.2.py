# faire 3 fonction qui donner un bollene en fonction du nombre de carractet rentrée
import string
import Task3_1

password="mysecretpassword1!!!"

def passcheck(password):
    if Task3_1.long(password,16) and Task3_1.digit(password,1) and Task3_1.ponct(password,3):
        return True
    return False

print(passcheck(password))