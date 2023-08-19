#!/usr/bin/python3

import pygame, sys
from pygame.locals import *
import random, time
import images
from main_game import *

pygame.init()

#Assets
vec = pygame.math.Vector2 
HEIGHT = 450
WIDTH = 600
ACC = 0.6
FRIC = -0.12
FPS = 60

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

class Food():
    #initilizing
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((0, 0, 255))
        self.rect = self.surf.get_rect()

        self.pos = vec((WIDTH - random.randint(30, 200), 20))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    #spinning

    #falling parabola/ gravity/ randomize gravity effect, randomize "jumping" height, randomize horizontal movement

    def fall(self):
        self.acc = vec(0, 0.3)
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

    def update(self):
        hitt = pygame.sprite.spritecollide(food, ground, False)
        collect = pygame.sprite.spritecollide(food, main_char, False)
        if self.vel.y > 0:
            if hitt:
                self.pos.y = hitt[0].rect.top + 1
                self.vel.y = 0
        if collect:
            self.pos = vec((WIDTH - random.randint(30, 200), 20))
            self.vel = vec(0,0)
            #score += score_value


    #all food images
    def sprite(self):
        foods = ['images/bacon.png', 'images/biscuit.png', 'images/french_toast.png',
                'images/fried_egg.png', 'images/hashbrowns.png', 'images/pancake.png', 'images/scrambled_eggs.png']

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    
    displaysurface.fill((0,0,0))
    current_time = pygame.time.get_ticks()
    if current_time > next_object:
        next_object += time_int
        object_list.append(Food())
    
    
    food.update()
    food.fall()
    for object in object_list[:]:
        displaysurface.blit(food.surf, food.rect)


    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
   
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