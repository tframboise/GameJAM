'''
EPITECH PROJECT, 2025
Game JAM
File description:
gem.py
'''

import pygame

class MagicGemDrop(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        image = pygame.image.load("assets/gem.png").convert_alpha()
        self.image = pygame.transform.scale(image, (60, 60))
        self.rect = self.image.get_rect(center=pos)

class MagicGemUI:
    def __init__(self):
        image = pygame.image.load("assets/gem.png").convert_alpha()
        self.image = pygame.transform.scale(image, (50, 50))

    def draw(self, screen, count):
        for i in range(count):
            x = 10 + i * (self.image.get_width() + 5)
            y = 10
            screen.blit(self.image, (x, y))
