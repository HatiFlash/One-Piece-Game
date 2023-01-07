import pygame

#classe qui va gerer le projectile du joueur
class poing(pygame.sprite.Sprite) :

    #definir le constructeur de cette classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 10
        self.player = player
        self.image = pygame.image.load('jeu/canon.png')
        self.image = pygame.transform.scale(self.image, (20,20))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x +10
        self.rect.y = player.rect.y +20
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        # tourner le canon
        self.angle += 25
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)


    def move(self):
        self.rect.y -= self.velocity
        self.rotate()

        #verifier si le projectile entre en collision avec le pirate
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            #supprimer le canon
            self.remove()
            #infliger des degats aux pirate
            monster.damage(self.player.attack)
        #verifier si le projectile entre en collision avec le pirate
        for boss in self.player.game.check_collision(self, self.player.game.all_boss):
            #supprimer le canon
            self.remove()
            #infliger des degats au boss
            boss.damage(self.player.attack)

        # verifier si le shuriken n'est plus dans la fenetre
        if self.rect.y < -60:
            #supprimer le canon
            self.remove()
