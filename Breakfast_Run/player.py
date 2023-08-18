#!/usr/bin/python3
"This will have animation, moving, and visuals for player"

import pygame, sys
from pygame.locals import *
import random, time


class Player(pygame.sprite.Sprite):
    #initilized
    def __init__(self):
        super().__init__()
        self.image == pygame.image.load("images/player.png")

    #animation

    #jump physics

    #moving