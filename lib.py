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
    def __init__(self, pos, r, box_size):
        self.pos = pos
        self.radius = r
        self.true_radius = r
        self.color = (255, 255, 255)
        n = 15
        self.v = pg.Vector3(ran.randint(-n, n), ran.randint(-n, n), ran.randint(-n, n))
        self.box_size = box_size
    
    def move(self):
        self.pos += self.v
        
        if self.pos.x + self.radius >= WIDTH or self.pos.x - self.radius<= 0:
            self.v.x *= -1
        if self.pos.y + self.radius >= HEIGHT or self.pos.y - self.radius <= 0:
            self.v.y *= -1
        if self.pos.z + self.radius>= DEPTH or self.pos.z - self.radius <= 0:
            self.v.z *= -1
    
    def modRadius(self):
        pos = self.pos
        r = self.true_radius
        self.radius = (r * LENGTH) / (LENGTH + pos.z)
    
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

class Walker2D():
    def __init__(self, pos, r, box_size):
        self.pos = pos
        self.radius = r
        self.color = (255, 255, 255)
        n = 15
        self.v = pg.Vector2(ran.randint(-n, n), ran.randint(-n, n))
        self.box_size = box_size
        self.vec_ac = pg.Vector2(0, 0)
    
    def move(self):
        vec = pg.mouse.get_pos() - self.pos
        dist = math.sqrt(vec[0] ** 2 + vec[1] ** 2)
        ac = 1 / dist
        k = ac / dist
        dx = self.pos[0] - pg.mouse.get_pos()[0]
        dy = self.pos[1] - pg.mouse.get_pos()[1]
        ac_vec = pg.Vector2(self.vec_ac[0] + dx * k, self.vec_ac[1] + dy * k)

        self.v = ac_vec
        self.pos += self.v
        
        if self.pos.x + self.radius >= WIDTH or self.pos.x - self.radius<= 0:
            self.v.x *= -1
        if self.pos.y + self.radius >= HEIGHT or self.pos.y - self.radius <= 0:
            self.v.y *= -1
    
    def setRadius(self, r):
        self.radius = r
    
    def getPos(self):
        return (self.pos.x, self.pos.y)

    def getRadius(self):
        return self.radius
    
    def getColor(self):
        return self.color