
import pygame
import settings
import sys
from units.unit import Unit
from units.swordsman import Swordsman
from scenes.scenes import Scene
pygame.init()
# settings
height = 16
width = 16


screen = pygame.display.set_mode(settings.DISPLAY)
clock = pygame.time.Clock()
# ^^^^^^^^^

# map_units.append(Swordsman(40,4,1,150,150,4,screen))
# map_units.append(Swordsman(40,4,1,120,250,4,screen))
window_scene = Scene(screen)


######## my#############
def loop(window_scene):
    while True:
        clock.tick(settings.FPS)

        window_scene.run_scene()


loop(window_scene)
