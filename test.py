import math
import pgzrun as pgr
import pgzero as pgz
import pygame as pg
import random as ran
import os

WIDTH  = 1000
HEIGHT = 600
DEPTH  = 600
LENGTH = 100
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

bg = pg.image.load("src/img.jpg")
img = pg.image.load("src/texture.png").convert_alpha()
img = pg.transform.scale(img, (320, 320))

def update():
    pass

def draw():
    screen.fill((0, 0, 0))
    screen.blit(img, (0, 0))

pgr.go()