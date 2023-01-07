#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hsbai
#
# Created:     16/11/2020
# Copyright:   (c) hsbai 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame

#classe qui va gerer le projectile du joueur
class gomme(pygame.sprite.Sprite):

    #definir le constructeur de cette classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 8
        self.player = player
        self.image = pygame.image.load('jeu/shuriken1.png')
        self.image = pygame.transform.scale(self.image, (60,60))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 10
        self.rect.y = player.rect.y + 20
        self.origin_image = self.image
        self.angle = 0
        self.current_image = 0
        self.current_count = 0

    def rotate(self):
        # tourner le shuriken
        self.angle += 25
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_gommes.remove(self)


    def move(self):
        self.rect.y -= self.velocity
        self.rotate()

        #verifier si le projectile entre en collision avec le pirate
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            #supprimer le shuriken
            #infliger des degats aux pirate
            monster.damage(self.player.attack)
        #verifier si le projectile entre en collision avec le pirate
        for boss in self.player.game.check_collision(self, self.player.game.all_boss):
            #supprimer le shuriken
            #infliger des degats aux pirate
            boss.damage(self.player.attack)

        # verifier si le shuriken n'est plus dans la fenetre
        if self.rect.y < 250:
            #supprimer le shuriken
            self.remove()




