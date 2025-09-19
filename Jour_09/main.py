import pygame
import Pendu_for_pygame
import string

pygame.init()

ecran = pygame.display.set_mode((900, 600))
image = pygame.image.load("Black_bord_resized.png").convert()  # charge l image de fond
Blanc = (255, 255, 255)
pygame.display.set_caption("The Hangman")  # titre du la fenetre
police = pygame.font.Font("Neat_Chalk.ttf", 30)  # style d'ecriture pour le jeu
police2 = pygame.font.Font("Neat_Chalk.ttf", 15)
police_point = pygame.font.Font("Neat_Chalk.ttf", 45)
police_crai = pygame.font.Font("Neat_Chalk.ttf", 70)
police_crai2 = pygame.font.Font("Neat_Chalk.ttf", 45)


# intialisation des parametre du jeu
# l_aff=[""]
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

    out_of_txt(l_aff, 500, 500, police_crai)


def manstick(penalty):

    # pygame.draw.line(ecran,(0,0,0),(10,10),(100,100),width=10)
    if penalty >= 1:
        pygame.draw.line(ecran, (Blanc), (50, 550), (100, 550), width=7)
        pygame.draw.line(ecran, (Blanc), (50, 550), (75, 500), width=7)
        pygame.draw.line(ecran, (Blanc), (100, 550), (75, 500), width=7)

    # base
    if penalty >= 2:
        pygame.draw.line(ecran, (Blanc), (75, 500), (75, 400), width=7)
    if penalty >= 3:
        pygame.draw.line(ecran, (Blanc), (75, 400), (75, 300), width=7)
    if penalty >= 4:
        pygame.draw.line(ecran, (Blanc), (75, 300), (75, 200), width=7)
    if penalty >= 5:
        pygame.draw.line(ecran, (Blanc), (75, 200), (175, 200), width=7)
    if penalty >= 6:
        pygame.draw.line(ecran, (Blanc), (175, 200), (275, 200), width=7)
    if penalty >= 7:
        pygame.draw.line(ecran, (Blanc), (275, 200), (275, 300), width=7)
    if penalty >= 8:
        pygame.draw.circle(ecran, (Blanc), (275, 300), 20)
    if penalty >= 9:
        pygame.draw.line(ecran, (Blanc), (275, 300), (275, 400), width=7)
    if penalty >= 10:
        pygame.draw.line(ecran, (Blanc), (275, 350), (250, 325), width=9)
    if penalty >= 11:
        pygame.draw.line(ecran, (Blanc), (275, 350), (300, 325), width=9)
    if penalty >= 12:
        pygame.draw.line(ecran, (Blanc), (275, 400), (250, 425), width=7)
    if penalty >= 13:
        pygame.draw.line(ecran, (Blanc), (275, 400), (300, 425), width=7)

    # Mat
    # corde
    # man
    # Bras

    # Jambe


def openning_game():
    ecran.blit(image, image_rect)  # ecran de fond lancer avant la boucle
    out_of_txt("Welcom to Hangman Game", 450, 250, police)
    out_of_txt("Please press space to start the game", 450, 450, police2)


def win_or_lose(winner=False, loser=False):
    if winner == True:
        out_of_txt("You win!!", 250, 250, police)
        pygame.display.flip()
        pygame.time.delay(4000)
        pygame.quit()

    if loser == True:
        out_of_txt("You lose", 250, 250, police)
        out_of_txt(f"The word was : {word}", 400, 330, police)
        pygame.display.flip()
        pygame.time.delay(4000)
        pygame.quit()


l_tuch = []

run = True
openning_game()  # ouverture et message de bienvenue


def debug_clav(l_tuch, ev):
    print("Le code généré est le suivant : ")
    print("     - event.dict['unicode'] : " + ev.dict["unicode"])
    print("     - event.key : " + str(ev.key))
    print("     - pygame.key.name(event.key) : " + pygame.key.name(ev.key))
    print(ev.type)


while run:

    for ev in pygame.event.get():
        # print(ev.type)
        if ev.type == pygame.QUIT:  # 768 = escape
            # passe a false le ev.type pour quiter la fenetre sur demande
            run = False

        # ecran.blit()
        if ev.type == pygame.KEYDOWN:
            clear_screen()
            l_tuch.append(pygame.key.name(ev.key))
            # liste des action clavier par le joueur
            # ecran.blit(image,image_rect) # affiche le text ecris par le joueur
            # debug_clav(l_tuch, ev)

            if ev.key == pygame.K_ESCAPE:
                run = False
                break

            if pygame.key.name(ev.key) == "space":  # debut de la partie
                clean_start()
                # mettre un sortie pour re start le jeu

            if (
                pygame.key.name(ev.key) != "space"
                and pygame.key.name(ev.key) in string.ascii_letters
            ):

                # envoie des données au hangman
                l_aff, penalty, winner, loser = Pendu_for_pygame.hangman(
                    l_tuch[-1], l_tuch, penalty, word
                )

                # on lance le jeux et on alimente avec le text du joueur

                out_of_txt(l_aff, 500, 500, police_crai)
                out_of_txt(str(penalty), 750, 80, police)

                manstick(penalty)
                win_or_lose(winner, loser)

                """
                if winner or loser and pygame.key.name(ev.key) == "r":
                    pygame.quit()
                    # print("#### relance ####")
                """
                # faire un restarte avec  un clic sourie

    pygame.display.flip()  # update la page

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
-gere les lettre par un enter 

-
"""
