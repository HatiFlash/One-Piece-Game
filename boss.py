#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hsbai
#
# Created:     17/11/2020
# Copyright:   (c) hsbai 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pygame
import random
from kick import kick
#importation des image de pirate
imgPerso=[pygame.image.load("jeu/b1.png"),pygame.image.load("jeu/b2.png"),pygame.image.load("jeu/b3.png"),pygame.image.load("jeu/b4.png"),pygame.image.load("jeu/b5.png"),pygame.image.load("jeu/b6.png"),pygame.image.load("jeu/b7.png"),pygame.image.load("jeu/b8.png")]
imgPersor=[pygame.image.load("jeu/b1r.png"),pygame.image.load("jeu/b2r.png"),pygame.image.load("jeu/b3r.png"),pygame.image.load("jeu/b4r.png"),pygame.image.load("jeu/b5r.png"),pygame.image.load("jeu/b6r.png"),pygame.image.load("jeu/b7r.png"),pygame.image.load("jeu/b8r.png")]
#creer une classe pour le monstre sur le jeu
class Boss(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 150
        self.max_health = 150
        self.attack = 20
        self.all_kicks = pygame.sprite.Group()
        self.image = pygame.image.load('jeu/b1.png')
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 20
        self.velocity = random.randint(1, 4)
        self.imgPerso = imgPerso
        self.numpic = 0
        self.dy = 0
        self.dir = 0
        self.current_image = 0
        self.current_count = 0


    def animate(self):
        self.current_count += 1
        if self.velocity<0 :
            if self.current_count == 7:
                self.current_count = 0
                self.current_image += 1
            if self.current_image == 7:
                self.current_image = 0
            self.image = imgPerso[self.current_image]
            self.image = pygame.transform.scale(self.image, (100,100))
        else:
            if self.current_count == 7:
                self.current_count = 0
                self.current_image += 1
            if self.current_image == 7:
                self.current_image = 0
            self.image = imgPersor[self.current_image]
            self.image = pygame.transform.scale(self.image, (100,100))




    def damage(self, amount):
        #infliger les degats
        self.health -= amount

        #verifier si son nouveau nb de points de vie est inferieur ou egale a 0
        if self.health <= 0:
            #reapparaitre comme un nouveau monstre
            self.rect.x = 500
            self.rect.y = 40
            self.velocity = random.randint(1, 3)
            self.health = self.max_health
            pirate_spawn = pygame.mixer.Sound("jeu/doflamingo.ogg")
            pirate_spawn.play(0, 0, 100)
            self.game.score += 10
            self.game.killboss += 1

            #niveau du score
            if self.game.score == 10:
                self.game.lvl += 1
            if self.game.score == 20:
                self.game.lvl += 1
            if self.game.score == 30:
                self.game.lvl += 1
            if self.game.score == 40:
                self.game.lvl += 1
            if self.game.score == 50:
                self.game.lvl += 1
            if self.game.score == 60:
                self.game.lvl += 1
            if self.game.score == 70:
                self.game.lvl += 1
            if self.game.score == 80:
                self.game.lvl += 1
            if self.game.score == 90:
                self.game.lvl += 1
            if self.game.score == 100:
                self.game.lvl += 1
            if self.game.score == 110:
                self.game.lvl += 1
            if self.game.score == 120:
                self.game.lvl += 1
            if self.game.score == 130:
                self.game.lvl += 1
            if self.game.score == 140:
                self.game.lvl += 1

    def launch_kick(self):
        #creer une nouvelle instance de la classe projectile
        self.all_kicks.add(kick(self))

    def update_health_bar(self, surface):
        #dessiner la barre de vie
        pygame.draw.rect(surface, (99, 122, 98), [self.rect.x - 2, self.rect.y - 10, self.max_health, 4])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x - 2, self.rect.y - 10, self.health, 4])

    def remove(self):
        self.game.all_boss.remove(self)

    #si le monstre touche le bas de l'ecran
    def forward(self):
        if self.rect.y > 700:
            self.remove()
            self.game.game_over()

        #deplacement s'effectue que si il n'y a pas de collision avec un groupe de joueur
        elif not self.game.check_collision(self, self.game.all_players):
            self.rect.x += self.velocity
            if self.rect.x>670:
                self.rect.x=670
                self.velocity=-self.velocity
            if self.rect.x<480:
                self.rect.x=480
                self.velocity=-self.velocity

        else:
            #infliger les degats au joueur
            self.game.player.damage(self.attack)
            # verifier si le shuriken n'est plus dans la fenetre
            if self.rect.y < -60:
                # supprimer le shuriken
                self.remove()
