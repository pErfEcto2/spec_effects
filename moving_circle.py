import pgzrun as pgr
import pgzero as pgz
import pygame as pg
import random as ran
import os
import lib
from lib import WIDTH, HEIGHT, DEPTH, LENGTH
import math


w = lib.Walker3D(pg.Vector3(WIDTH / 2, HEIGHT / 2, DEPTH / 2), 50, pg.Vector3(WIDTH, HEIGHT, DEPTH))

def update():
    w.move()
    pass

def draw():
    screen.fill((0, 0, 0))
    w.modRadius()
    screen.draw.filled_circle(pos=w.getPos(), radius=w.getVisibleRadius(), color=w.getColor())

pgr.go()
