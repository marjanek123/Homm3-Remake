
import pygame
import sys
import settings


class Object:
    def __init__(self, name, image, shape, pos):
        self.name = name
        self.image = image
        # self.image.set_shifts((5,35,23,245))
        self.shape = shape
        self.pos = pos

    # def move(self):
    #     if( self.pos_x == self.travel_pos_x and self.pos_y == self.travel_pos_y ):
    #         self.travel=False
    # def hit(self,hit):
    #     self.hp-=hit
    #     if(self.hp<=0):
    #         return True
    # def fight(self):
    #     pass

    def draw(self):
        self.screen.blit(self.image, (settings.DISPLAY[0]/2 - settings.X*32/2 +
                         self.pos[0]*32, settings.DISPLAY[1]/2 - settings.X*32/2 + self.pos[1]*32))
