# Pendu
import random
from english_words import get_english_words_set
import time
import os


l_try = []


def score(x):
    return x >= 12


def fr_word(long):

    rm = 0
    with open("mots_pendu.txt", "r") as f:
        mots_fr = f.readlines()  # la liste de mot dans le txt

    while len(rm) != long:
        rm = random.choice(mots_fr)
    return rm


def engl(long):
    rm = ""
    # english_words
    # print (random.shuffle(english_word)
    web2lowerset = get_english_words_set(["web2"], lower=True)
    # l_web2=list(web2lowerset)
    while len(rm) != long:
        rm = random.choice(list(web2lowerset))
    return rm


"""
def underscore1(txt, l_found):
    l_aff = []
    for l in txt:  # verifier chaque lettre dans le mot
        if l in l_found:  # si la lettre est dans le l_found
            l_aff.append(l)
        else:
            l_aff.append("_")
    return l_aff  # retourne une liste de lettre avec le ou _
"""


def underscore(txt, l_found):
    l_aff = []
    for l in txt:  # verifier chaque lettre dans le mot
        l_aff.append(l if l in l_found else "_")  # si la lettre est dans le l_found
    return l_aff  # retourne une liste de lettre avec le ou _


"""
def nb_found2(l_found, word):
    nb = 0
    for elm in word:
        if elm in l_found:
            nb += 1
    return nb
"""


def nb_found(l_found, word):
    nb = 0
    for elm in word:
        nb += 1 if elm in l_found else nb
    return nb


def match(
    tent, word, penalty, l_found
):  # Controle la tentative et donne le penalty en fonction du resultat
    winner = False

    if len(tent) <= 1:
        if tent in word:

            print("")
            print(f"Found {tent.upper()} ")
            l_found.append(tent)
            if nb_found(l_found, word) == len(word):
                winner = True
                print("You win")
                print(" ### You Hack the word ### ")
                return penalty, l_found, winner

        else:
            print(f"Not Found {tent}")
            penalty += 1
            score(penalty)

    else:
        if tent == word:
            winner = True
            print("Nice job! You win")
            print(" ### You Hack the word ### ")
            return penalty, l_found, winner

        else:
            penalty += 5
    return penalty, l_found, winner


# underscore("abcd")
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


def letter_try(l):
    if l not in l_try:
        l_try.append(l)
    return l_try


"""
def letter_try1(l):
    return l_try.append(l if l not in l_try else "")
"""


def hangman(ev_key, l_found, penalty, word):
    winner = False
    loser = False

    max_penalty = 13

    if penalty < max_penalty:  # and t < max_time:
        # letter_try(l_aff)
        l_aff = underscore(word, l_found)
        # affiche des _ si la lettre ne sont pas trouvé
        # main2.out_of_txt("".join(l_aff),550,100,police)

        penalty, l_found, winner = match(ev_key, word, penalty, l_found)
        print(l_aff)
    else:
        l_aff = underscore(word, l_found)
        loser = True

    return l_aff, penalty, winner, loser
