'''
EPITECH PROJECT, 2025
Game JAM
File description:
gem.py
'''

import pygame
import random

class MagicGemDrop(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("assets/gem.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect(center=pos)

class MagicGemUI:
    def __init__(self):
        self.icon = pygame.image.load("assets/gem.png").convert_alpha()
        self.icon = pygame.transform.scale(self.icon, (30, 30))

    def draw(self, screen, count):
        for i in range(count):
            screen.blit(self.icon, (10 + i * 35, 10))
