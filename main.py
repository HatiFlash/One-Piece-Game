# Créé par hsbai, le 09/11/2020 en Python 3.4
import pygame
from game import Game
pygame.init()
pygame.mixer.init()
import time


# creer la fenetre principal
pygame.display.set_caption("Luffy Quest")
icon = pygame.image.load("jeu/icon.png")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((1200,680))

# importation du fond
fond = pygame.image.load('jeu/maps1.png')
fond = pygame.transform.scale(fond, (1200,680 ))

#importer le fond du menu
banner = pygame.image.load('jeu/menu.png')
fbanner = pygame.image.load('jeu/over.png')
fbanner = pygame.transform.scale(fbanner, (1200,680 ))

#importer le bouton pour lancer une parie
play_button = pygame.image.load('jeu/boutton.png')
play_button = pygame.transform.scale(play_button, (250,120 ))
play_button_rect = play_button.get_rect()
play_button_rect.x = 490
play_button_rect.y = 500

#importer le bouton pour relancer une parie
restart_button = pygame.image.load('jeu/restart.png')
restart_button = pygame.transform.scale(restart_button, (400, 150))
restart_button_rect = restart_button.get_rect()
restart_button_rect.x = 770
restart_button_rect.y = 820

#charger le jeu
game = Game()
#menu_music = pygame.mixer.Sound("jeu/epic.ogg")
#cry = pygame.mixer.Sound("jeu/cry.ogg")
#menu_music.play(1, 0, 1000)
#cry.play(0, 0, 1000)
attente=0

running = True

# tant que la boucle est vrai
while running:
    attente+=1
    #fenetre du jeu
    screen.blit(fond, (0,0))
    #verifier si le jeu a commencer
    if game.is_playing==1:#1= au jeu
        #declencher le jeu grace a def update
        game.update(screen)
    #verifier si le jeu n'a pas commencer
    elif game.is_playing==0:
        #ajouter l'ecran d'accueil
        screen.blit(banner, (-450, -250))
        screen.blit(play_button,(490, 500))
    elif game.is_playing==2:
        screen.blit(fbanner, (0, 0))
        screen.blit(restart_button, (400, 500))
        score_text = pygame.font.Font('PirateKids.otf',30).render("score: {0}".format(game.score),1,(255,0,0))
        screen.blit(score_text,(20,20))
        lvl_text = pygame.font.Font('PirateKids.otf',30).render("Niveau atteint: {0}".format(game.lvl),1,(255,0,0))
        screen.blit(lvl_text,(20,60))
        lvl_text = pygame.font.Font('PirateKids.otf',30).render("Canon tirer: {0}".format(game.canon),1,(255,0,0))
        screen.blit(lvl_text,(20,100))
        lvl_text = pygame.font.Font('PirateKids.otf',30).render("Super shuriken: {0}".format(game.supercanon),1,(255,0,0))
        screen.blit(lvl_text,(20,140))
        lvl_text = pygame.font.Font('PirateKids.otf',30).render("Pirate tuer: {0}".format(game.pirate),1,(255,0,0))
        screen.blit(lvl_text,(20,180))
        lvl_text = pygame.font.Font('PirateKids.otf',30).render("Boss tuer: {0}".format(game.killboss),1,(255,0,0))
        screen.blit(lvl_text,(20,220))

    #mettre a jour l'ecran
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")
        # detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detecter si la touche espace est declencher pour lancer le shuriken
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
                #punch = pygame.mixer.Sound("jeu/punch.ogg")
                #punch.play(0, 0, 0)
                game.canon += 1
            # detecter si la touche espace est declencher pour lancer le super shuriken
            if event.key == pygame.K_v and attente>200:
                attente=0
                game.player.launch_gomme()
                #punch = pygame.mixer.Sound("jeu/punch.ogg")
                #punch.play(0, 0, 0)
                game.supercanon += 1
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verifier si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos) :
                #mettre le jeu en mode lancer
                game.start()
                #menu_music.stop()
                #cry.stop()
                #play = pygame.mixer.Sound("jeu/play.ogg")
                #play.play(0, 0, 0)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verifier si la souris est en collision avec le bouton jouer
            if restart_button_rect.collidepoint(event.pos):
                #mettre le jeu en mode lancer
                game.start()
                #pygame.mixer.music.play("jeu/play.ogg")

