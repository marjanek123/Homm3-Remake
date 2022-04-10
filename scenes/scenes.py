from turtle import position
import pygame
import sys
import json
import numpy as np
import os
import settings
from map.terrain.grass import Grass
import resorce
from objects.object import Object
from units.hero import Heroes
import time
from pathfinding import astar
from spritesheet import spritesheet
import resorce
import asyncio


class Game:
    def __init__(self):
        self.units = []
        self.terrain = []
        self.objects = []
        self.maze = np.zeros([settings.X, settings.Y], dtype=int)
        self.map = self.genereate_map()
        self.objects_map = self.creatae_objects()
        self.units.append(Heroes(1, (0, 0), resorce.resorce.hero1))
        self.presed = False

    def genereate_map(self):
        with open("scenes/bg_map.json") as bg:
            data = json.load(bg)
        # with open("map/bg_object.json") as fr:
        #     ob_data = json.load(fr)
        for x in range(settings.Y*settings.X):
            t = data[x]["t"]
            p = data[x]["pos"]

            with open("scenes/bg_object.json") as fr:
                ob_data = json.load(fr)
            for a in range(len(ob_data)):
                if ob_data[a]["terainbg"] == t:
                    self.terrain.append(Grass(pygame.image.load(os.path.join(
                        'assets', 'image', "{}".format(ob_data[a]["imgbg"]))), data[x]["pos"]))

    def creatae_objects(self):
        with open("scenes/maplypleyerobjects.json") as f:
            data = json.load(f)
        for count1 in range(0, len(data)):
            obj = data[count1]["ob"]
            pos = data[count1]["pos"]
            with open("scenes/maplyobj.json") as fr:
                cdata = json.load(fr)
            for a in range(0, len(cdata)):
                if cdata[a]["ob"] == data[count1]["ob"]:
                    self.get_object(cdata[a]["terrain"], data[count1]["pos"])
                    self.objects.append(Object(cdata[a]["ob"], pygame.image.load(os.path.join(
                        'assets', 'image', "{}".format(cdata[a]["img"]))), cdata[a]["terrain"], data[count1]["pos"]))

    def get_object(self, a1, a2):

        a = a2[0]
        b = a2[1]
        c = a1
        x1 = 0
        y1 = 0
        x = a
        y = b

        for row in range(len(a2)+2):

            y = b
            y1 = 0
            x += 1
            for col in range(len(a1)+1):
                try:
                    if self.maze[x-1][y] == 0 and c[x1][y1] == 0:
                        pass
                    elif self.maze[x-1][y] == 1 and c[x1][y1] == 0:
                        pass
                    elif self.maze[x-1][y] == 1 and c[x1][y1] >= 2:
                        pass
                    elif self.maze[x-1][y] >= 2:
                        pass
                    else:
                        self.maze[x-1][y] = c[x1][y1]
                except IndexError:
                    pass

                y += 1
                y1 += 1
            x1 += 1


