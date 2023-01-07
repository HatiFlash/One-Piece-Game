import pygame
import random

#importation des image de pirate
imgPerso=[pygame.image.load("jeu/p1.png"),pygame.image.load("jeu/p2.png"),pygame.image.load("jeu/p3.png"),pygame.image.load("jeu/p4.png"),pygame.image.load("jeu/p5.png")]

#creer une classe pour le monstre sur le jeu
class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pygame.image.load('jeu/pirate.png')
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
        if self.current_count == 7:
            self.current_count = 0
            self.current_image += 1
            if self.current_image == 4:
                self.current_image = 0
            self.image = imgPerso[self.current_image]
            self.image = pygame.transform.scale(self.image, (90,90))


    def damage(self, amount):
        #infliger les degats
        self.health -= amount

        #verifier si son nouveau nb de points de vie est inferieur ou egale a 0
        if self.health <= 0:
            #reapparaitre comme un nouveau monstre
            self.rect.x = 500 + random.randint(0,100 )
            self.rect.y = 20 + random.randint(0, 60)
            self.velocity = random.randint(1, 2)
            self.health = self.max_health
            #pirate_spawn = pygame.mixer.Sound("jeu/pirate_spawn.ogg")
            #pirate_spawn.play(0, 0, 100)
            self.game.score += 1
            self.game.pirate += 1
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



    def update_health_bar(self, surface):
        #dessiner la barre de vie
        pygame.draw.rect(surface, (99, 122, 98), [self.rect.x - 2, self.rect.y - 10, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x - 2, self.rect.y - 10, self.health, 5])

    def remove(self):
        self.game.all_monsters.remove(self)

    #si le monstre touche le bas de l'ecran
    def forward(self):
        if self.rect.y > 700:
            self.remove()
            self.game.game_over()

        #deplacement s'effectue que si il n'y a pas de collision avec un groupe de joueur
        elif not self.game.check_collision(self, self.game.all_players):
            self.rect.y += self.velocity
        else:
            #infliger les degats au joueur
            self.game.player.damage(self.attack)
            # verifier si le shuriken n'est plus dans la fenetre
            if self.rect.y < -60:
                # supprimer le shuriken
                self.remove()
