# Pendu
import random
from english_words import get_english_words_set

def score(x):
    if x >= 12:
        print ("You loose!")
    
def ram ():
    print(random.sample(range(1,7),6))



def engl():
    #english_words
    #print (random.shuffle(english_word)

    web2lowerset = get_english_words_set(['web2'],lower=True)
    l_web2=list(web2lowerset)
    rm=random.choice(list(web2lowerset))
    print(rm)

def underscore(txt):
    long= len(txt)
    print("_ "* long)

#underscore("abcd")
"""
Pseudocode

def pendu ():
    Pour i partie 
    choie ramdom dans list mots
    initialiser nb essai += 0
    
    Pour i caracter dans le mot:
    print "_ " * i print nb essai 

    demander imput essai 
    si len(imput) = 1 and imput in mot
        var_true_imput.append(input) 
        print "Found {input}"
    sinon 
        nb_essai+=1

    pour i caracter dans le mot 
        si i in var_true 
        print(i)
        else :
            print("_ ")
        
        

""" 

