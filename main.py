from world1 import World
from agent import Agent
import pygame
import time

def main():
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 800

    game = World(SCREEN_WIDTH,SCREEN_HEIGHT,"Terrifying")

    clock = pygame.time.Clock()
    t = 0
    loop = True
    while loop:
        loop = game.update()
        if (time.time() % 7 == 0):
            game.randomWorld()
            t = 0
        game.draw()
        clock.tick(60)
        t += 1

main()
