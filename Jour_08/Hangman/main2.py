import pygame
import Pendu_for_pygame


pygame.init()

ecran = pygame.display.set_mode((900, 600))
image = pygame.image.load("wallpaper_game.xcf").convert()  # charge l image de fond
Blanc = (255, 255, 255)
pygame.display.set_caption("The Hangman")  # titre du la fenetre
police = pygame.font.SysFont("Arial", 70, False, True)  # style d'ecriture pour le jeu
police2 = pygame.font.SysFont("Arial", 25, False, True)
police_point = pygame.font.SysFont("Arial", 45, False, True)

# intialisation des parametre du jeu
len_word = 6
penalty = 0
word = Pendu_for_pygame.engl(len_word)
print(word)

winner = False
loser = False

txt = police.render("txt", True, Blanc)
# txt_zone=police.get_rect(250,450) # objet de la zone de txt


image_rect = image.get_rect()  # dimension l'objet ajouté
txt_rect = txt.get_rect()
txt_rect.center = (250, 250)


def out_of_txt(text, x, y, police):  # fonction d'affichage de text
    txt = police.render("".join(text), True, Blanc)  # fromatage de police
    txt_rect = txt.get_rect()  # mise en dimention de text encadrement
    txt_rect.center = (x, y)  # positionnement
    ecran.blit(txt, txt_rect)  # affichages sur la page de jeu


def clear_screen():
    ecran.blit(image, image_rect)  # ecran de fond lancer avant la boucle


def clean_start(l_aff="", penalty=0, winner=False, loser=False):
    clear_screen()
    l_aff = []
    l_aff, penalty, winner, loser = Pendu_for_pygame.hangman(
        l_tuch[-1], l_tuch, penalty, word
    )  # on lance le jeux et on alimente avec le text du joueur

    out_of_txt(l_aff, 500, 500, police)


def manstick():

    # pygame.draw.line(ecran,(0,0,0),(10,10),(100,100),width=10)
    pygame.draw.line(ecran, (0, 0, 0), (50, 550), (100, 550), width=7)
    pygame.draw.line(ecran, (0, 0, 0), (50, 550), (75, 500), width=7)
    pygame.draw.line(ecran, (0, 0, 0), (100, 550), (75, 500), width=7)

    # base

    pygame.draw.line(ecran, (0, 0, 0), (75, 500), (75, 400), width=7)
    pygame.draw.line(ecran, (0, 0, 0), (75, 400), (75, 300), width=7)
    pygame.draw.line(ecran, (0, 0, 0), (75, 300), (75, 200), width=7)
    # Mat
    pygame.draw.line(ecran, (0, 0, 0), (75, 200), (175, 200), width=7)
    pygame.draw.line(ecran, (0, 0, 0), (175, 200), (275, 200), width=7)
    # corde
    pygame.draw.line(ecran, (0, 0, 0), (275, 200), (275, 300), width=7)
    # man
    pygame.draw.circle(ecran, (0, 0, 0), (275, 300), 20)
    pygame.draw.line(ecran, (0, 0, 0), (275, 300), (275, 400), width=7)
    # Bras
    pygame.draw.line(ecran, (0, 0, 0), (275, 350), (250, 325), width=9)
    pygame.draw.line(ecran, (0, 0, 0), (275, 350), (300, 325), width=9)

    # Jambe
    pygame.draw.line(ecran, (0, 0, 0), (275, 400), (250, 425), width=7)
    pygame.draw.line(ecran, (0, 0, 0), (275, 400), (300, 425), width=7)


def openning_game():
    ecran.blit(image, image_rect)  # ecran de fond lancer avant la boucle
    out_of_txt("Welcom to Hangman Game", 450, 250, police)
    out_of_txt("Please press space to start the game", 450, 450, police2)


def win_or_loose():
    if winner == True:
        out_of_txt("You win!!", 250, 250, police)
    if loser == True:
        out_of_txt("You loose", 250, 250, police)


l_tuch = []
run = True
openning_game()
# ecran.blit(txt,txt_rect)


def send_to_hangman():
    l_aff, penalty, winner, loser = Pendu_for_pygame.hangman(
        l_tuch[-1], l_tuch, penalty, word
    )
    # on lance le jeux et on alimente avec le text du joueur


def debug_clav(l_tuch, ev):
    print("Le code généré est le suivant : ")
    print("     - event.dict['unicode'] : " + ev.dict["unicode"])
    print("     - event.key : " + str(ev.key))
    print("     - pygame.key.name(event.key) : " + pygame.key.name(ev.key))
    print(l_tuch)


while run:

    for ev in pygame.event.get():
        if (
            ev.type == pygame.QUIT
        ):  # passe a false le ev.type pour quiter la fenetre sur demande
            run = False

        # ecran.blit()
        if ev.type == pygame.KEYDOWN:
            clear_screen()
            l_tuch.append(
                pygame.key.name(ev.key)
            )  # liste des action clavier par le joueur
            # ecran.blit(image,image_rect) # affiche le text ecris par le joueur
            debug_clav(l_tuch, ev)

            if pygame.key.name(ev.key) == "space":  # debut de la partie
                clean_start()
                # mettre un sortie pour re start le jeu

            if pygame.key.name(ev.key) != "space":

                l_aff, penalty, winner, loser = Pendu_for_pygame.hangman(
                    l_tuch[-1], l_tuch, penalty, word
                )  # on lance le jeux et on alimente avec le text du joueur

                out_of_txt(l_aff, 500, 500, police)
                out_of_txt(str(penalty), 650, 50, police)

                win_or_loose()

    pygame.display.flip()

pygame.quit()


"""
Trouver comment rendre dynamqiue le text sur la page ->Ok
recueper les données tapées par l utilisateur -> Ok


pseudo code 

-Ouvrir la page  afficher bienvenue
-lorsque l utilisateur tape sur Espace , lancer le jeux . fixer dans un 1er temps les vie :
faire un cadre de la vie et cadre pour le mot secret
-afficher les mots cachées par les underscores et nb vie du joueur en haut a droite de l'ecran
-lorsque le joueur tape une lettre afficher la lettre si ok sinon donner la pénalité et affiche le pendu +1 faiere 
-
-



"""
