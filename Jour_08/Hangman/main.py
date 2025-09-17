import pygame
#import Pendu_give_us_more

pygame.init()

ecran=pygame.display.set_mode((600,600))
image = pygame.image.load("wallpaper_game.xcf").convert() # charge l image de fond
Blanc = (255, 255, 255)
pygame.display.set_caption("The Hangman") # titre du la fenetre
police = pygame.font.SysFont('Arial', 70, False, True) # style d'ecriture pour le jeu

z_txt= police.render("txt" ,True,Blanc)
#txt_zone=police.get_rect(250,450) # objet de la zone de txt



def manstick():

    #pygame.draw.line(ecran,(0,0,0),(10,10),(100,100),width=10)
    pygame.draw.line(ecran,(0,0,0),(50,550),(100,550),width=7)
    pygame.draw.line(ecran,(0,0,0),(50,550),(75,500),width=7)
    pygame.draw.line(ecran,(0,0,0),(100,550),(75,500),width=7)
    
    # base
    
    pygame.draw.line(ecran,(0,0,0),(75,500),(75,400),width=7)
    pygame.draw.line(ecran,(0,0,0),(75,400),(75,300),width=7)
    pygame.draw.line(ecran,(0,0,0),(75,300),(75,200),width=7)
    #Mat
    pygame.draw.line(ecran,(0,0,0),(75,200),(175,200),width=7)
    pygame.draw.line(ecran,(0,0,0),(175,200),(275,200),width=7)
    #corde
    pygame.draw.line(ecran,(0,0,0),(275,200),(275,300),width=7)
    #man
    pygame.draw.circle(ecran,(0,0,0),(275,300),20)
    pygame.draw.line(ecran,(0,0,0),(275,300),(275,400),width=7)
    #Bras
    pygame.draw.line(ecran,(0,0,0),(275,350),(250,325),width=9)
    pygame.draw.line(ecran,(0,0,0),(275,350),(300,325),width=9)

    #Jambe
    pygame.draw.line(ecran,(0,0,0),(275,400),(250,425),width=7)
    pygame.draw.line(ecran,(0,0,0),(275,400),(300,425),width=7)


run = True
while run:
    ecran.blit(image,(0,0))

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: # passe a false le ev.type pour quiter la fenetre sur demande
            run = False
            
        #ecran.blit()
        """
        if ev.type == pygame.KEYDOWN:
                print("Le code généré est le suivant : ")
                print("     - event.dict['unicode'] : " + ev.dict['unicode'])
                print("     - event.key : " + str(ev.key))
                print("     - pygame.key.name(event.key) : " + pygame.key.name(ev.key))
        """
            
    pygame.display.flip()

pygame.quit()

    
