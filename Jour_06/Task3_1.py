# faire 3 fonction qui donner un bollene en fonction du nombre de carractet rentrée
import string

txt="abcde3"

def long (txt, num):
    nb=0
    for elm in txt:
        if elm in string.ascii_letters:
            nb+=1   
    if num >= nb:
        return True
    return False

#print (long(txt,2))

def ponct (txt, num):
    nb=0
    for elm in txt:    
        if elm in string.punctuation:
            nb+=1
    if num >= nb:
        return True
    
    return False

#print(ponct(txt, 0))


def digit (txt, num):
    nb=0
    for elm in txt:
        if elm in string.digits :
            nb+=1
        
        if num >= nb:
            return True
        
    return False

#print(digit(txt,1))

