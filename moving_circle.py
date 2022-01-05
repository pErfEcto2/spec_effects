import random as ran
import pgzero as pgz
import pgzrun as pgr
import pygame as pg
import lib
from lib import HEIGHT, WIDTH

a = 10
f = pg.Vector2(0, 50)

circles = []
for _ in range(100):
    circles.append(lib.Circle(pg.Vector2(WIDTH * ran.random(), HEIGHT * ran.random()), ran.randint(5000, 10000)))

def on_key_down(key):
    global f, a
    if key == pgz.keyboard.keys.A:
        f.x += -a
    if key == pgz.keyboard.keys.D:
        f.x += a

def update():
    global f, circles

    for circle in circles:
        circle.accelerate(f)
        circle.move()


def draw():
    global circles, f
    screen.fill((0, 0, 0))

    for circle in circles:
        circle.draw(screen)
        circle.drawSpeed(screen)


pgr.go()
