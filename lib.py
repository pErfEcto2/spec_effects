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

class Walker3D():
    def __init__(self, pos, r, box_size, v):
        self.pos = pos
        self.radius = r
        self.true_radius = r
        self.color = (255, 255, 255)
        self.v = v
        self.box_size = box_size
    
    def move(self):
        self.pos += self.v
        
        if self.pos.x <= 0:
            self.pos.x = self.radius
            self.v.x *= -1
        if self.pos.x + 2 * self.radius >= WIDTH:
            self.pos.x = WIDTH - 2 * self.radius
            self.v.x *= -1
        
        if self.pos.y <= 0:
            self.pos.y = self.radius
            self.v.y *= -1
        if self.pos.y + self.radius >= HEIGHT:
            self.pos.y = HEIGHT - self.radius
            self.v.y *= -1
        
        if self.pos.z + 2 * self.radius>= DEPTH or self.pos.z <= 0:
            self.v.z *= -1
        
    
    def modRadius(self):
        pos = self.pos
        r = self.true_radius
        self.radius = (r * LENGTH) / (LENGTH + pos.z)
    
    def draw(self, scr):
        scr.draw.filled_circle(pos=(self.pos.x, self.pos.y), radius=self.radius, color=self.color)
    
    def setRadius(self, r):
        self.radius = r
    
    def getPos(self):
        return (self.pos.x, self.pos.y)

    def getRadius(self):
        return self.true_radius
    
    def getVisibleRadius(self):
        return self.radius
    
    def getColor(self):
        return self.color
    
    def incVel(self, acc):
        self.v += acc
    
    def getSpeed(self):
        return self.v
    
    def decreaseSpeed(self, n):
        self.v //= n
    
    def setPos(self, p):
        self.pos = p

class Walker2D():
    def __init__(self, pos, r, box_size, v=None, fade=True):
        self.pos = pos
        self.radius = r
        self.color = (255 * ran.random(), 255 * ran.random(), 255 * ran.random())
        n = 5

        if not v:
            self.v = pg.Vector2(ran.randint(-n, n), ran.randint(-n, n))
        else:
            self.v = v
        
        self.box_size = box_size
        self.vec_ac = pg.Vector2(0, 0)
        self.k = 1
        self.g = pg.Vector2(0, 0.3)
        self.frames = ran.randint(-5, 5)
        self.fade = fade
    
    def move(self):
        self.frames += 1

        self.v /= self.k
        self.v += self.g
        self.pos += self.v

        if self.pos.x + self.r >= WIDTH:
            self.pos.x = WIDTH - self.r
            self.v.x *= -1
        if self.pos.x - self.r <= 0:
            self.pos.x = self.r
            self.v.x *= -1

        if self.pos.y + self.r >= HEIGHT:
            self.pos.y = HEIGHT - self.r
            self.v.y *= -1
        if self.pos.y - self.r <= 0:
            self.pos.y = self.r
            self.v.y *= -1
        
        if self.fade:
            self.color = (abs(self.color[0] - 10), abs(self.color[1] - 10), abs(self.color[2] - 10))
    
    def draw(self, scr):
        scr.draw.filled_circle(pos=self.pos, radius=self.radius, color=self.color)
    
    def setRadius(self, r):
        self.radius = r
    
    def getPos(self):
        return self.pos

    def getRadius(self):
        return self.radius
    
    def getColor(self):
        return self.color
    
    def getFrames(self):
        return self.frames
    
    def getVel(self):
        return self.v

