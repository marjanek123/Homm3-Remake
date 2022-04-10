
from ast import While
import pygame
import sys
import settings
import time
import asyncio


class Heroes:
    def __init__(self, player, pos, image, ):

        self.image = image
        self.player = player
        self.pos = pos
        self.move_time = time.time()
        self.moving = False
        self.go_point = None
        self.path = None
        self.moving_cost = 1500

    def __str__(self):
        return "hero 0 "

    def __repr__(self):
        return True

    # @classmethod
    def move(self):
        if(self.path != []):
            print(self.path[::-1][0][1])
            if(self.moving_cost - self.path[::-1][0][1] > 0):
                time.sleep(0.3)
                self.moving_cost -= self.path[::-1][0][1]
                self.pos = self.path.pop()[0]
            else:
                self.moving = False
        else:
            self.moving = False

    # def hit(self,hit):
    #     self.hp-=hit
    #     if(self.hp<=0):
    #         return True
    # def fight(self):
    #     pass

    def draw(self):
        self.screen.blit(self.image, (settings.DISPLAY[0]/2 - settings.X*32/2 +
                         self.pos[0]*32, settings.DISPLAY[1]/2 - settings.X*32/2 + self.pos[1]*32))
