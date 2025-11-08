# Pendu
import random
from english_words import get_english_words_set
import time
import os


class Handgame:

    def __init__(self):
        self.long = 6  # Longeur du mot
        self.word = self.fr_word()
        self.winner = False
        self.loser = False
        self.penalty = 0
        self.max_penalty = 13
        self.l_aff = []
        self.l_try = []
        self.l_found = []

    def score(self, x):
        return x >= self.max_penalty - 1

    def fr_word(self):  # dictionnaire fr
        rm = ""
        with open("mots_pendu.txt", "r") as f:
            mots_fr = [m.strip() for m in f.readlines()]   # la liste de mot dans le txt

        while len(rm) != self.long:
            rm = random.choice(mots_fr)
        return rm

    def engl(self):  # dictionnaire englais
        rm = ""
        web2lowerset = get_english_words_set(["web2"], lower=True)
        while len(rm) != self.long:
            rm = random.choice(list(web2lowerset))
        return rm

    def underscore(self, l_found):  # gener les _ sur les lettre absente
        self.l_aff = []
        for l in self.word:  # verifier chaque lettre dans le mot
            self.l_aff.append(l if l in l_found else "_")
            # si la lettre est dans le l_found
        # return self.l_aff  # retourne une liste de lettre avec le ou _

    def nb_found(self):  # comptabilisation des lettres trouvées
        nb = 0
        for elm in self.word:
            nb += 1 if elm in self.l_found else nb
        return nb

    def match(self, tent):
        # controle la lettre trouvé avec le mots
        # Controle la tentative et donne le penalty en fonction du resultat

        if len(tent) <= 1:
            if tent in self.word:
                self.l_found.append(tent)
                if self.nb_found() == len(self.word):
                    self.winner = True
                    return self.penalty, self.l_found, self.winner

            else:
                print(f"Not Found {tent}")
                self.penalty += 1
                self.score(self.penalty)

        else:
            if tent == self.word:
                self.winner = True
                return self.penalty, self.l_found, self.winner

            # else:
            #     self.penalty += 5
        return self.penalty, self.l_found, self.winner

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

    def letter_try(self, l):
        if l not in self.l_try:
            self.l_try.append(l)
        return self.l_try

    def hangman(self, last_ev_key, l_tuch):

        if self.penalty < self.max_penalty:  # and t < max_time:
            # letter_try(l_aff)
            self.underscore(l_tuch)
            # affiche des _ si la lettre ne sont pas trouvé

            self.match(last_ev_key)
            # print(l_aff)
        else:
            self.l_aff = self.underscore(l_tuch)
            self.loser = True

        return self.l_aff, self.penalty, self.winner, self.loser