class Scene:

    def __init__(self, screen):
        super().__init__()
        self.array_of_scenes = ["menu", "game"]
        self.current_scene = "menu"
        self.screen = screen
        self.units = []
        # self.presed = pygame.mouse.get_pressed()

    def menu(self):
        # Initialize game variables as the player, enemies and such.

        # Handle events.

        for event in pygame.event.get():
            # przechwyć zamknięcie okna
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:    # Go to menu if you press A.
                    self.current_scene = "game"

        # Update the menu (like buttons, settings, ...).

        # Draw the shop.
        self.screen.fill((0, 0, 255))  # A green menu.
        pygame.display.update()

    def game(self):
        # Initialize game variables as the player, enemies and such.
        game = Game()
        play = True
        pressed1 = False
        click_time = time.time()
        selected_Hero = None
        selected_Town = None
        path = None
        traveling = False
        img = spritesheet(resorce.resorce.arrows)
        image = img.images_at(((790, 0, 32, 32), (790 + 3*32, 0, 32, 32), (790 + 2*32, 0+32, 32, 32), (790 + 3*32, 0, 32, 32), (790 + 2*32, 0+3*32, 32, 32), (790 + 4*32, 0+1*32, 32, 32), (790 + 5*32, 0, 32, 32), (790 + 6*32, 0, 32, 32), (790 + 5*32, 0+1*32, 32, 32), (790, 210, 32, 32)),
                              colorkey=(255, 255, 255))
        while play:
            for event in pygame.event.get():
                # przechwyć zamknięcie okna
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_b:    # Go to menu if you press A.

                        self.current_scene = "menu"
                        play = False
            with open("scenes/maplypleyerobjects.json") as f:
                data = json.load(f)
                # print(len(game.objects))

        # Update the game.

        # Draw your game.
            # self.cursor = pygame.mouse.get_pos()
            # print(pygame.mouse.get_pos())

            # if(pygame.mouse.get_pressed == True):
                # print('PRESED')

            # if event.type == pygame.MOUSEBUTTONUP and self.presed == True:
            #     self.presed == False
            # print(pygame.mouse.get_pressed()[0])
                # selected_Hero.path[:-1]
                # if(selected_Hero.path == []):
                #     traveling = False
                # selected_Hero.path.pop()

            if(pygame.mouse.get_pressed()[0] and pressed1 == False):
                mouse_pos = pygame.mouse.get_pos()
                point = (mouse_pos[0] // 32, mouse_pos[1] // 32)
                print(mouse_pos)
                print(selected_Hero)
                for element in game.units:
                    if element.pos[0] - 32 <= mouse_pos[0] and element.pos[0] + 32 >= mouse_pos[0] and element.pos[1]-32 <= mouse_pos[1] and element.pos[1]+32 >= mouse_pos[1]:
                        selected_Hero = element
                    print(path)

                if(selected_Hero):
                    print(selected_Hero.path)
                    if(game.maze[point[0]][point[1]] == 0):
                        selected_Hero.path = astar(
                            game.maze, selected_Hero.pos, (mouse_pos[0] // 32, mouse_pos[1] // 32,))
                        if (selected_Hero.go_point == (mouse_pos[0] // 32, mouse_pos[1] // 32,)):
                            selected_Hero.moving = True

                        else:
                            selected_Hero.go_point = (
                                mouse_pos[0] // 32, mouse_pos[1] // 32,)
                    else:
                        pass

                print(time.time() - click_time)
                click_time = time.time()
                # print(time.time() - click_time)
                pressed1 = True
                print("presed")

            if(not pygame.mouse.get_pressed()[0] and pressed1 == True):
                pressed1 = False
                print("resolved")

            # if(pressed1):
            #     # game.presed == False
            #     print("presed")

            self.screen.fill((0, 255, 0))  # A blue game.
            for a in game.terrain:
                self.screen.blit(a.image, (settings.DISPLAY[0]/2 - settings.X*32/2 +
                                 a.pos[0]*32, settings.DISPLAY[1]/2 - settings.X*32/2 + a.pos[1]*32))
            for o in game.objects:
                self.screen.blit(o.image, (settings.DISPLAY[0]/2 - settings.X*32/2 +
                                 o.pos[0]*32, settings.DISPLAY[1]/2 - settings.X*32/2 + o.pos[1]*32))
            for hero in game.units:
                self.screen.blit(hero.image, (settings.DISPLAY[0]/2 - settings.X*32/2 +
                                 hero.pos[0]*32, settings.DISPLAY[1]/2 - settings.X*32/2 + hero.pos[1]*32))
            # self.screen.blit(image[1], (34, 54))
            if(selected_Hero):
                costs = selected_Hero.moving_cost
                for arrow in selected_Hero.path[::-1]:
                    if(costs - arrow[1] > 0):
                        costs -= arrow[1]
                        self.screen.blit(
                            image[0], (arrow[0][0]*32, arrow[0][1]*32))
                    else:
                        costs -= arrow[1]
                        self.screen.blit(
                            image[9], (arrow[0][0]*32, arrow[0][1]*32))
            pygame.display.update()

            if(selected_Hero):
                if(selected_Hero.moving):
                    selected_Hero.move()

    def run_scene(self):
        if self.current_scene == "menu":
            self.menu()
        else:
            self.game()
