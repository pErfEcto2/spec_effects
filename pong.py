#!/home/projects/python/spec_effects/env/bin/python3


import pgzrun as pgr
import pgzero as pgz
import pygame as pg
import random as ran
from   lib import WIDTH, HEIGHT, WHITE, GREEN, RED

maxSpeed = 15
botMaxSpeed = 10
r = 10 # circle radius
score = pg.Vector2(0, 0)
k = 20 # decrease circle vertical acceleration
maxScore = 10
start = True
run = False
rectSize = pg.Vector2(10, 150)

userRectPos = pg.Vector2(5, HEIGHT / 2 - rectSize[1] / 2)
moveDown = False
moveUp = False
win = False
lose = False

botRectPos = pg.Vector2(WIDTH - rectSize[0] - 5, HEIGHT / 2 - rectSize[1] / 2)

circlePos = pg.Vector2(WIDTH / 2, HEIGHT / 2)

circleVel = pg.Vector2(maxSpeed, ran.randint(-maxSpeed, maxSpeed))

def on_key_down(key):
    global moveDown, moveUp, win, score, lose, circlePos, circleVel, start, run
    if key == pgz.keyboard.keys.UP and not (win or lose):
        moveUp = True
        moveDown = False

    elif key == pgz.keyboard.keys.DOWN and not (win or lose):
        moveUp = False
        moveDown = True

    elif key == pgz.keyboard.keys.RETURN:
        if win or lose:
            win = False
            lose = False
            score = pg.Vector2(0, 0)
            circlePos = pg.Vector2(WIDTH / 2, HEIGHT / 2)
            circleVel = pg.Vector2(maxSpeed, ran.randint(-maxSpeed, maxSpeed))

        elif start:
            start = False
            run = True
            
    elif key == pgz.keyboard.keys.ESCAPE:
        exit()

def on_key_up(key):
    global moveDown, moveUp
    if key == pgz.keyboard.keys.UP or key == pgz.keyboard.keys.DOWN:
        moveUp = False
        moveDown = False

def update():
    global circleVel, circlePos, userRectPos, notRunning, moveDown, moveUp, r, maxSpeed, k, botMaxSpeed
    if run:
        userRect = pgz.rect.Rect(userRectPos, rectSize)
        botRect = pgz.rect.Rect(botRectPos, rectSize)

        circlePos += circleVel

        if moveDown:
            userRectPos[1] += maxSpeed
        elif moveUp:
            userRectPos[1] -= maxSpeed

        if userRectPos[1] <= 0:
            userRectPos[1] = 0
        if userRectPos[1] + rectSize[1] >= HEIGHT:
            userRectPos[1] = HEIGHT - rectSize[1]

        dy = circlePos[1] - r - botRectPos[1] - rectSize[1] / 2
        if dy > 0:
            botRectPos[1] += botMaxSpeed
        elif dy < 0:
            botRectPos[1] -= botMaxSpeed


        if botRectPos[1] <= 0:
            botRectPos[1] = 0
        if botRectPos[1] + rectSize[1] >= HEIGHT:
            botRectPos[1] = HEIGHT - rectSize[1]

        if userRect.colliderect(pgz.rect.Rect(circlePos, (2 * r, 2 * r))):
            circleVel[0] *= -1
            circlePos[0] = userRectPos[0] + rectSize[0] + 5
            dy = (circlePos[1] + r) - (userRectPos[1] + rectSize[1] / 2) 
            circleVel[1] += dy / k

        if botRect.colliderect(pgz.rect.Rect(circlePos, (2 * r, 2 * r))):
            circleVel[0] *= -1
            circlePos[0] = botRectPos[0] - 2 * r + 5
            dy = (circlePos[1] + r) - (userRectPos[1] + rectSize[1] / 2) 
            circleVel[1] += dy / k

        if circlePos[0] <= 0:
            score[1] += 1
            circlePos = pg.Vector2(WIDTH / 2, HEIGHT / 2)
            circleVel = pg.Vector2(maxSpeed, ran.randint(-maxSpeed, maxSpeed))
            notRunning = True

        if circlePos[0] + r >= WIDTH:
            score[0] += 1
            circlePos = pg.Vector2(WIDTH / 2, HEIGHT / 2)
            circleVel = pg.Vector2(maxSpeed, ran.randint(-maxSpeed, maxSpeed))
            notRunning = True

        if circlePos[1] - r <= 0 or circlePos[1] + r >= HEIGHT:
            circleVel[1] *= -1

def draw():
    global notRunning, botRectPos, userRectPos, circlePos, win, lose, maxScore, start
    screen.fill((0, 0, 0))

    userRect = pgz.rect.Rect(userRectPos, rectSize)
    botRect = pgz.rect.Rect(botRectPos, rectSize)

    if start:
        screen.draw.text("WELCOME!", (WIDTH / 2 - 80, HEIGHT / 2 - 90), fontsize=40)
        screen.draw.text("YOURS SIDE IS LEFT, BOT'S SIDE IS RIGHT", (WIDTH / 2 - 300, HEIGHT / 2 - 50), fontsize=40)
        screen.draw.text("CONTROLS: UP ARROW - MOVE UP, DOWN ARROW - MOVE DOWN", (WIDTH / 2 - 450, HEIGHT / 2 - 10), fontsize=40)
        screen.draw.text("PRESS ENTER TO START", (WIDTH / 2 - 180, HEIGHT / 2 + 30), fontsize=40)
        screen.draw.text("PRESS ESCAPE TO EXIT", (WIDTH / 2 - 180, HEIGHT / 2 + 70), fontsize=40)


    if score[0] >= maxScore:
        screen.draw.text("YOU WIN", (WIDTH / 2 - 110, HEIGHT / 2 - 50), fontsize=70, color=GREEN)
        screen.draw.text("PRESS ESCAPE TO EXIT", (WIDTH / 2 - 170, HEIGHT / 2 + 20), fontsize=40)
        screen.draw.text("PRESS ENTER TO CONTINUE", (WIDTH / 2 - 200, HEIGHT / 2 + 70), fontsize=40)
        win = True
        lose = False
        run = False
    
    elif score[1] >= maxScore:
        screen.draw.text("YOU LOSE", (WIDTH / 2 - 130, HEIGHT / 2 - 50), fontsize=70, color=RED)
        screen.draw.text("PRESS ESCAPE TO EXIT", (WIDTH / 2 - 170, HEIGHT / 2 + 20), fontsize=40)
        screen.draw.text("PRESS ENTER TO CONTINUE", (WIDTH / 2 - 200, HEIGHT / 2 + 70), fontsize=40)
        lose = False
        lose = True
        ran = False
    
    elif not start:
        screen.draw.filled_circle(pos=circlePos, radius=r, color=WHITE)

        screen.draw.filled_rect(userRect, WHITE)
        screen.draw.filled_rect(botRect, WHITE)

        s = f"{int(score[0])}   {int(score[1])}"
        screen.draw.text(s, (WIDTH / 2 - 40, 10), fontsize=40)

pgr.go()