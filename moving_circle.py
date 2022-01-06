import random as ran
from typing import Sized
import pgzero as pgz
import pgzrun as pgr
import pygame as pg
import lib
from lib import HEIGHT, WIDTH
import sys

a = 10000 # accelerate
g = 10000 # gravity
maxSpeed = 5
n = 100 # number of circles
p = 0.01 # density of air
k = 1.1 # air slower koef
f = pg.Vector2(0, g)

circles = lib.createLivingCircles(n, maxSpeed)

def on_key_down(key):
    global f, a, circles, n
    if key == pgz.keyboard.keys.A:
        f.x += -a
    if key == pgz.keyboard.keys.D:
        f.x += a
    if key == pgz.keyboard.keys.W:
        f.y += -g
    if key == pgz.keyboard.keys.S:
        f.y += g
    if key == pgz.keyboard.keys.R:
        circles = lib.createLivingCircles(n, maxSpeed)

def update():
    global f, circles, n, maxSpeed

    #if ran.randint(0, 9) == 0:
    #    circles.append(lib.createLivingCircles(n, maxSpeed))

    for i, circle in enumerate(circles):
        if not circle.isAlive():
            circles.pop(i)
        else:
            circle.update()
            circle.accelerate(f)
            circle.move()

    print(len(circles), sys.getsizeof(circles))

def draw():
    global circles, f
    screen.fill((0, 0, 0))

    for circle in circles:
        circle.draw(screen, True)


pgr.go()
