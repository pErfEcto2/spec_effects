import random as ran
from typing import Sized
import pgzero as pgz
import pgzrun as pgr
import pygame as pg
import lib
from lib import HEIGHT, WHITE, WIDTH
import sys
import time as t

a = 2 # accelerate
g = 2 # gravity
maxSpeed = 10
n = 50 # number of smokes
p = 0.01 # density of an air
k = 1.1 # air slower koef
r = 3 # radius of a smoke
c = pg.Color(20, 20, 20) # color of a smoke
timeToSpawn = 0.5
f = pg.Vector2(0, 2)
onPause = False
whitePath = "src/texture.png"
surface = pg.Surface((WIDTH, HEIGHT), pg.SRCALPHA)
speedToDestroy = 5

last = t.time()

#fires = lib.createLivingCircles(n, maxSpeed, speedToDestroy, pos=pg.mouse.get_pos(), rad=r)
fires = []

bg = pg.image.load("src/img.jpg")

def on_key_down(key):
    global f, a, onPause, f
    if key == pgz.keyboard.keys.A:
        f.x += -a
    if key == pgz.keyboard.keys.D:
        f.x += a
    if key == pgz.keyboard.keys.W:
        f.y += -g
    if key == pgz.keyboard.keys.S:
        f.y += g
    if key == pgz.keyboard.keys.SPACE:
        onPause = not onPause
    if key == pgz.keyboard.keys.R:
        f = pg.Vector2(0, 2)

def update():
    global f, fires, n, maxSpeed, last, timeToSpawn, speedToDestroy

    if onPause:
        return
    
    #now = t.time()
    #if now - last > timeToSpawn:
    #    for fire in lib.createLivingCircles(n, maxSpeed, speedToDestroy, pos=pg.mouse.get_pos(), rad=r):
    #        fires.append(fire)
    #    
    #    last = now

    if ran.randint(0, 19) == 0:
        for fire in lib.createLivingCircles(1, maxSpeed, speedToDestroy, pos=pg.Vector2(WIDTH * ran.random(), HEIGHT - r), rad=r):
            fires.append(fire)

    toDelete = []
    for i, fire in enumerate(fires):
        if not fire.isAlive():
            toDelete.append(i)
        else:
            fire.update()
            fire.accelerate(f)
            fire.move()
    fires = [fires[i] for i in range(len(fires)) if i not in toDelete]

    print(len(fires))

    surface = pg.Surface((WIDTH, HEIGHT), pg.SRCALPHA)

def draw():
    global fires, smokes, surface
    surface.fill((0, 0, 0, 25))

    for fire in fires:
        fire.draw(screen)
    
    screen.blit(surface, pos=(0, 0))

pgr.go()
