import pygame
import math
import random
import os

pygame.init()

screen = pygame.display.set_mode((600, 600))

pygame.display.set_caption("Snake Wizard")

programIcon = pygame.image.load(os.path.join('swizard.png'))

pygame.display.set_icon(programIcon)

stage = "menu"

def napisz(tekst, x, y, rozmiar):
    cz = pygame.font.SysFont("Arial", rozmiar)
    rend = cz.render(tekst, 1, (50, 255, 100))
    x = (600 - rend.get_rect().width)/2
    y = (600 - rend.get_rect().height)/2
    screen.blit(rend, (x, y))

class Wizard:
    def __init__(self, n, m, width, height, vel):
        self.n = n
        self.m = m
        self.width = width
        self.height = height
        self.vel = vel
        self.ksztalt = pygame.Rect(self.n, self.m, self.width, self.height)
        self.grafika = pygame.image.load(os.path.join('swizard.png'))
    def rysuj(self):
        screen.blit(self.grafika, (self.n, self.m))
    def changes(self):
        self.grafika = pygame.image.load(os.path.join('ssnake.png'))
        self.vel = 150
    def backton(self):
        self.grafika = pygame.image.load(os.path.join('swizard.png'))
        self.vel = 100

class Enemy:
    def __init__(self, a, b, w, h):
        self.a = a
        self.b = b
        self.w = w
        self.h = h
        self.shape = pygame.Rect(self.a, self.b, self.w, self.h)
        self.wyglad = pygame.image.load(os.path.join('fireball.png'))
    def drawit(self):
        screen.blit(self.wyglad, (self.a, self.b))
    def chase(self):
        if(self.a < x):
            self.a += 10
        if(self.a > x):
            self.a -= 10
        if(self.b < y):
            self.b += 10
        if(self.b > y):
            self.b -= 10
    def dash(self):
        self.a += random.randint(-30, 30)
        self.b += random.randint(-30, 30)

getTicksLastFrame = pygame.time.get_ticks()
xd = Enemy(250, 250, 20, 20)
snake = Wizard(50, 50, 20, 20, 100)
run = True
l = 0
c = 1
p = False
areyou = False
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                if ((stage != "game") and (p == False)):
                    stage = "game"
    screen.fill((255, 255, 255))
    if stage == "menu":
        napisz("Snake Wizard | Made by Adam Wasiak | Press s, to start.", 0, 0, 20)
    elif stage == "game":
        l += 1
        x = snake.n
        y = snake.m
        pygame.time.delay(100)
        t = pygame.time.get_ticks()
        # deltaTime in seconds.
        deltaTime = (t - getTicksLastFrame) / 1000.0
        getTicksLastFrame = t


        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x > 5:
            snake.n -= snake.vel * deltaTime 
        if keys[pygame.K_RIGHT] and x < 600 - snake.width - 5:
            snake.n += snake.vel * deltaTime
        if keys[pygame.K_UP] and y > 5:
            snake.m -= snake.vel * deltaTime
        if keys[pygame.K_DOWN] and y < 600 - snake.height - 5:
            snake.m += snake.vel * deltaTime
        if keys[pygame.K_SPACE] and c > 0:
            snake.changes()
            c -= 1
            areyou = True

        
        xd.shape = pygame.Rect(xd.a, xd.b, xd.w, xd.h)
        snake.ksztalt = pygame.Rect(snake.n, snake.m, snake.width, snake.height)
        xd.drawit()
        snake.rysuj()
        xd.chase()
        xd.dash()
        if(xd.shape.colliderect(snake.ksztalt) and areyou == False):
            stage = "end"
            p = True
        elif(xd.shape.colliderect(snake.ksztalt) and areyou == True):
            areyou = False
            snake.n = 50
            snake.m = 50
            snake.backton()
    elif stage == "end":
        q = "Your score is " + str(l)
        napisz(q, 0, 0, 20)
    pygame.display.update()


pygame.quit()