class Circle():
    def __init__(self, pos: pg.Vector2, m: int, maxSp: int, v: pg.Vector2 = None, r: int = None) -> None:
        self.pos = pos
        self.mass = m
        self.acc = pg.Vector2(0, 0)

        if not v:
            self.v = pg.Vector2(0, 0)
        else:
            self.v = v
        
        if not r:
            self.r = m / 1000
        else:
            self.r = r
        
        self.color = (255 * ran.random(), 255 * ran.random(), 255 * ran.random())
        self.maxSpeed = maxSp
        self.S = 3.1415 * self.r ** 2
        #self.img = None
    
    def accelerate(self, f: pg.Vector2) -> None:
        self.acc = f / self.mass
    
    def move(self) -> None:
        if self.v.length() > self.maxSpeed:
            self.v.scale_to_length(self.maxSpeed)
        
        self.pos += self.v
        
        #self.v += self.acc
        #if self.pos.x + self.r >= WIDTH:
        #    self.pos.x = WIDTH - self.r
        #    #self.v.x *= -1
        #if self.pos.x <= 0:
        #    self.pos.x = self.r
        #    #self.v.x *= -1
        #
        #if self.pos.y + self.r >= HEIGHT:
        #    self.pos.y = HEIGHT - self.r
        #    #self.v.y *= -1
        #if self.pos.y - self.r <= 0:
        #    self.pos.y = self.r
        #    #self.v.y *= -1
        
    def drawSpeed(self, scr) -> None:
        scr.draw.line(self.pos, self.pos + self.v * 2, color=RED)
    
    def draw(self, scr, filled: bool) -> None:
        if filled:
            scr.draw.filled_circle(pos=self.pos, radius=self.r, color=self.color)
        else:
            scr.draw.circle(pos=self.pos, radius=self.r, color=self.color)
                 
    def loadImg(self, path, scaleTo: tuple = None) -> None:
        self.img = pg.image.load(path).convert_alpha()
        if scaleTo:
            self.img = pg.transform.scale(self.img, scaleTo)
    
    def getS(self) -> float:
        return self.S
    
    def getSpeed(self) -> pg.Vector2:
        return self.v

    def decreaseSpeed(self, n: float) -> None:
        self.v /= n

def createCircles(n: int, maxS: int, color: tuple, pos: pg.Vector2 = None, rad: int = None) -> list:
    l = []
    if not pos:
        pos = pg.Vector2(WIDTH / 2, HEIGHT / 2)
    
    if not rad:
        rad = ran.randint(5, 15)
    
    for _ in range(n):
        l.append(Circle(pos,
                        ran.randint(10000, 100000),
                        maxS,
                        color,
                        pg.Vector2(ran.randint(-10, 10), ran.randint(-30, 5)),
                        rad))
    return l

class livingCircle(Circle):
    def __init__(self, pos: pg.Vector2, m: int, maxSp: int, scale: tuple, c: tuple = None, v: pg.Vector2 = None, r: int = None, path: str = None, speedToDestroy: float = 5) -> None:
        super().__init__(pos, m, maxSp, v=v, r=r)
        if not c:
            c = (255 * ran.random(), 0, 0)
        self.color = c
        self.scaleTo = scale
        self.lifes = 255
        self.speedToDestroy = speedToDestroy

        if path:
            super().loadImg(path, self.scaleTo)
            self.parentHasImg = True
        else:
            self.parentHasImg = False
    
    def update(self) -> None:
        self.lifes -= self.speedToDestroy
        self.r -= self.speedToDestroy / 3.5
    
    def isAlive(self) -> bool:
        return self.lifes > 0 and self.r > 0

    def draw(self, scr) -> None:
        if self.parentHasImg:
            copyImg = self.img.copy()
            copyImg.set_alpha(self.lifes)
            scr.surface.blit(copyImg, self.pos)
        else:
            super().draw(scr, True)

def createLivingCircles(n: int, maxS: int, speedToDestroy: float, path: str = None, c: tuple = None, pos: pg.Vector2 = None, rad: int = None, v: pg.Vector2 = None) -> list:
    l = []
    if not pos:
        pos = pg.Vector2(WIDTH / 2, HEIGHT / 2)
    
    if not rad:
        rad = ran.randint(5, 15)

    for _ in range(n):
        l.append(livingCircle(pos=pos,
                              m=ran.randint(10, 100),
                              maxSp=maxS,
                              scale=(rad, rad),
                              c=c,
                              v=pg.Vector2(ran.randint(-5, 5), ran.randint(-5, 5)),
                              r=rad,
                              path=path,
                              speedToDestroy=speedToDestroy))
    return l

def writeTiFile(path: str, message: str) -> None:
    with open(path, "w") as f:
        f.write(message)

def readFromFile(path) -> str:
    with open(path, "r") as f:
        return f.read()