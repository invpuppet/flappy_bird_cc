import pygame
import random
import math
import os
import time
pygame.font.init()

WIN_WIDTH = 500
WIN_HEIGHT = 800

BACKGROUND = pygame.tranform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))

def draw_window(win):
    win.blit(BACKGROUND, (0, 0))
    pygame.display.update()


def main():
    run = True
    win = pygame.desplay.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()

    while (run):
