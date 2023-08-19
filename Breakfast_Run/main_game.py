#!/usr/bin/python3
"This file will run everything in successtion and call all future functions"
import pygame, sys
from pygame.locals import *
import random, time
import images

pygame.init()

#Assets
vec = pygame.math.Vector2 
HEIGHT = 450
WIDTH = 600
ACC = 0.6
FRIC = -0.12
FPS = 60
BACKGROUND = pygame.image.load("background.png")

#7 imgaes
FOODS = ['images/bacon.png', 'images/biscuit.png', 'images/french_toast.png',
        'images/fried_egg.png', 'images/hashbrowns.png', 'images/pancake.png', 'images/scrambled_eggs.png']


SCORE = 0
FONT = pygame.font.SysFont(None, 30)

FramePerSec = pygame.time.Clock()

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")


#Classes
class Player(pygame.sprite.Sprite):
    #initilized
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

        self.pos = vec((10, 385))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    #animation
    "Look up"

    #jump physics
    def jump(self):
        hits = pygame.sprite.spritecollide(self, ground, False)
        if hits:
            self.vel.y = -12

    def move(self):
        self.acc = vec(0,0.4)
   
        pressed_keys = pygame.key.get_pressed()            
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC

        if pressed_keys[K_UP]:
            self.jump()
            
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        
        if self.pos.x > WIDTH:
            self.pos.x = WIDTH
        if self.pos.x < 0:
            self.pos.x = 0
           
        self.rect.midbottom = self.pos

    def update(self):
        hits = pygame.sprite.spritecollide(P1, ground, False)
        if P1.vel.y > 0:
            if hits:
                self.pos.y = hits[0].rect.top + 1
                self.vel.y = 0


class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 10))
        self.surf.fill((0, 255, 0))
        self.rect = self.surf.get_rect(center =(WIDTH/2, HEIGHT))


class Food():
    #initilizing
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((40, 40))
        self.image = pygame.image.load(FOODS[random.randrange(0, 7)])
        self.image = pygame.transform.scale(self.image, (40, 40))
        #self.surf.fill((0, 0, 255))
        self.rect = self.surf.get_rect()
        self.center = 10

        self.x = WIDTH - random.randrange(20, 150)
        self.y = HEIGHT / 10
        self.pos = vec((self.x, self.y))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    #spinning

    #falling parabola/ gravity/ randomize gravity effect, randomize "jumping" height, randomize horizontal movement

    def fall(self):
        self.acc = vec(random.randrange(-8, 0) / 10, random.randrange(1, 2) / 10)
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.2 * self.acc
        self.rect.midbottom = self.pos

    def update(self):
        hitt = pygame.sprite.spritecollide(food, ground, False)
        if self.vel.y > 0:
            if hitt:
                self.pos.y = hitt[0].rect.top + 1
                self.vel.y = 0

    #all food images

        foods = ['images/bacon.png', 'images/biscuit.png', 'images/french_toast.png',
                'images/fried_egg.png', 'images/hashbrowns.png', 'images/pancake.png', 'images/scrambled_eggs.png']

class Pigeon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill

    def move(self):
        self.add()

P1 = Player()
Plat = Platform()
pigeon = Pigeon()
food = Food()

#Groups
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(Plat)
#all_sprites.add(pigeon)
#all_sprites.add(food)

ground = pygame.sprite.Group()
ground.add(Plat)

main_char = pygame.sprite.Group()
main_char.add(P1)

#start game, run cutscene

#main menu

object_list = []
time_int = 1500
next_object = 0
collect = pygame.sprite.spritecollide(food, main_char, False)

#game start
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    P1.update()
    P1.move()
    food.update()

    current_time = pygame.time.get_ticks()
    if current_time > next_object:
        next_object += time_int
        time_int -= 10
        object_list.append(Food())

    WINDOW.fill((0,0,0))

    for object in object_list[:]:
        collect = pygame.sprite.spritecollide(object, main_char, False)
        WINDOW.blit(object.image, object.rect)
        object.fall()
        object.update()
        if collect:
            object_list.remove(object)
            SCORE += 100
        


    for entity in all_sprites:
        WINDOW.blit(entity.surf, entity.rect)

    score_text = FONT.render("Score: " + str(SCORE), True, (255, 255, 255))
    WINDOW.blit(score_text, (10, 10))

    pygame.display.update()
    FramePerSec.tick(FPS)

#difficulty increaser

#run all sprites

#falling food randomizer

#character control

#collision

#score adding

#food missed

#hunger bar

#game over

#stop menu