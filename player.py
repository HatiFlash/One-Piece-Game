import pygame
from projectile import poing
from super_projectile import gomme
imgPersos=[pygame.image.load("jeu/l2.png"),pygame.image.load("jeu/l3.png"),pygame.image.load("jeu/l4.png"),pygame.image.load("jeu/l5.png"),pygame.image.load("jeu/l6.png"),pygame.image.load("jeu/l7.png")]
imgPersosR=[pygame.image.load("jeu/l2r.png"),pygame.image.load("jeu/l3r.png"),pygame.image.load("jeu/l4r.png"),pygame.image.load("jeu/l5r.png"),pygame.image.load("jeu/l6r.png"),pygame.image.load("jeu/l7r.png")]

#creation des stats joueur
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 50
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.all_gommes = pygame.sprite.Group()
        self.image = pygame.image.load('jeu/luffy1.png')
        self.image = pygame.transform.scale(self.image, (120, 135))
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 500
        self.current_image = 0
        self.current_count = 0


    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            #si le joueur n'a plus de pv
            self.game.game_over()

    def update_health_bar(self, surface):
        #dessiner la barre de vie
        pygame.draw.rect(surface, (99, 122, 98), [self.rect.x + 7, self.rect.y -16, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 7, self.rect.y -16, self.health, 7])

    def launch_projectile(self):
        #creer une nouvelle instance de la classe projectile
        self.all_projectiles.add(poing(self))

    def launch_gomme(self):
        #creer une nouvelle instance de la classe projectile
        self.all_gommes.add(gomme(self))

    def move_right(self):
        #si le joueur n'est pas en contact avec un pirate
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity
        self.current_count += 1
        if self.current_count == 5:
            self.current_count = 0
            self.current_image += 1
            if self.current_image == 5:
                self.current_image = 0
            self.image = imgPersosR[self.current_image]
            self.image = pygame.transform.scale(self.image, (90,105))

    def move_left(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x -= self.velocity
        self.current_count += 1
        if self.current_count == 5:
            self.current_count = 0
            self.current_image += 1
            if self.current_image == 5:
                self.current_image = 0
            self.image = imgPersos[self.current_image]
            self.image = pygame.transform.scale(self.image, (90,105))


    def move_up(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            if self.rect.y > 0:
                self.rect.y -= self.velocity

    def move_down(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            if self.rect.y < 680:
                self.rect.y += self.velocity