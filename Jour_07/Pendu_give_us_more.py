# Pendu
import random
from english_words import get_english_words_set
import time


def score(x):
    if x >= 12:
        print ("You loose!")
        return False
    return True
    

def engl(long):
    rm=""
    #english_words
    #print (random.shuffle(english_word)
    web2lowerset = get_english_words_set(['web2'],lower=True)
    #l_web2=list(web2lowerset)
    while len(rm) != long:
        rm=random.choice(list(web2lowerset))
    return rm

def underscore(txt,l_found):
    
    for l in txt :
        if l in l_found:
            print(f"{l.upper()} ", end="")
        else :
            print("_ ",end= "")

def nb_found(l_found, word):
    nb=0
    for elm in word:
        if elm in l_found:
            nb+=1
    return nb


def match(tent,word,penalty,l_found): # Controle la tentative et donne le penalty en fonction du resultat
    if len(tent) <= 1:
        if tent in word:

            print("")
            print(f"Found {tent.upper()} ")
            l_found.append(tent)
            if nb_found(l_found,word) == len(word):
                print("You win")
                print( " ### You Hack the word ### ")
                exit()
            
        else :
            print(f"Not Found {tent}")
            penalty +=1
            score(penalty)
        
    else :
        if tent == word:
            print("Nice job! You win")
            print( " ### You Hack the word ### ")
            exit()
        else:
            penalty+=5
    return penalty, l_found 

#underscore("abcd")
"""
Pseudocode

def pendu ():
    Pour i partie 
    choisi un ramdom dans list mots
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

def hangman():
    l_found=[]
    penalty=0
    print( "Welcom to hangman game.....")
    len_word=int(input("please chose your difficulty of the word. number of letter :  "))
    max_penalty=int(input(" Now chose you number of life : "))
    max_time= int(input ("Chose a time game in second !"))


    word = engl(len_word)
    #word= "abba"
    print("---------------------- Game Start ------------------------")
    print(word)
    start= time.time()
    t=0

    while penalty<=max_penalty and t < max_time:
        underscore(word, l_found) # affiche des _ si la lettre ne sont pas trouvé
        print(f"  {penalty} Penalty")
        print("")
        t = time.time() - start
        if max_time-t < 20 :
            print(" Je voudrais pas de presser mais il te reste moins de 20 sec ! Après je dis ça, je dis rien  ")
            print("")

        user_tent=input("Send your letter or word :  ").lower()
        penalty, l_found = match(user_tent,word,penalty,l_found)
        

    print("")
    print("#### Game Over ####" )
    
        
hangman()
