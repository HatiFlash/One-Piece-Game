
import pygame

#classe qui va gerer le projectile du joueur
class kick(pygame.sprite.Sprite) :

    #definir le constructeur de cette classe
    def __init__(self, boss):
        super().__init__()
        self.velocity = 6
        self.boss = boss
        self.image = pygame.image.load('jeu/canon.png')
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()
        self.rect.x = boss.rect.x +1
        self.rect.y = boss.rect.y +2
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        # tourner le canon
        self.angle += 25
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.boss.all_kicks.remove(self)


    def move(self):
        self.rect.y += self.velocity
        self.rotate()

        #verifier si le projectile entre en collision avec le pirate
        for player in self.boss.game.check_collision(self, self.boss.game.all_players):
            #supprimer le canon
            self.remove()
            #infliger des degats aux joueur
            player.damage(self.boss.attack)

        # verifier si le canon rouge n'est plus dans la fenetre
        if self.rect.y > 700:
            #supprimer le canon
            self.remove()
