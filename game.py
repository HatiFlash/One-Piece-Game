import pygame
pygame.init()
pygame.mixer.init()
from boss import Boss
from player import Player
from monster import Monster

#creer une seconde classe qui va representer le jeu
class Game:

    def __init__(self):
        #definir si le jeu a commencer ou non
        self.is_playing = 0
        #generer le joueur a chaque partie creer
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #groupe de pirate
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.monster = Monster(self)
        #boss
        self.all_boss = pygame.sprite.Group()
        self.pressed = {}
        self.boss = Boss(self)
        self.attente=0
        #statistique
        self.score = 0
        self.lvl = 0
        self.killboss=0
        self.pirate=0
        self.canon=0
        self.supercanon=0
        #self.music = pygame.mixer.Sound("jeu/game_over.mp3")


    def start(self):
        self.score = 0
        self.lvl = 0
        self.killboss=0
        self.pirate=0
        self.canon=0
        self.supercanon=0
        self.is_playing = 1
        #menu_music = pygame.mixer.Sound("jeu/epic.ogg")
        # m enu_music.stop()
        self.spawn_boss()
        self.spawn_monster()
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self,):
        # remettre le jeu 0 (reinitialiser toute la map)
        self.all_monsters = pygame.sprite.Group()
        self.all_boss = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.player.attack = 40
        self.is_playing = 2
        pygame.mixer.pause()
    def update(self, screen):
        self.attente+=1
        if self.attente>100:
            self.boss.launch_kick()
            self.attente=0
        # mettre l'image du joueur
        screen.blit(self.player.image, self.player.rect)

        self.update_score(screen)

        self.update_lvl(screen)

        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        # appliquer l'ensemble des image du shuriken
        self.player.all_projectiles.draw(screen)
        self.player.all_gommes.draw(screen)
        self.boss.all_kicks.draw(screen)

        # appliquer l'ensemble des image du groupe de pirate
        self.all_monsters.draw(screen)
        self.all_boss.draw(screen)

        # recuperer les shuriken du joueur
        for projectiles in self.player.all_projectiles:
            projectiles.move()

        # recuperer les super shuriken du joueur
        for projectiles in self.player.all_gommes:
            projectiles.move()

        #recuper le canon du boss
        for kick in self.boss.all_kicks:
            kick.move()




        # recuperer les pirates de notre jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.animate()
            monster.update_health_bar(screen)

        # recuperer le boss de notre jeu
        for boss in self.all_boss:
            boss.forward()
            boss.animate()
            boss.update_health_bar(screen)

        # verifier les touche
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 700:
            self.player.move_right()
        if self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 370:
            self.player.move_left()
        if self.pressed.get(pygame.K_UP) and self.player.rect.y < 980:
            self.player.move_up()
        if self.pressed.get(pygame.K_DOWN) and self.player.rect.y < 540:
            self.player.move_down()

    #affichage du score
    def update_score(self, screen):
        score_text = pygame.font.Font('PirateKids.otf',30).render("score: {0}".format(self.score),1,(0,0,0))
        screen.blit(score_text,(20,20))
        if self.score > 10:
            self.player.attack = self.player.attack = 50-20
            self.monster.velocity = self.monster.velocity = +3


    #affichage du niveau
    def update_lvl(self, screen):
        lvl_text = pygame.font.Font('PirateKids.otf',30).render("Niveau: {0}".format(self.lvl),1,(9,237,77))
        screen.blit(lvl_text,(20,60))


    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)

    def spawn_boss(self):
        boss = Boss(self)
        self.all_boss.add(boss)

    def update_canon(self, screen):
        lvl_text = pygame.font.Font('PirateKids.otf',30).render("Niveau: {0}".format(self.canon),1,(9,237,77))

    def update_supercanon(self, screen):
        lvl_text = pygame.font.Font('PirateKids.otf',30).render("Niveau: {0}".format(self.supercanon),1,(9,237,77))

    def update_pirate(self, screen):
        lvl_text = pygame.font.Font('PirateKids.otf',30).render("Niveau: {0}".format(self.pirate),1,(9,237,77))

    def update_doflamingo(self, screen):
        lvl_text = pygame.font.Font('PirateKids.otf',30).render("Niveau: {0}".format(self.killboss),1,(9,237,77))



