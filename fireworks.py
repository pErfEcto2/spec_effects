import pgzrun as pgr
import pgzero as pgz
import pygame as pg
import random as ran
from lib import WIDTH, HEIGHT, WHITE, GREEN, RED
import lib

n = 2
frameLimit = 20

def createPartExpl(particles, num, pos=None):
    if not pos:
        pos = pg.Vector2(WIDTH / 2 + ran.randint(-5, 5), HEIGHT / 2 + ran.randint(-5, 5))
    for _ in range(num):
        particles.append(lib.Walker2D(pos, 5, pg.Vector2(WIDTH, HEIGHT)))

fireParticles = []
fires = []

def on_key_down():
    global fires, n
    fires.append(lib.Walker2D(pg.Vector2(WIDTH * ran.random(), HEIGHT), 10, pg.Vector2(WIDTH, HEIGHT + 200),
                                  pg.Vector2(ran.randint(-5, 5), ran.randint(10, 20)), False))

def update():
    global fireParticles, frameLimit, fires, n

    if ran.randint(0, 10) == 0:
        fires.append(lib.Walker2D(pg.Vector2(WIDTH * ran.random(), HEIGHT), n, pg.Vector2(WIDTH, HEIGHT + 200),
                                  pg.Vector2(ran.randint(-5, 5), ran.randint(10, 20)), False))

    for i, expl in enumerate(fires):
        if expl.getVel().y <= 0:
            expl.move()
        else:
            createPartExpl(fireParticles, 10, expl.getPos())
            fires.pop(i)
    
    #for j, fire in enumerate(fireParticles):
    #    if fire.getFrames() < frameLimit:
    #        fire.move()
    #    else:
    #        fireParticles.pop(j)
    
    print(len(fires), len(fireParticles))

def draw():
    global fires, fireParticles
    screen.fill((0, 0, 0))

    print(len(fires), len(fireParticles))
    
    for fire in fires:
        fire.draw(screen)
    
    for part in fireParticles:
        part.draw(screen)
        

pgr.go()