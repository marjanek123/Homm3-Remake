import pygame
import os


class Resorces:
    def __init__(self):

        self.dirt2 = pygame.image.load(
            os.path.join('assets', 'image', "dirt2.PNG"))
        self.dirt3 = pygame.image.load(
            os.path.join('assets', 'image', "dirt3.PNG"))
        self.dirt4 = pygame.image.load(
            os.path.join('assets', 'image', "dirt4.PNG"))
        self.dirt5 = pygame.image.load(
            os.path.join('assets', 'image', "dirt5.PNG"))
        self.dirt6 = pygame.image.load(
            os.path.join('assets', 'image', "dirt6.PNG"))
        self.dirt7 = pygame.image.load(
            os.path.join('assets', 'image', "dirt7.PNG"))
        self.dirt8 = pygame.image.load(
            os.path.join('assets', 'image', "dirt8.PNG"))
        self.hero = pygame.image.load(
            os.path.join('assets', 'image', "player1.PNG"))
        self.hero1 = pygame.transform.scale(self.hero, (60, 60))

        self.arrows = pygame.image.load(
            os.path.join('assets', 'image', "41280.png"))


resorce = Resorces()
