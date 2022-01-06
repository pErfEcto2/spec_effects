import random as ran
from typing import Sized
import pgzero as pgz
import pgzrun as pgr
import pygame as pg
import lib
from lib import HEIGHT, WIDTH
import sys
import time as t

a = 100000 # accelerate
g = 10000 # gravity
maxSpeed = 5
n = 10 # number of fires
p = 0.01 # density of an air
k = 1.1 # air slower koef
r = 30 # radius of a smoke
c = (7, 7, 7) # color of a smoke
timeToSpawn = 0.02
f = pg.Vector2(0, -50000)
onPause = False

last = t.time()

fires = lib.createLivingCircles(n, maxSpeed, pos=pg.mouse.get_pos())
smokes = lib.createLivingCircles(n, maxSpeed, c=c, pos=pg.mouse.get_pos(), rad=r)

def on_key_down(key):
    global f, a, fires, n, onPause, smokes, r, c
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

def update():
    global f, fires, n, maxSpeed, last, timeToSpawn, smokes, c

    if onPause:
        return
    now = t.time()
    if now - last > timeToSpawn:
        for fire in lib.createLivingCircles(n, maxSpeed, pos=pg.mouse.get_pos()):
            fires.append(fire)
        
        for smoke in lib.createLivingCircles(n, maxSpeed, c=c, pos=pg.mouse.get_pos(), rad=r):
            smokes.append(smoke)
        
        last = now

    toDelete = []
    for i, fire in enumerate(fires):
        if not fire.isAlive():
            toDelete.append(i)
        else:
            fire.update()
            fire.accelerate(f)
            fire.move()
    fires = [fires[i] for i in range(len(fires)) if i not in toDelete]

    toDelete = []
    for i, smoke in enumerate(smokes):
        if not smoke.isAlive():
            toDelete.append(i)
        else:
            smoke.update()
            smoke.accelerate(f)
            smoke.move()
    smokes = [smokes[i] for i in range(len(smokes)) if i not in toDelete]

    print(len(fires) + len(smokes))

def draw():
    global fires, smokes
    screen.fill((0, 0, 0))

    for smoke in smokes:
        smoke.draw(screen, True)
    for fire in fires:
        fire.draw(screen, True)

pgr.go()
