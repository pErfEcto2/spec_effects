import random as ran
from typing import Sized
import pgzero as pgz
import pgzrun as pgr
import pygame as pg
import lib
from lib import HEIGHT, WHITE, WIDTH
import sys
import time as t

a = 10 # accelerate
g = 10 # gravity
maxSpeed = 4
n = 10 # number of smokes
p = 0.01 # density of an air
k = 1.1 # air slower koef
r = 5 # radius of a smoke
c = pg.Color(20, 20, 20) # color of a smoke
timeToSpawn = 0
f = pg.Vector2(0, 0)
onPause = False
whitePath = "src/texture.png"
firePath = "src/fire.png"
surface = pg.Surface((WIDTH, HEIGHT), pg.SRCALPHA)
speedToDestroy = 0.1

last = t.time()

fires = lib.createLivingCircles(n, maxSpeed, pos=pg.Vector2(WIDTH / 2, HEIGHT / 2), rad=r, speedToDestroy=speedToDestroy)
smokes = lib.createLivingCircles(n, maxSpeed, pos=pg.Vector2(WIDTH / 2, HEIGHT / 2), rad=r, speedToDestroy=speedToDestroy)

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
        f = pg.Vector2(0, -50)

def update():
    global f, fires, n, maxSpeed, last, timeToSpawn, smokes, c, speedToDestroy

    if onPause:
        return
    now = t.time()
    if now - last > timeToSpawn:
        for fire in lib.createLivingCircles(n, maxSpeed, pos=pg.Vector2(WIDTH / 2, HEIGHT / 2), rad=r, speedToDestroy=speedToDestroy):
            fires.append(fire)
        
        for smoke in lib.createLivingCircles(n, maxSpeed, pos=pg.Vector2(WIDTH / 2, HEIGHT / 2), rad=r, speedToDestroy=speedToDestroy):
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
    global fires, smokes, surface
    surface.fill((0, 0, 0, 25))

    for smoke in smokes:
        smoke.draw(screen)
    for fire in fires:
        fire.draw(screen)
    
    screen.blit(surface, pos=(0, 0))

pgr.go()
