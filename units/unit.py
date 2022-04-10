
import pygame
import sys
import settings

class Unit:
    def __init__(self,hp,atack,player,pos_x,pos_y,img, screen):
        
        self.screen=screen
        self.img=img
        self.hp=hp
        self.left_hp=hp
        self.target=None
        self.atack=atack
        self.player=player
        self.travel=False
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.travel_pos_x=0
        self.travel_pos_y=0
    
    def move(self):
        if( self.pos_x == self.travel_pos_x and self.pos_y == self.travel_pos_y ):
            self.travel=False
    def hit(self,hit):
        self.hp-=hit
        if(self.hp<=0):
            return True
    def fight(self):
        pass
    def draw(self):
        pygame.draw.ellipse(self.screen, settings.WHITE, (self.pos_x - settings.UNIT_WIDTH/2 ,self.pos_y - settings.UNIT_HEIGHT/2,settings.UNIT_WIDTH,settings.UNIT_HEIGHT))
        

    
        